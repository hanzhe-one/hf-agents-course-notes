"""
firstAgent.py — 最小可跑的 SmolAgents CodeAgent + @tool
Minimal runnable SmolAgents CodeAgent with a @tool.

重新实现自 Hugging Face Agents Course 官方教程（Unit 2 · SmolAgents）：
Re-implemented from the HF Agents Course official tutorials (Unit 2 · SmolAgents):
https://huggingface.co/learn/agents-course

需要：pip install smolagents
运行前在根目录 .env 配置：HUGGINGFACEHUB_API_TOKEN=hf_xxx
（也可设置 model_id 指向你有权限的模型）
"""

import os
from dotenv import load_dotenv
from smolagents import CodeAgent, tool, InferenceClientModel

load_dotenv()  # 读取 .env 中的 HUGGINGFACEHUB_API_TOKEN


@tool
def get_weather(city: str) -> str:
    """返回指定城市的天气。

    Args:
        city: 城市名称，如 "北京"
    """
    # 占位实现；真实场景可调天气 API
    return f"晴，{city} 今天 25°C"


def main():
    model = InferenceClientModel(token=os.getenv("HUGGINGFACEHUB_API_TOKEN"))
    agent = CodeAgent(tools=[get_weather], model=model)
    answer = agent.run("北京天气怎么样？")
    print("Agent answer:", answer)


if __name__ == "__main__":
    main()
