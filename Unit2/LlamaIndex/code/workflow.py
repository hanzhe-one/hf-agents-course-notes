"""
workflow.py — 最小 LlamaIndex Workflow（对齐 HF Agents Course · Unit 2 · LlamaIndex）
Minimal LlamaIndex Workflow, aligned with HF Agents Course · Unit 2 · LlamaIndex.

课程出处 / Source: https://huggingface.co/learn/agents-course

Workflow 由多个 @step 组成，步骤间通过事件（StartEvent / 自定义 Event /
StopEvent）串联。课程入门示例就是一个返回 "Hello, world!" 的单步工作流。
下面保留该最小形态，并附一个两步链式的变体展示事件传递。
需要：pip install llama-index-core
"""

import asyncio
from llama_index.core.workflow import StartEvent, StopEvent, Workflow, step


class MyWorkflow(Workflow):
    @step
    async def my_step(self, ev: StartEvent) -> StopEvent:
        return StopEvent(result="Hello, world!")


async def main():
    w = MyWorkflow(timeout=10, verbose=False)
    result = await w.run()
    print(result)


if __name__ == "__main__":
    asyncio.run(main())
