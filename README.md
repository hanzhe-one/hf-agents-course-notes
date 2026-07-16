# Hugging Face Agents 课程笔记 · 学习仓库

> HF Agents Course — Notes & Minimal Examples

这是我学习 [Hugging Face Agents Course](https://huggingface.co/learn/agents-course) 前三单元（Unit 1–3）时整理的笔记与可运行示例代码集合。仓库用于**个人总结与分享展示**。

This repo collects my notes and minimal runnable examples from the first three units (Unit 1–3) of the [Hugging Face Agents Course](https://huggingface.co/learn/agents-course). It serves as both a personal study log and a shareable showcase.

---

## 📚 单元导航 / Unit Navigation

| 单元 Unit | 主题 Topic | 笔记 Notes | 要点 Highlights |
| --- | --- | --- | --- |
| **Unit 1** | Agent 基础 / Agent Fundamentals | [Unit1/notes.md](Unit1/notes.md) | ReAct 循环、工具定义、基础 Agent |
| **Unit 2** | 三大框架 / Three Frameworks | [Unit2/notes.md](Unit2/notes.md) | LangGraph · LlamaIndex · SmolAgents |
| **Unit 3** | 综合应用 / Applied Agents | [Unit3/notes.md](Unit3/notes.md) | 端到端 Agent 应用（如 Alfred 助手） |
| Unit 4 | 待续 / Coming soon | [Unit4/](Unit4/) | 学习中，敬请期待 |

### Unit 2 框架细分 / Unit 2 Frameworks

- [LangGraph](Unit2/LangGraph/notes.md) — 基于图的有状态 Agent
- [LlamaIndex](Unit2/LlamaIndex/notes.md) — 数据/RAG 与 Workflow
- [SmolAgents](Unit2/SmolAgents/notes.md) — 轻量级 CodeAgent

---

## 🗂️ 仓库结构 / Repository Structure

每个单元包含一份中文笔记 `notes.md` 和一个 `code/` 目录（最小可跑示例，与笔记分离，便于单独运行）。

Each unit has a Chinese `notes.md` and a `code/` folder (minimal runnable examples, kept separate from notes for easy execution).

```
hf-agents-course-notes/
├── README.md
├── LICENSE
├── .gitignore
├── requirements.txt
├── Unit1/{notes.md, code/}
├── Unit2/{notes.md, LangGraph/, LlamaIndex/, SmolAgents/}
├── Unit3/{notes.md, code/}
└── Unit4/   # 预留 placeholder
```

---

## 🚀 本地运行 / Run Locally

> 部分示例需要 Hugging Face Token（`HUGGINGFACEHUB_API_TOKEN`）。在根目录创建 `.env` 文件并填入：`HUGGINGFACEHUB_API_TOKEN=hf_xxx`

1. 创建虚拟环境并安装依赖 / Create a venv and install deps:
   ```bash
   python -m venv .venv
   source .venv/bin/activate        # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```
2. 运行示例 / Run an example:
   ```bash
   python Unit1/code/reAct.py
   python Unit2/SmolAgents/code/firstAgent.py
   ```

---

## ⚠️ 关于示例代码 / About the Example Code

本仓库中的示例代码由我**基于 HF Agents Course 官方公开教程重新实现**，仅作学习对照之用，文件头均注明出处。

The example code in this repo is **re-implemented from the official HF Agents Course public tutorials** for study purposes; each file notes its source.

---

## 📄 License

代码与笔记以 [MIT License](LICENSE) 发布。

Licensed under the [MIT License](LICENSE).
