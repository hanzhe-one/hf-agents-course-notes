# Unit 2 · LangGraph / 基于图的有状态 Agent

> 对应课程：[HF Agents Course — Unit 2 · LangGraph](https://huggingface.co/learn/agents-course)

## 核心概念 / Core Concepts

- **StateGraph**：用图定义 Agent 流程，节点是函数，边是转移条件。
- **State**：在节点间传递的共享状态（通常用 TypedDict / Pydantic）。
- **节点 Node / 边 Edge**：节点执行逻辑，边决定下一步走向（含条件边 `add_conditional_edges`）。

## 关键代码与运行 / Key Code & Run

- [`code/first_langgraph.py`](code/first_langgraph.py)：最小 StateGraph（一个状态 + 两个节点 + 条件边）。

运行（需 `pip install langgraph langchain langchain-openai` 并配置 API key）：
```bash
python code/first_langgraph.py
```

## 踩坑 / 感悟 / Takeaways

> TODO: 记录你对"显式图 vs 隐式循环"的理解；条件边的写法；状态如何累积。

## 参考 / References

- [LangGraph 官方文档](https://langchain-ai.github.io/langgraph/)
