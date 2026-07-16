"""
tool.py — 工具的两种定义方式（对齐 HF Agents Course · Unit 1）
Two ways to define a Tool, aligned with HF Agents Course · Unit 1.

课程出处 / Source: https://huggingface.co/learn/agents-course

包含两部分（与课程一致）：
1) smolagents 的 @tool 装饰器：最简单的工具定义。
2) 手写 Tool 类：理解一个工具的"名称/描述/参数/输出"元信息如何拼成
   可注入到系统提示里的字符串（course 中的 Tool 抽象）。
pip install smolagents
"""

from smolagents import tool


@tool
def calculator(a: int, b: int) -> int:
    """两数相乘的工具。

    Args:
        a: 第一个整数
        b: 第二个整数
    """
    return a * b


class Tool:
    """表示一段可复用代码（工具）。

    Attributes:
        name: 工具名称
        description: 工具功能描述
        func: 被包装的可调用对象
        arguments: 参数列表 [(name, type), ...]
        outputs: 返回类型
    """

    def __init__(self, name, description, func, arguments, outputs):
        self.name = name
        self.description = description
        self.func = func
        self.arguments = arguments
        self.outputs = outputs

    def to_string(self) -> str:
        """返回工具的字符串描述（可注入系统提示）。"""
        args_str = ", ".join(
            f"{arg_name}: {arg_type}" for arg_name, arg_type in self.arguments
        )
        return (
            f"Tool Name: {self.name},"
            f" Description: {self.description},"
            f" Arguments: {args_str},"
            f" Outputs: {self.outputs}"
        )

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)


calculator_tool = Tool(
    "calculator",
    "Multiply two integers.",
    calculator,
    [("a", "int"), ("b", "int")],
    "int",
)


if __name__ == "__main__":
    print(calculator_tool.to_string())
    print("calculator(6, 7) =", calculator_tool(6, 7))
