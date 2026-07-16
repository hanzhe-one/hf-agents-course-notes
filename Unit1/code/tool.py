"""
tool.py — 用函数定义"工具"的最小示例
Minimal example of defining tools as functions.

重新实现自 Hugging Face Agents Course 官方教程（Unit 1）：
Re-implemented from the HF Agents Course official tutorials (Unit 1):
https://huggingface.co/learn/agents-course

课程中常用 @tool 装饰器（smolagents）或 Pydantic/函数 schema（LangChain）
来描述工具的"名称 + 描述 + 参数"。这里用手写 schema 演示核心思想，
不依赖任何框架，便于理解工具是如何被 Agent 发现和调用的。
"""

import math


def make_tool(name, description, func, arg_name):
    """把普通函数包装成带元信息的 tool 字典。

    Wrap a plain function with metadata so an agent can discover & call it.
    """
    return {
        "name": name,
        "description": description,
        "arg_name": arg_name,
        "func": func,
    }


# 定义两个工具（用 lambda 包一层，统一支持按名传参）
TOOLS = [
    make_tool(
        "square_root",
        "返回一个数的平方根",
        lambda x: math.sqrt(x),
        "x",
    ),
    make_tool(
        "add",
        "返回两个数之和",
        lambda a, b: a + b,
        "a",  # 简化：仅演示单参数入口
    ),
]


def call_tool(tool, **kwargs):
    return tool["func"](**kwargs)


if __name__ == "__main__":
    for t in TOOLS:
        print(f"- {t['name']}: {t['description']}")
    print("\nsquare_root(9) =", call_tool(TOOLS[0], x=9))
    print("add(2, 3)      =", call_tool(TOOLS[1], a=2, b=3))
