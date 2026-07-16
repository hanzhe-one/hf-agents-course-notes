"""
reAct.py — ReAct 提示驱动的 Agent（对齐 HF Agents Course · Unit 1）
ReAct prompting demo, aligned with HF Agents Course · Unit 1.

课程出处 / Source: https://huggingface.co/learn/agents-course

改动说明 / Change vs. course:
- 课程 Dummy Agent 一节用 serverless Inference API 驱动一个遵循
  Thought/Action/Observation 格式的系统提示。这里保持同样的思路，
  用 huggingface_hub.InferenceClient（需要 HF token）替代本地 ollama。
- Run 前在根目录 .env 配置：HUGGINGFACEHUB_API_TOKEN=hf_xxx
- pip install huggingface-hub python-dotenv
"""

import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

# 与课程一致：一段驱动 ReAct 格式的系统提示
SYSTEM_PROMPT = """你是一个可以调用外部工具的聪明助手。
为了解决用户的问题，你可以使用以下工具：
- get_weather: 获取指定城市当前的天气情况。输入应为城市名，比如 "London"。

你必须严格遵循以下格式进行思考和输出：
Thought: 你需要思考接下来做什么
Action: 决定使用的工具名称（必须是 get_weather）
Action Input: 传给该工具的具体参数
Observation: 工具返回的客观结果
...（以上步骤可循环多次）
Thought: 我现在已经知道最终答案
Final Answer: 对用户问题的最终回答
"""


def get_weather(location: str) -> str:
    """模拟一个调用外部天气 API 的工具。"""
    if "London" in location or "伦敦" in location:
        return "12°C, 阴天，有阵雨 (Rainy)"
    return "25°C, 晴朗"


def main():
    client = InferenceClient(
        model="Qwen/Qwen2.5-Coder-32B-Instruct",
        token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
    )

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "What's the weather in London?"},
    ]

    # 第一次调用：让模型产生 Thought/Action（在 Observation 处停止）
    completion = client.chat_completion(messages, max_tokens=500, stop=["Observation:"])
    output = completion.choices[0].message.content
    print(output)

    # 把工具执行结果作为 Observation 拼回，再让模型给出 Final Answer
    observation = get_weather("London")
    messages.append({"role": "assistant", "content": output})
    messages.append({"role": "user", "content": f"Observation: {observation}"})

    completion = client.chat_completion(messages, max_tokens=500)
    print("Observation:", observation)
    print(completion.choices[0].message.content)


if __name__ == "__main__":
    main()
