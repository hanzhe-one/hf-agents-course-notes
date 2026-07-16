# Unit 3 · 综合应用 / Applied Agents

> 对应课程：[HF Agents Course — Unit 3](https://huggingface.co/learn/agents-course)
> 本单元把前两个单元的能力组合成端到端 Agent 应用（如课程中的 Alfred 助手：查邮件、看日历、发消息等）。

## 核心概念 / Core Concepts

- **端到端应用**：把工具（邮件/日历/搜索）+ 框架（SmolAgents 等）+ 提示编排成可用产品。
- **多工具调度**：Agent 在一次任务中组合调用多个工具。
- **安全与权限**：执行动作（发邮件/改日程）前的确认与边界控制。

## 关键代码与运行 / Key Code & Run

- [`code/smolagents_alfred.py`](code/smolagents_alfred.py)：端到端 Alfred 助手——把 **BM25 嘉宾信息检索**（`GuestInfoRetrieverTool`）、**网页搜索**（`DuckDuckGoSearchTool`）、**天气工具**（`@tool` 包装搜索）组合进一个 `CodeAgent`，并用 `instructions` 约束输出格式。
- 示例数据：[`code/data/invitees.jsonl`](code/data/invitees.jsonl)（课程字段：name/relation/description/email）。

运行（需 `pip install "smolagents[toolkit]" datasets langchain-core langchain-community` 并配置 token）：
```bash
python code/smolagents_alfred.py
```

## 踩坑 / 感悟 / Takeaways

- **`load_dataset("json", data_files=...)` 的路径是相对"当前工作目录"的**：在仓库根目录跑 `python Unit3/code/smolagents_alfred.py` 时，cwd 是根目录，所以代码里写 `code/data/invitees.jsonl`。从别处跑就会找不到文件——或用绝对路径/动态 `__file__` 路径更稳。
- **BM25 是关键词检索，不是语义检索**：它按词面匹配，`query="best friend"` 能命中 relation 字段，但中文/同义词召回弱。课程示例数据偏英文，中文检索效果会打折（这正是 RAG 里"检索器选型"的坑）。
- **`@tool` 嵌套定义在 `main()` 里**：`get_current_weather_tool` 写在 `main` 内是因为它要复用 `search_tool` 实例；注意它必须和 `guest_info_tool`、`search_tool` 一起在 `main` 里传给 `CodeAgent`，不能在模块顶层单独跑。
- **`instructions` 约束输出格式**：明确告诉模型"先调 guest_info_retriever 再搜索""每步一个 Thought 一个代码块""用 `final_answer()` 收尾"，能显著减少模型乱写、跑不出结果的情况。
- **`DuckDuckGoSearchTool` 有限流**：跑多次容易被限流返回空，调试时可以先把天气/检索工具单独验证，再接搜索。
- **端到端调试难点**：问题往往不在"模型"，而在"工具描述/数据/路径"——先单独验证每个工具（直接 `tool.forward(...)`），再交给 Agent 编排，定位快得多。

## 参考 / References

- [HF Agents Course Unit 3](https://huggingface.co/learn/agents-course)
