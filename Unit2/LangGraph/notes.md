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

- **`START`/`END` 要从 `langgraph.graph` 导入**：课程里 `add_edge(START, ...)` 和 `add_edge(..., END)` 用的是图自带的起止点，不是字符串，别自己定义 `"start"`/`"end"`。
- **状态字段必须显式初始化**：`compiled_graph.invoke({...})` 时 `EmailState` 里的每个字段（含 `messages: []`、`is_spam: None`）都要给初值，否则节点里 `state.get("messages", [])` 拿不到、累积失败。
- **条件边返回值 = 目标节点名**：`route_email` 返回 `"spam"`/`"legitimate"`，必须和 `add_conditional_edges(..., {"spam": "handle_spam", "legitimate": "draft_response"})` 的 key 一一对应，拼错就报"找不到节点"。
- **节点返回的是"要更新的状态字段"，不是整个 state**：节点函数返回 `{"draft_response": ...}` 即可，LangGraph 自动合并；返回整个 dict 反而容易覆盖别的字段。
- **本示例用本地规则、不调 LLM**：所以 `first_langgraph.py` 无需 API key 就能跑——容易让人误以为也要配模型，其实它纯靠关键词分类。
- **vs SmolAgents 的 loop**：LangGraph 是"图显式定义每一步 + 状态显式传递"，SmolAgents 是"LLM 自己决定下一步写什么代码"。前者可控、可观测，后者灵活但黑盒。

## 参考 / References

- [LangGraph 官方文档](https://langchain-ai.github.io/langgraph/)
