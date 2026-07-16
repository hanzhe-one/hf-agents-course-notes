"""
firstAgent.py — 第一个 CodeAgent（对齐 HF Agents Course · Unit 2 · smolagents）
First CodeAgent, aligned with HF Agents Course · Unit 2 · smolagents.

课程出处 / Source: https://huggingface.co/learn/agents-course

课程的 Alfred 派对示例：用一个搜索工具让 CodeAgent 规划派对。
模型用 HF serverless Inference（InferenceClientModel），无需本地 ollama。
pip install "smolagents[toolkit]"
Run 前在根目录 .env 配置：HUGGINGFACEHUB_API_TOKEN=hf_xxx
"""

import os
from dotenv import load_dotenv
from smolagents import CodeAgent, DuckDuckGoSearchTool, InferenceClientModel

load_dotenv()


def main():
    model = InferenceClientModel(
        model_id="Qwen/Qwen2.5-Coder-32B-Instruct",
        token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
    )
    agent = CodeAgent(tools=[DuckDuckGoSearchTool()], model=model)
    agent.run(
        "Search for the best music recommendations for a party at the Wayne's mansion."
    )


if __name__ == "__main__":
    main()
