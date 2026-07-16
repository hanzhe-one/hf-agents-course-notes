# Unit 2 · 三大框架 / Three Agent Frameworks

> 对应课程：[HF Agents Course — Unit 2](https://huggingface.co/learn/agents-course)
> 本单元分别学习三个主流 Agent 框架，下面是横向对比与各自的笔记链接。

## 框架总览 / Framework Overview

| 框架 Framework | 核心抽象 Core Abstraction | 适合场景 Best For |
| --- | --- | --- |
| [LangGraph](LangGraph/notes.md) | 有状态图 StateGraph（节点 + 边 + 状态） | 复杂、可控、需状态流转的多步流程 |
| [LlamaIndex](LlamaIndex/notes.md) | Workflow（步骤） + RAG 数据管道 | 数据/RAG 驱动、检索增强的 Agent |
| [SmolAgents](SmolAgents/notes.md) | CodeAgent（用代码作为行动空间） | 轻量、快速上手、代码即工具调用 |

## 关键对比 / Key Comparison

- **控制粒度**：LangGraph 最强（图显式定义每一步），SmolAgents 最简洁（让 LLM 直接写代码）。
- **工具定义**：三者都支持函数式工具，但装饰器/约定不同（`@tool` vs Pydantic vs function tool）。
- **状态管理**：LangGraph 用 `State` 显式传递；SmolAgents 内部维护记忆；LlamaIndex 用 `Context`。

- 上手成本：SmolAgents 最轻（几行出 Agent），LangGraph 要理解图/状态/边，LlamaIndex 概念最多（Index/Retriever/Workflow/Context）。
- 跨框架通用坑：①工具描述（docstring）决定模型选不选得对；②`pip install` 的包名和导入名常不一致（如 `llama-index` vs `llama_index`）；③本地课程示例多用规则/离线，跑通后再接真实 LLM。

## 参考 / References

- [HF Agents Course Unit 2](https://huggingface.co/learn/agents-course)
- [LangGraph 文档](https://langchain-ai.github.io/langgraph/)
- [LlamaIndex 文档](https://docs.llamaindex.ai/)
- [SmolAgents 文档](https://huggingface.co/docs/smolagents)
