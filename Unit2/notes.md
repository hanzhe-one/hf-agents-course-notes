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

> TODO: 用一个相同任务（如"查天气并写邮件"）分别用三框架实现，对比代码量与可控性。

## 参考 / References

- [HF Agents Course Unit 2](https://huggingface.co/learn/agents-course)
- [LangGraph 文档](https://langchain-ai.github.io/langgraph/)
- [LlamaIndex 文档](https://docs.llamaindex.ai/)
- [SmolAgents 文档](https://huggingface.co/docs/smolagents)
