"""
toolClass.py — 用 Tool 子类自定义工具（对齐 HF Agents Course · Unit 2 · smolagents）
Custom tool via Tool subclass, aligned with HF Agents Course · Unit 2 · smolagents.

课程出处 / Source: https://huggingface.co/learn/agents-course

课程示例：Alfred 需要一个能按类别给出超级英雄派对主题的工具。
除了 @tool 装饰器，smolagents 还支持继承 Tool 类来定义更复杂的工具
（声明 name / description / inputs / output_type，并实现 forward）。
pip install "smolagents[toolkit]"
Run 前在根目录 .env 配置：HUGGINGFACEHUB_API_TOKEN=hf_xxx
"""

import os
from dotenv import load_dotenv
from smolagents import CodeAgent, InferenceClientModel, Tool

load_dotenv()


class SuperheroPartyThemeTool(Tool):
    name = "superhero_party_theme_generator"
    description = (
        "This tool suggests creative superhero-themed party ideas based on a "
        "category. It returns a unique party theme idea."
    )
    inputs = {
        "category": {
            "type": "string",
            "description": (
                "The type of superhero party (e.g., 'classic heroes', "
                "'villain masquerade', 'futuristic Gotham')."
            ),
        }
    }
    output_type = "string"

    def forward(self, category: str):
        themes = {
            "classic heroes": "Justice League Gala: Guests come dressed as their favorite DC heroes with themed cocktails like 'The Kryptonite Punch'.",
            "villain masquerade": "Gotham Rogues' Ball: A mysterious masquerade where guests dress as classic Batman villains.",
            "futuristic Gotham": "Neo-Gotham Night: A cyberpunk-style party inspired by Batman Beyond, with neon decorations and futuristic gadgets.",
        }
        return themes.get(
            category.lower(),
            "Themed party idea not found. Try 'classic heroes', "
            "'villain masquerade', or 'futuristic Gotham'.",
        )


def main():
    party_theme_tool = SuperheroPartyThemeTool()
    model = InferenceClientModel(
        model_id="Qwen/Qwen2.5-Coder-32B-Instruct",
        token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
    )
    agent = CodeAgent(tools=[party_theme_tool], model=model)
    result = agent.run(
        "What would be a good superhero party idea for a 'villain masquerade' theme?"
    )
    print(result)


if __name__ == "__main__":
    main()
