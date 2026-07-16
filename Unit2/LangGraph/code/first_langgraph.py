"""
first_langgraph.py — 最小可跑的 LangGraph StateGraph
Minimal runnable LangGraph StateGraph.

重新实现自 Hugging Face Agents Course 官方教程（Unit 2 · LangGraph）：
Re-implemented from the HF Agents Course official tutorials (Unit 2 · LangGraph):
https://huggingface.co/learn/agents-course

为便于直接运行，节点逻辑用纯 Python 模拟（不真正调用 LLM）。
把 node 内的逻辑替换成真实 LLM 调用即可对接课程示例。
需要：pip install langgraph
"""

from typing import TypedDict
from langgraph.graph import StateGraph, END


class State(TypedDict):
    count: int
    text: str


def node_a(state: State) -> State:
    """第一个节点：累加计数并追加文本。"""
    print(f"[node_a] in: {state}")
    return {"count": state["count"] + 1, "text": state["text"] + "A"}


def node_b(state: State) -> State:
    """第二个节点：再累加一次。"""
    print(f"[node_b] in: {state}")
    return {"count": state["count"] + 1, "text": state["text"] + "B"}


def should_continue(state: State) -> str:
    """条件边：count >= 3 则结束，否则回到 node_a。"""
    return "end" if state["count"] >= 3 else "continue"


def build_graph():
    builder = StateGraph(State)
    builder.add_node("node_a", node_a)
    builder.add_node("node_b", node_b)
    builder.set_entry_point("node_a")
    # node_a -> node_b
    builder.add_edge("node_a", "node_b")
    # node_b -> (条件) -> node_a 或 END
    builder.add_conditional_edges(
        "node_b",
        should_continue,
        {"continue": "node_a", "end": END},
    )
    return builder.compile()


if __name__ == "__main__":
    graph = build_graph()
    result = graph.invoke({"count": 0, "text": ""})
    print("\nFinal state:", result)
