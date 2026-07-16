# Unit 3 · 综合应用 / Applied Agents

> 对应课程：[HF Agents Course — Unit 3](https://huggingface.co/learn/agents-course)
> 本单元把前两个单元的能力组合成端到端 Agent 应用（如课程中的 Alfred 助手：查邮件、看日历、发消息等）。

## 核心概念 / Core Concepts

- **端到端应用**：把工具（邮件/日历/搜索）+ 框架（SmolAgents 等）+ 提示编排成可用产品。
- **多工具调度**：Agent 在一次任务中组合调用多个工具。
- **安全与权限**：执行动作（发邮件/改日程）前的确认与边界控制。

## 关键代码与运行 / Key Code & Run

- [`code/smolagents_alfred.py`](code/smolagents_alfred.py)：基于 SmolAgents 的 Alfred 风格助手最小示例（含示例数据）。
- 示例数据：[`code/data/invitees.jsonl`](code/data/invitees.jsonl)

运行（需 `pip install smolagents` 并配置 token）：
```bash
python code/smolagents_alfred.py
```

## 踩坑 / 感悟 / Takeaways

> TODO: 记录端到端调试的难点；工具描述如何决定 Agent 是否用对工具；失败重试。

## 参考 / References

- [HF Agents Course Unit 3](https://huggingface.co/learn/agents-course)
