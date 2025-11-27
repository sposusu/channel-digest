# What are Deep Agents?

**Channel:** LangChain
**Published:** 2025-11-24
**Video:** [Watch on YouTube](https://youtube.com/watch?v=IVts6ztrkFg)

---

# 介紹 Deep Agents：一個用於複雜 AI 任務的開源框架

## 重點摘要
`deep-agents` 是一個基於 LangChain 和 LangGraph 的、有特定主張的開源代理人（Agent）框架。它提供一小組強大的預建工具（檔案系統、終端機、規劃、子代理人），讓 AI 代理人能執行更長、更複雜的「深度工作」任務，並將複雜性從程式碼轉移到精密的提示（prompt）中。

## 故事大綱
- **開場**：影片主講人 Lance 介紹了「深度代理人」（Deep Agents）的概念，指出 AI 代理人能處理的任務長度大約每七個月就翻一倍。他以 Claude Code、Devin 等成功的長時任務代理人為例，說明它們都依賴一小組簡單但功能強大的「原子工具」。

- **中段**：Lance 解釋了這些核心工具，包括：用於存取電腦的檔案系統、執行腳本的終端機（Shell）、用於長期任務的規劃能力，以及用於隔離上下文的子代理人委派。他接著闡明了 `deep-agents` 與 LangChain（提供通用抽象）和 LangGraph（提供底層運行環境）的關係，將 `deep-agents` 定位為一個整合了特定工具與提示的、有特定主張的框架。

- **結尾**：Lance 宣布釋出 `deep-agents` 0.2 版（包含可插拔後端、中介軟體等新功能）以及 `deep-agents` CLI 工具。這個 CLI 工具讓開發者可以在自己的電腦上運行一個能存取本地檔案系統的深度代理人，就像 Claude Code 一樣。他最後強調此專案完全開源，並歡迎社群貢獻與反饋。

## 關鍵見解
1.  **代理人能力迅速增長**：AI 代理人處理任務的複雜度和長度正以驚人速度成長，大約每七個月翻一倍，使得「深度工作」成為可能。
2.  **少即是多**：成功的代理人並非使用大量工具，而是依賴一小組通用的「原子工具」，如檔案系統、終端機、規劃和子代理人委派。
3.  **提示即程式**：開發的複雜性正從傳統程式碼轉移到提示工程。透過高度詳細的指令，可以引導少數幾個強大的工具完成複雜任務。
4.  **善用檔案系統**：檔案系統不僅能為模型的上下文視窗減輕負擔（卸載內容），還能儲存代理人可隨時執行的可重用腳本或「技能」。
5.  **框架整合**：`deep-agents` 將上述概念打包成一個基於 LangChain/LangGraph 的開源框架，讓開發者能更輕易地建構自己的複雜代理人。

## 精彩時刻
- **關鍵數據**：「代理人能承擔的任務長度，大約每七個月翻一倍。」
- **核心比喻**：`deep-agents` 是一個建立在 LangChain 框架和 LangGraph 運行環境之上的「有特定主張的代理人框架」(opinionated agent harness)。
- **最大亮點**：發布了 `deep-agents` CLI，讓使用者可以在自己的電腦上運行一個強大的代理人，就像 Claude Code 一樣，能夠直接存取本地檔案系統。

---

# Introducing Deep Agents: An Open-Source Harness for Complex AI Tasks

## TL;DR
`deep-agents` is an open-source, opinionated agent harness built on LangChain and LangGraph. It provides a small set of powerful, pre-built tools (file system, shell, planning, sub-agents) to enable AI agents to perform longer, more complex "deep work" tasks, moving complexity from code into sophisticated prompts.

## Story Flow
- **Beginning**: The speaker, Lance, introduces the concept of "deep agents," noting that the length of tasks AI agents can handle is doubling roughly every seven months. He points to successful long-running agents like Claude Code and Devin, which rely on a small set of simple yet powerful "atomic tools."

- **Middle**: Lance explains these core tools: file system access, a shell for script execution, planning for long-term tasks, and sub-agent delegation for context isolation. He then clarifies the relationship between `deep-agents`, LangChain (providing abstractions), and LangGraph (the underlying runtime), positioning `deep-agents` as an opinionated harness that integrates specific tools and prompts.

- **End**: Lance announces the release of `deep-agents` 0.2 (with new features like pluggable backends and middleware) and the `deep-agents` CLI. This CLI allows developers to run a deep agent on their local machine with access to the file system, much like Claude Code. He concludes by emphasizing that the project is fully open-source and welcomes community contributions and feedback.

## Key Insights
1.  **Rapid Growth in Agent Capability**: The complexity and length of tasks agents can handle are growing exponentially, doubling approximately every seven months, making "deep work" feasible.
2.  **Less is More**: Successful agents don't use a vast number of tools but rely on a small set of general-purpose "atomic" tools like file system access, a shell, planning, and sub-agent delegation.
3.  **The Prompt is the Program**: Complexity is shifting from traditional code to prompt engineering. Highly detailed instructions can guide a few powerful tools to accomplish complex tasks.
4.  **Leverage the File System**: The file system is crucial not only for offloading context from the model's context window but also for storing reusable scripts or "skills" that the agent can execute.
5.  **Framework Integration**: `deep-agents` packages these concepts into an open-source harness built on LangChain/LangGraph, making it easier for developers to build their own sophisticated agents.

## Notable Moments
- **Key Statistic**: "The length of tasks that an agent can take is doubling roughly every seven months."
- **Core Analogy**: `deep-agents` is described as an "opinionated agent harness" built on top of the LangChain framework and LangGraph runtime.
- **Major Highlight**: The release of the `deep-agents` CLI, which allows users to run a powerful agent locally on their own machine with access to their file system, similar to Claude Code.
