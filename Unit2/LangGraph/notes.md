# Unit 2 · LangGraph / 基于图的有状态 Agent

> 对应课程：[HF Agents Course — Unit 2 · LangGraph](https://huggingface.co/learn/agents-course)

## 核心概念 / Core Concepts

- **StateGraph**：用图定义 Agent 流程，节点是函数，边是转移条件。
- **State（TypedDict）**：在节点间传递的共享状态（如 `EmailState` 里的 `is_spam` / `draft_response`）。
- **节点 Node / 边 Edge**：节点返回要更新的状态字段；边决定走向，条件边用 `add_conditional_edges` 按返回值分流。
- **本地规则 vs LLM**：课程示例用本地关键词规则做分类/草拟，不依赖 LLM，因此开箱即跑。

## 关键代码与运行 / Key Code & Run

- [`code/first_langgraph.py`](code/first_langgraph.py)：Alfred 邮件处理图——`read_email → classify_email →（条件边）spam/legitimate → draft_response → notify_mr_hugg`，完整演示 StateGraph + 条件边 + 共享状态。

运行（需 `pip install langgraph`，**无需 token**，分类用本地规则）：
```bash
python code/first_langgraph.py
```

## 踩坑 / 感悟 / Takeaways

> TODO: 记录你对"显式图 vs 隐式循环"的理解；条件边返回值如何映射到目标节点；状态字段如何跨节点累积；与 SmolAgents 的 Agent loop 对比。

## 参考 / References

- [LangGraph 官方文档](https://langchain-ai.github.io/langgraph/)
