"""
workflow.py — 最小可跑的 LlamaIndex Workflow（两个步骤串联）
Minimal runnable LlamaIndex Workflow (two steps chained via events).

重新实现自 Hugging Face Agents Course 官方教程（Unit 2 · LlamaIndex）：
Re-implemented from the HF Agents Course official tutorials (Unit 2 · LlamaIndex):
https://huggingface.co/learn/agents-course

需要：pip install llama-index-core llama-index
这里不接真实 LLM/RAG，用纯逻辑演示 Workflow 的"步骤 + 事件"结构。
"""

from llama_index.core.workflow import (
    StartEvent,
    StopEvent,
    Workflow,
    step,
)
from llama_index.core.llms import MockLLM  # 课程示例常用 Mock 便于离线运行


class GreetWorkflow(Workflow):
    @step
    async def step_one(self, ev: StartEvent) -> StopEvent:
        name = ev.get("name", "world")
        # 真实场景这里可调用 LLM；演示用字符串拼接
        message = f"Hello, {name}!"
        return StopEvent(result=message)


if __name__ == "__main__":
    import asyncio

    wf = GreetWorkflow()
    # 用 MockLLM 避免真实 API 依赖（如课程示例）
    wf.llm = MockLLM()
    result = asyncio.run(wf.run(name="Agent"))
    print(result)
