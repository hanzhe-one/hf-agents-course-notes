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

> TODO: 记录 Workflow 与 LangGraph 图的区别；RAG 检索质量对结果的影响；切分策略。

## 参考 / References

- [LlamaIndex 官方文档](https://docs.llamaindex.ai/)
