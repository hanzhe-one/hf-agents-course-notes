# Hugging Face Agents 课程笔记 · 学习仓库

> HF Agents Course — Notes & Minimal Examples

这是我学习 [Hugging Face Agents Course](https://huggingface.co/learn/agents-course) 全部四个单元（Unit 1–4）时整理的笔记与示例代码集合。仓库用于**个人总结与分享展示**。

This repo collects my notes and runnable examples from the four units (Unit 1–4) of the [Hugging Face Agents Course](https://huggingface.co/learn/agents-course). It serves as both a personal study log and a shareable showcase.

---

## 📚 单元导航 / Unit Navigation

| 单元 Unit | 主题 Topic | 笔记 Notes | 要点 Highlights |
| --- | --- | --- | --- |
| **Unit 1** | Agent 基础 / Agent Fundamentals | [Unit1/notes.md](Unit1/notes.md) | ReAct 提示、工具定义（`@tool` 与 `Tool` 类） |
| **Unit 2** | 三大框架 / Three Frameworks | [Unit2/notes.md](Unit2/notes.md) | LangGraph · LlamaIndex · SmolAgents |
| **Unit 3** | 综合应用 / Applied Agents | [Unit3/notes.md](Unit3/notes.md) | 端到端 Alfred 助手（检索+搜索+天气） |
| Unit 4 | 期末项目 / Final Project | [Unit4/](Unit4/) | ✅ 30%（证书已取得） |

### Unit 2 框架细分 / Unit 2 Frameworks

- [LangGraph](Unit2/LangGraph/notes.md) — 基于图的有状态 Agent（邮件处理图）
- [LlamaIndex](Unit2/LlamaIndex/notes.md) — 数据/RAG 与 Workflow
- [SmolAgents](Unit2/SmolAgents/notes.md) — 轻量级 CodeAgent（`@tool` / `Tool` 子类 / 多工具）

---

## 🗂️ 仓库结构 / Repository Structure

每个单元包含一份中文笔记 `notes.md` 和一个 `code/` 目录（可运行示例，与笔记分离，便于单独运行）。

Each unit has a Chinese `notes.md` and a `code/` folder (runnable examples, kept separate from notes for easy execution).

```
hf-agents-course-notes/
├── README.md
├── LICENSE
├── .gitignore
├── requirements.txt
├── Unit1/{notes.md, code/}                 # reAct.py, tool.py
├── Unit2/{notes.md, LangGraph/, LlamaIndex/, SmolAgents/}
│   ├── LangGraph/code/first_langgraph.py   # Alfred 邮件处理图
│   ├── LlamaIndex/code/workflow.py         # 最小 Workflow
│   └── SmolAgents/code/{firstAgent,multiAgent,toolClass}.py
├── Unit3/{notes.md, code/smolagents_alfred.py, code/data/invitees.jsonl}
└── Unit4/{notes.md, code/}                  # GAIA 子集评测（30% 证书线）
```

---

## 🚀 本地运行 / Run Locally

> 需要 Hugging Face Token 的示例：在根目录创建 `.env` 并填入 `HUGGINGFACEHUB_API_TOKEN=hf_xxx`（见 `.env.example`）。
> Examples that call a model need a HF token: create `.env` from `.env.example`.

1. 创建虚拟环境并安装依赖 / Create a venv and install deps:
   ```bash
   python -m venv .venv
   source .venv/bin/activate        # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```
2. 运行示例 / Run an example:
   ```bash
   # Unit 1（reAct.py 需 token；tool.py 无需）
   python Unit1/code/tool.py
   python Unit1/code/reAct.py

   # Unit 2
   python Unit2/LangGraph/code/first_langgraph.py   # 本地规则，无需 token
   python Unit2/LlamaIndex/code/workflow.py          # 无需 token
   python Unit2/SmolAgents/code/firstAgent.py        # 需 token
   python Unit2/SmolAgents/code/multiAgent.py        # 需 token
   python Unit2/SmolAgents/code/toolClass.py         # 需 token

   # Unit 3（需 token + datasets/langchain）
   python Unit3/code/smolagents_alfred.py
   ```

---

## ⚠️ 关于示例代码 / About the Example Code

本仓库中的示例代码**对齐 Hugging Face Agents Course 官方教程**（Unit 1–3），
按课程写法实现，模型统一改用 HF serverless Inference（`InferenceClientModel`），
不依赖本地 ollama。每个文件头均注明课程出处。

The example code in this repo **follows the official HF Agents Course tutorials**
(Unit 1–3). Models use HF serverless Inference (`InferenceClientModel`) instead of
local ollama. Each file notes its course source.

---

## 📄 License

代码与笔记以 [MIT License](LICENSE) 发布。

Licensed under the [MIT License](LICENSE).
