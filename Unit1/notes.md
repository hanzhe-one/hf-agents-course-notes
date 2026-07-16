# Unit 1 · Agent 基础 / Agent Fundamentals

> 对应课程：[HF Agents Course — Unit 1](https://huggingface.co/learn/agents-course)
> 本单元笔记模板，待填充真实学习总结。

## 核心概念 / Core Concepts

- **ReAct（Reasoning + Acting）**：Agent 通过「思考 Thought → 行动 Action → 观察 Observation」循环与工具/环境交互。
- **Tool（工具）**：Agent 可调用的函数，通常有名称、描述、输入模式。
- **Agent Loop**：在停止条件满足前，不断决定下一步动作并执行。

> TODO: 用自己的话复述 ReAct 原理；画一次循环的顺序图。

## 关键代码与运行 / Key Code & Run

- [`code/reAct.py`](code/reAct.py)：用系统提示驱动模型遵循 Thought/Action/Observation 格式，并用 `get_weather` 工具补全 Observation（对齐课程 Dummy Agent 一节，模型用 HF InferenceClient）。
- [`code/tool.py`](code/tool.py)：工具的两种定义方式——`@tool` 装饰器与手写 `Tool` 类（`to_string()` 生成可注入系统提示的描述）。

运行（`reAct.py` 需 `pip install huggingface-hub python-dotenv` 并配置 token）：
```bash
python code/tool.py
python code/reAct.py
```

## 踩坑 / 感悟 / Takeaways

- **ReAct 循环的收敛**：必须让模型在「观察到结果」后输出 `Final Answer`，否则会无限调工具。手写 demo 时这一点最容易漏（见 `code/reAct.py`）。
- **Windows 控制台中文乱码 / 编码坑**：在 Windows 的 cmd/PowerShell 里直接跑含中文的脚本，stdout 是 GBK，中文会变乱码（文件本身 UTF-8 正常，GitHub 渲染没问题）。若要在本地看中文，建议用 UTF-8 终端或把测试串改成英文。
- **工具函数的参数传递**：`math.sqrt()` 这类内置函数不支持关键字参数，`call_tool(tool, x=9)` 会报错；用 lambda 包一层即可统一按名传参（见 `code/tool.py`）。
- **工具描述的重要性**：Agent 是否"用对工具"高度依赖 `@tool` 的 docstring 描述与参数说明，描述写不清模型就容易选错或传错参。

## 参考 / References

- [HF Agents Course Unit 1](https://huggingface.co/learn/agents-course)
- [ReAct 论文 (Yao et al., 2022)](https://arxiv.org/abs/2210.03629)
