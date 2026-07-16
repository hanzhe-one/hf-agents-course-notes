"""
smolagents_alfred.py — Alfred 风格助手最小示例（端到端应用）
Minimal Alfred-style assistant example (end-to-end applied agent).

重新实现自 Hugging Face Agents Course 官方教程（Unit 3）：
Re-implemented from the HF Agents Course official tutorials (Unit 3):
https://huggingface.co/learn/agents-course

这是一个"个人助理"最小骨架：读取受邀者名单（data/invitees.jsonl），
根据名单用工具发送邀请。为便于离线演示，发送动作是占位打印。
需要：pip install smolagents；真实运行需在 .env 配置 HUGGINGFACEHUB_API_TOKEN。
"""

import os
import json
from dotenv import load_dotenv
from smolagents import CodeAgent, tool, InferenceClientModel

load_dotenv()


def load_invitees(path: str = "code/data/invitees.jsonl") -> list[dict]:
    """从 jsonl 读取受邀者名单。"""
    invitees = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                invitees.append(json.loads(line))
    return invitees


@tool
def send_invite(name: str, email: str) -> str:
    """向某人发送活动邀请。

    Args:
        name: 受邀者姓名
        email: 受邀者邮箱
    """
    # 占位实现：真实场景调用邮件 API
    print(f"[send] 已向 {name} <{email}> 发送邀请")
    return f"invited:{name}"


def main():
    invitees = load_invitees()
    print(f"加载到 {len(invitees)} 位受邀者")

    model = InferenceClientModel(token=os.getenv("HUGGINGFACEHUB_API_TOKEN"))
    agent = CodeAgent(tools=[send_invite], model=model)
    agent.run(
        "请给名单上的每一位受邀者发送邀请，并告诉我总共邀请了几人。"
    )


if __name__ == "__main__":
    main()
