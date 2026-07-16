"""
smolagents_alfred.py — Alfred 端到端助手（对齐 HF Agents Course · Unit 3）
Alfred end-to-end agent, aligned with HF Agents Course · Unit 3.

课程出处 / Source: https://huggingface.co/learn/agents-course

这是课程 Unit 3 的 Alfred：把"检索嘉宾信息 (BM25) + 网页搜索 + 天气工具"
组合进一个 CodeAgent，处理'今天北京天气如何、是否适合穿短袖旅游'这类问题。
改动 vs. 课程：
- 模型从 ollama/qwen2.5:7b 换成 HF serverless Inference（InferenceClientModel）
- 数据集路径改为仓库本地 code/data/invitees.jsonl（字段同课程：name/relation/description/email）
pip install "smolagents[toolkit]" datasets langchain-core langchain-community
Run 前在根目录 .env 配置：HUGGINGFACEHUB_API_TOKEN=hf_xxx
"""

import os
from dotenv import load_dotenv
from datasets import load_dataset
from langchain_core.documents import Document
from langchain_community.retrievers import BM25Retriever
from smolagents import CodeAgent, DuckDuckGoSearchTool, InferenceClientModel, Tool, tool

load_dotenv()


def load_guests(path: str = "code/data/invitees.jsonl"):
    """加载嘉宾名单（与课程同字段：name/relation/description/email）。"""
    guest_dataset = load_dataset("json", data_files=path, split="train")
    docs = [
        Document(
            page_content="\n".join(
                [
                    f"Name: {guest['name']}",
                    f"Relation: {guest['relation']}",
                    f"Description: {guest['description']}",
                    f"Email: {guest['email']}",
                ]
            ),
            metadata={"name": guest["name"]},
        )
        for guest in guest_dataset
    ]
    return docs


class GuestInfoRetrieverTool(Tool):
    name = "guest_info_retriever"
    description = (
        "Retrieves detailed information about gala guests based on name or relation."
    )
    inputs = {
        "query": {
            "type": "string",
            "description": "The name or relation of the guest you want information about.",
        }
    }
    output_type = "string"

    def __init__(self, documents):
        super().__init__()
        self.retriever = BM25Retriever.from_documents(documents)

    def forward(self, query: str):
        results = self.retriever.invoke(query)
        if results:
            return "\n\n".join(doc.page_content for doc in results[:3])
        return "No matching guest information found."


def main():
    docs = load_guests()
    guest_info_tool = GuestInfoRetrieverTool(docs)
    search_tool = DuckDuckGoSearchTool()

    @tool
    def get_current_weather_tool(location: str, when: str = "today") -> str:
        """Fetch weather information for a given location and time.

        Args:
            location: A city, region, or country name, for example 'Beijing'.
            when: A natural-language time reference such as 'today', 'tomorrow',
                'this afternoon', or a date like '2026-04-16'.
        """
        try:
            query = f"{location} weather {when}"
            return search_tool.forward(query)
        except Exception as exc:
            return f"Error fetching weather for '{location}' at '{when}': {exc}"

    model = InferenceClientModel(
        model_id="Qwen/Qwen2.5-Coder-32B-Instruct",
        token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
    )
    alfred = CodeAgent(
        tools=[guest_info_tool, search_tool, get_current_weather_tool],
        model=model,
        max_steps=6,
        code_block_tags="markdown",
        instructions=(
            "Use guest_info_retriever for invitee facts before using web_search. "
            "Use get_current_weather_tool for weather questions by passing location and when. "
            "Reply with exactly one Thought and one Python code block per step. "
            "When you have the answer, call final_answer(...) in Python code and stop."
        ),
    )

    task = "今天北京的天气是什么? 是否可以穿短袖去旅游？"
    response = alfred.run(task)
    print("Alfred's Response:")
    print(response)


if __name__ == "__main__":
    main()
