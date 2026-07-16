# Unit 2 · LlamaIndex / 数据、RAG 与 Workflow

> 对应课程：[HF Agents Course — Unit 2 · LlamaIndex](https://huggingface.co/learn/agents-course)

## 核心概念 / Core Concepts

- **Workflow**：由多个 `Step` 组成的有向流程，步骤间通过 `Context` 与返回值传递数据。
- **RAG 管道**：`VectorStoreIndex` 加载文档 → 切分 → 嵌入 → 检索 → 合成答案。
- **Event**：Workflow 步骤通过事件（StartEvent / 自定义 Event）触发与通信。

## 关键代码与运行 / Key Code & Run

- [`code/workflow.py`](code/workflow.py)：最小 Workflow（两个步骤串联 + 事件）。

运行（需 `pip install llama-index`）：
```bash
python code/workflow.py
```

## 踩坑 / 感悟 / Takeaways

- **包名坑：`llama-index` vs `llama-index-core`**：pip 装 `llama-index`（完整版）和 `llama-index-core`（仅核心）都能跑 Workflow，但完整版会拉一大堆依赖；课程里 Workflow 只用 core 就够。装错版本容易遇到 Pydantic v1/v2 兼容性告警。
- **Workflow 必须 `asyncio.run`**：`@step` 是 `async def`，入口 `w.run()` 也是协程，脚本要用 `asyncio.run(main())` 包起来，不能直接 `main()`。
- **步骤靠"事件"串联，不是靠 return 顺序**：第一个 `@step` 返回 `StopEvent` 就结束；要串多步得自定义中间 Event（如 `class MyEvent(StartEvent)`），否则图不知道下一步触发谁。
- **vs LangGraph**：LlamaIndex Workflow 偏向"数据/检索驱动的步骤流"，事件即数据；LangGraph 是"显式状态图 + 条件边"，更适合带分支/循环的控制流。课程 Unit3 的 Alfred 检索就用到了这里的 `Document`/`BM25Retriever`。
- **RAG 检索质量决定上限**：`VectorStoreIndex` 的切分粒度、embedding 模型直接影响回答质量；检索不到，模型再强也答不对。

## 参考 / References

- [LlamaIndex 官方文档](https://docs.llamaindex.ai/)
