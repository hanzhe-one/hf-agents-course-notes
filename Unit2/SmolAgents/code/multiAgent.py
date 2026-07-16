"""
multiAgent.py — 最小可跑的 SmolAgents ManagerAgent（多智能体协作）
Minimal runnable SmolAgents ManagerAgent orchestrating specialist sub-agents.

重新实现自 Hugging Face Agents Course 官方教程（Unit 2 · SmolAgents）：
Re-implemented from the HF Agents Course official tutorials (Unit 2 · SmolAgents):
https://huggingface.co/learn/agents-course

需要：pip install smolagents
运行前在根目录 .env 配置：HUGGINGFACEHUB_API_TOKEN=hf_xxx
"""

import os
from dotenv import load_dotenv
from smolagents import CodeAgent, ManagerAgent, InferenceClientModel

load_dotenv()


def build_model():
    return InferenceClientModel(token=os.getenv("HUGGINGFACEHUB_API_TOKEN"))


def main():
    # 两个专长子 Agent
    weather_agent = CodeAgent(
        tools=[], model=build_model(), name="weather_agent",
        description="擅长回答天气相关问题",
    )
    calendar_agent = CodeAgent(
        tools=[], model=build_model(), name="calendar_agent",
        description="擅长回答日程/日历相关问题",
    )

    # 管理 Agent 负责把任务分派给子 Agent
    manager = ManagerAgent(
        tools=[], model=build_model(),
        managed_agents=[weather_agent, calendar_agent],
    )

    answer = manager.run("帮我查一下明天天气，并看看我的日程是否为空。")
    print("Manager answer:", answer)


if __name__ == "__main__":
    main()
