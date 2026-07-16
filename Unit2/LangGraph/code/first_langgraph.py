"""
first_langgraph.py — Alfred 邮件处理图（对齐 HF Agents Course · Unit 2 · LangGraph）
Alfred email-processing graph, aligned with HF Agents Course · Unit 2 · LangGraph.

课程出处 / Source: https://huggingface.co/learn/agents-course

这是课程中 Alfred 用 LangGraph 处理邮件的完整示例：
- 读取邮件 -> 分类（本地规则判断是否垃圾邮件/类别）-> 草拟回复 -> 呈报
- 用 StateGraph 维护共享状态 EmailState，含一条条件边分流垃圾/正常邮件
课程里这部分用本地规则引擎，不依赖 LLM，因此开箱即跑。
pip install langgraph
"""

from pathlib import Path
from typing import Any, Dict, Literal, Optional, TypedDict

from langgraph.graph import END, START, StateGraph


class EmailState(TypedDict):
    email: Dict[str, Any]
    is_spam: Optional[bool]
    spam_reason: Optional[str]
    email_category: Optional[str]
    draft_response: Optional[str]
    messages: list[Dict[str, str]]


SPAM_SIGNALS = {
    "lottery": "mentions a lottery prize",
    "won": "claims the recipient won money",
    "prize": "pushes an unexpected prize",
    "bank details": "asks for sensitive financial information",
    "processing fee": "requests an advance fee",
    "urgent": "uses urgency to pressure the recipient",
}

CATEGORY_SIGNALS = {
    "question": "inquiry",
    "interested": "inquiry",
    "schedule": "request",
    "call": "request",
    "thank": "thank you",
    "issue": "complaint",
    "problem": "complaint",
    "information": "information",
}


def classify_email_locally(email: Dict[str, Any]) -> Dict[str, Optional[str] | bool]:
    text = f"{email['subject']} {email['body']}".lower()

    for keyword, reason in SPAM_SIGNALS.items():
        if keyword in text:
            return {
                "is_spam": True,
                "spam_reason": reason,
                "email_category": None,
                "analysis": f"Marked as spam because the message {reason}.",
            }

    category = "general"
    for keyword, detected_category in CATEGORY_SIGNALS.items():
        if keyword in text:
            category = detected_category
            break

    return {
        "is_spam": False,
        "spam_reason": None,
        "email_category": category,
        "analysis": f"Marked as legitimate and categorized as {category}.",
    }


def draft_response_locally(email: Dict[str, Any], category: str) -> str:
    sender_name = email["sender"].split("@")[0].replace(".", " ").title()

    if category == "inquiry":
        body = (
            "Thank you for your interest. Mr. Hugg would be happy to learn more "
            "about your needs and discuss how he may be able to help."
        )
    elif category == "request":
        body = (
            "Thank you for reaching out. I will share your request with Mr. Hugg "
            "and we will follow up shortly regarding availability."
        )
    elif category == "thank you":
        body = "Your kind note is appreciated. I will make sure Mr. Hugg sees your message."
    elif category == "complaint":
        body = (
            "Thank you for flagging this issue. We take your concern seriously and "
            "will review it promptly."
        )
    else:
        body = "Thank you for your message. Mr. Hugg will review it and respond as appropriate."

    return (
        f"Dear {sender_name},\n\n"
        f"{body}\n\n"
        "Kind regards,\n"
        "Alfred\n"
        "on behalf of Mr. Hugg"
    )


def read_email(state: EmailState) -> Dict[str, Any]:
    """Log the incoming email without changing the graph state."""
    email = state["email"]
    print(
        f"Alfred is processing an email from {email['sender']} "
        f"with subject: {email['subject']}"
    )
    return {}


def classify_email(state: EmailState) -> Dict[str, Any]:
    """Classify the email with local rules and record the analysis."""
    result = classify_email_locally(state["email"])
    new_messages = state.get("messages", []) + [
        {"role": "system", "content": "Local rules engine analyzed the email."},
        {"role": "assistant", "content": str(result["analysis"])},
    ]
    return {
        "is_spam": result["is_spam"],
        "spam_reason": result["spam_reason"],
        "email_category": result["email_category"],
        "messages": new_messages,
    }


def handle_spam(state: EmailState) -> Dict[str, Any]:
    """Handle spam by printing the reason and ending the workflow."""
    print(f"Alfred has marked the email as spam. Reason: {state['spam_reason']}")
    print("The email has been moved to the spam folder.")
    return {}


def draft_response(state: EmailState) -> Dict[str, Any]:
    """Create a draft response for legitimate email."""
    category = state["email_category"] or "general"
    response_text = draft_response_locally(state["email"], category)
    new_messages = state.get("messages", []) + [
        {"role": "assistant", "content": response_text},
    ]
    return {
        "draft_response": response_text,
        "messages": new_messages,
    }


def notify_mr_hugg(state: EmailState) -> Dict[str, Any]:
    """Print the prepared response for review."""
    email = state["email"]
    print("\n" + "=" * 50)
    print(f"Sir, you've received an email from {email['sender']}.")
    print(f"Subject: {email['subject']}")
    print(f"Category: {state['email_category']}")
    print("\nI've prepared a draft response for your review:")
    print("-" * 50)
    print(state["draft_response"])
    print("=" * 50 + "\n")
    return {}


def route_email(state: EmailState) -> Literal["spam", "legitimate"]:
    """Choose the next node after classification."""
    if state["is_spam"]:
        return "spam"
    return "legitimate"


email_graph = StateGraph(EmailState)
email_graph.add_node("read_email", read_email)
email_graph.add_node("classify_email", classify_email)
email_graph.add_node("handle_spam", handle_spam)
email_graph.add_node("draft_response", draft_response)
email_graph.add_node("notify_mr_hugg", notify_mr_hugg)

email_graph.add_edge(START, "read_email")
email_graph.add_edge("read_email", "classify_email")
email_graph.add_conditional_edges(
    "classify_email",
    route_email,
    {
        "spam": "handle_spam",
        "legitimate": "draft_response",
    },
)
email_graph.add_edge("handle_spam", END)
email_graph.add_edge("draft_response", "notify_mr_hugg")
email_graph.add_edge("notify_mr_hugg", END)

compiled_graph = email_graph.compile()


def run_example(email: Dict[str, Any], label: str) -> Dict[str, Any]:
    print(f"\nProcessing {label} email...")
    result = compiled_graph.invoke(
        {
            "email": email,
            "is_spam": None,
            "spam_reason": None,
            "email_category": None,
            "draft_response": None,
            "messages": [],
        }
    )
    print(f"Final state for {label}: {result}")
    return result


def main() -> None:
    legitimate_email = {
        "sender": "john.smith@example.com",
        "subject": "Question about your services",
        "body": (
            "Dear Mr. Hugg, I was referred to you by a colleague and I'm interested "
            "in learning more about your consulting services. Could we schedule a "
            "call next week? Best regards, John Smith"
        ),
    }

    spam_email = {
        "sender": "winner@lottery-intl.com",
        "subject": "YOU HAVE WON $5,000,000!!!",
        "body": (
            "CONGRATULATIONS! You have been selected as the winner of our "
            "international lottery! To claim your $5,000,000 prize, please send us "
            "your bank details and a processing fee of $100."
        ),
    }

    run_example(legitimate_email, "legitimate")
    run_example(spam_email, "spam")


if __name__ == "__main__":
    main()
