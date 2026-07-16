# Unit 2 · SmolAgents / 轻量级 CodeAgent

> 对应课程：[HF Agents Course — Unit 2 · SmolAgents](https://huggingface.co/learn/agents-course)

## 核心概念 / Core Concepts

- **CodeAgent**：以"生成的 Python 代码"作为行动空间——比 JSON 工具调用更灵活。
- **@tool**：用装饰器把普通函数变成带名称/描述的工具。
- **ManagerAgent（多智能体）**：一个管理 Agent 调度多个专长子 Agent 协作。

## 关键代码与运行 / Key Code & Run

- [`code/firstAgent.py`](code/firstAgent.py)：CodeAgent + `@tool` 最小示例。
- [`code/multiAgent.py`](code/multiAgent.py)：ManagerAgent 调度两个子 Agent。

运行（需 `pip install smolagents` 并在 `.env` 配置 `HUGGINGFACEHUB_API_TOKEN`）：
```bash
python code/firstAgent.py
python code/multiAgent.py
```

## 踩坑 / 感悟 / Takeaways

> TODO: 记录 CodeAgent 相比 JSON-action Agent 的优势；代码执行安全；token 配置。

## 参考 / References

- [SmolAgents 官方文档](https://huggingface.co/docs/smolagents)
