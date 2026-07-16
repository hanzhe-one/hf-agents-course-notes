"""
reAct.py — 最小可跑的 ReAct（Reasoning + Acting）循环演示
Minimal hand-written ReAct loop demo.

重新实现自 Hugging Face Agents Course 官方教程（Unit 1）：
Re-implemented from the HF Agents Course official tutorials (Unit 1):
https://huggingface.co/learn/agents-course

说明 / Notes:
- 为演示清晰，这里用一个"假模型" mock_model 来代替真实 LLM 调用，
  避免依赖 API token。把 mock_model 换成真实 LLM 调用即可对接课程示例。
- A fake model stands in for a real LLM so this runs with no API token.
  Swap `mock_model` for a real LLM call to match the course example.
"""

# 一个示例"工具"：根据城市返回天气（占位实现）
TOOLS = {
    "get_weather": lambda city: f"晴，{city} 今天 25°C",
}


def mock_model(prompt: str) -> str:
    """模拟 LLM：根据提示返回 Thought/Action 文本。

    A stand-in for an LLM that returns Thought/Action text.
    In the real course this is an actual chat-completion call.

    注：这里用 ASCII 触发词 "weather" 而非中文，避免 Windows 控制台
    GBK 编码导致的中文比较失败（真实课程里模型输出是结构化的，
    不会有此问题）。
    演示逻辑：首轮看到 weather 触发词 -> 返回 Action；当 prompt 中
    已包含 "Observation:"（说明已经过一轮工具调用）-> 返回 Final Answer，
    从而完整演示「思考->行动->观察->结束」闭环。
    """
    if "Observation:" in prompt:
        return "Thought: I have the weather now.\nFinal Answer: It is sunny, 25C in Beijing."
    if "weather" in prompt.lower():
        return 'Thought: I need the weather.\nAction: get_weather["Beijing"]'
    return "Thought: I have enough info.\nFinal Answer: Done."


def parse_action(text: str):
    """从模型输出中解析 Action: tool["arg"]。"""
    for line in text.splitlines():
        if line.strip().startswith("Action:"):
            body = line.split("Action:", 1)[1].strip()
            name, arg = body.split("[", 1)
            arg = arg.rstrip("]").strip('"')
            return name.strip(), arg
    return None, None


def react_loop(question: str, max_steps: int = 5):
    """ReAct 主循环：Thought -> Action -> Observation，直到 Final Answer。"""
    print(f"Question: {question}\n")
    prompt = question
    for step in range(1, max_steps + 1):
        out = mock_model(prompt)
        print(f"--- Step {step} ---\n{out}\n")

        if "Final Answer:" in out:
            return out.split("Final Answer:", 1)[1].strip()

        name, arg = parse_action(out)
        if name in TOOLS:
            obs = TOOLS[name](arg)
            print(f"Observation: {obs}\n")
            prompt = f"{out}\nObservation: {obs}\n"
        else:
            print("Observation: 未找到对应工具。\n")
    return "（达到最大步数，未得出最终答案）"


if __name__ == "__main__":
    answer = react_loop("What is the weather today?")
    print(f"Answer: {answer}")
