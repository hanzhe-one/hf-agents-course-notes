# Unit 2 · SmolAgents / 轻量级 CodeAgent

> 对应课程：[HF Agents Course — Unit 2 · SmolAgents](https://huggingface.co/learn/agents-course)

## 核心概念 / Core Concepts

- **CodeAgent**：以"生成的 Python 代码"作为行动空间——比 JSON 工具调用更灵活，能直接写 `pandas`/循环等。
- **@tool 装饰器**：把普通函数变成带名称/描述的工具（docstring 即工具描述，参数注解即 schema）。
- **Tool 子类**：更复杂的工具用 `class Tool` 声明 `name / description / inputs / output_type` 并实现 `forward`。
- **工具组合**：一个 Agent 可挂多个工具（搜索、网页访问、自定义计算）协作完成任务。

## 关键代码与运行 / Key Code & Run

- [`code/firstAgent.py`](code/firstAgent.py)：第一个 CodeAgent（搜索工具）。
- [`code/multiAgent.py`](code/multiAgent.py)：多工具 CodeAgent（`@tool` 自定义货运时间计算 + 搜索 + 访问网页，输出 pandas DataFrame）。
- [`code/toolClass.py`](code/toolClass.py)：用 `Tool` 子类定义派对主题工具。

运行（需 `pip install "smolagents[toolkit]"` 并在 `.env` 配置 `HUGGINGFACEHUB_API_TOKEN`）：
```bash
python code/firstAgent.py
python code/multiAgent.py
python code/toolClass.py
```

## 踩坑 / 感悟 / Takeaways

> TODO: 记录 CodeAgent 相比 JSON-action Agent 的优势；`additional_authorized_imports` 的作用（为何 multiAgent 要显式开 pandas）；代码执行安全；token 配置。

## 参考 / References

- [SmolAgents 官方文档](https://huggingface.co/docs/smolagents)
