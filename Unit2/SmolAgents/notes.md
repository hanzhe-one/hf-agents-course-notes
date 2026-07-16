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

- **`@tool` 的 docstring + 类型注解就是 schema**：工具名来自函数名，描述来自 docstring，参数类型来自注解。描述写不清，模型就容易选错工具或传错参——比框架本身更容易出错的是"工具描述"。
- **`additional_authorized_imports` 不开就报错**：像 `multiAgent.py` 要让模型输出 pandas DataFrame，必须显式 `additional_authorized_imports=["pandas"]`。SmolAgents 默认只允许安全的内置，未授权的 import 会被执行器拒绝。
- **`CodeAgent` 比 JSON-action `ToolCallingAgent` 更灵活**：CodeAgent 让模型直接写 Python（能写循环、调 pandas），ToolCallingAgent 只输出工具调用的 JSON。课程默认用 CodeAgent。
- **`InferenceClientModel` 的 token**：从环境变量 `HUGGINGFACEHUB_API_TOKEN` 读，或显式传 `token=`。serverless 模型有速率限制，跑长任务容易触限，需要控制 `max_steps`。
- **代码执行安全**：CodeAgent 会真跑模型生成的代码，`additional_authorized_imports` 是在"能力"和"安全"之间权衡的开关，别为了省事开成 `*`。
- **`code_block_tags="markdown"`**：让模型用 ` ```python ` 包裹代码块，解析更稳（Unit3 alfred 用到）。

## 参考 / References

- [SmolAgents 官方文档](https://huggingface.co/docs/smolagents)
