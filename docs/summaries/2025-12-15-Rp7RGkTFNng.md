# Building & Observing a Deep Agent for Email Triage with LangSmith

**Channel:** LangChain
**Published:** 2025-12-15
**Video:** [Watch on YouTube](https://youtube.com/watch?v=Rp7RGkTFNng)

---

# 如何用 AI Agents 打造 AI Agents

## 重點摘要
本影片展示如何使用 LangSmith 的新功能（特別是 Poly 和 `langsmith fetch`）來偵錯、監控並改善 AI Agents。講者建立了一個簡單的郵件助理 agent，並利用 LangSmith 的工具，讓另一個「寫程式 agent」能自動修正其行為並撰寫測試，實現一個由 AI 驅動的開發循環。

## 故事大綱
- **開場：** 介紹一個簡單的 AI agent (`agent.py`)，其任務是根據詳細的系統提示詞來分類和回覆收到的郵件。講者強調，建立 agent 的初始版本非常簡單，但真正的挑戰在於確保它能正確運作。
- **中段：** 執行 agent 處理一封來自朋友 Oliver Queen 的會議邀約郵件。初步的終端機輸出雜亂難懂，於是改用 LangSmith 的追蹤（tracing）功能，清晰地呈現了 agent 的每一步決策。接著，使用 LangSmith 中的新工具「Poly 鸚鵡」與該追蹤紀錄對話，快速總結出 agent 的行為：它接受了一個過早的會議（早上 8 點）。
- **結尾：** 為了修正「不喜歡早起開會」這個問題，講者展示了 `langsmith fetch` 指令，它能將 LangSmith 的追蹤資料拉回本地終端機。然後，他啟動一個「寫程式 agent」，該 agent 使用 `langsmith fetch` 讀取執行紀錄，理解問題後，自動修改了系統提示詞（要求 agent 拒絕早上 9 點前的會議），並為此新增了一個 `pytest` 測試案例以確保問題被永久修復。

## 關鍵見解
1.  **Agent 的初始建置很簡單，但驗證與迭代是關鍵：** 真正困難的不是寫出 agent 的第一版，而是確保它在各種情境下都能如預期般運作並持續改進。
2.  **可觀測性是 Agent 開發的基石：** LangSmith 的追蹤功能提供了無可取代的價值，它讓開發者能清楚看見 agent 的「思考過程」與每一步的工具調用。
3.  **用對話方式加速偵錯：** Poly 工具讓開發者能像聊天一樣查詢複雜的 agent 執行紀錄，省去手動點擊、分析每一個步驟的麻煩。
4.  **打通監控與本地開發的橋樑：** `langsmith fetch` 讓「寫程式 agent」能夠以編程方式存取觀測數據，從而實現自動化的偵錯、修正與測試循環。
5.  **測試 Agent 的彈性至關重要：** 使用像 `pytest` 這樣的標準測試框架，可以靈活地斷言工具是否被正確調用，或甚至利用另一個大型語言模型（LLM）來評斷最終輸出的品質。

## 精彩時刻
- **Poly 鸚鵡登場：** 影片中介紹了一個名為「Poly the parrot」的可愛工具，它能讀取 agent 的執行紀錄並用自然語言回答相關問題。
- **修正的動機：** 整個修正流程的觸發點非常生活化：「我其實不喜歡早起」（I don't love waking up early），這使得整個示範更具說服力。
- **Agent 驅動的開發循環：** 最精彩的部分是展示一個 agent (`deep agent CLI`) 如何利用 `langsmith fetch` 來診斷另一個 agent 的錯誤、自動修改程式碼、新增測試，並不斷迭代直到測試通過為止。

---

# How to Use AI Agents to Build AI Agents

## TL;DR
This video demonstrates how to use LangSmith's new features, specifically Poly and `langsmith fetch`, to debug, monitor, and improve AI agents. The speaker builds a simple email assistant agent and then uses LangSmith's tools to allow another "coding agent" to automatically fix its behavior and write tests, creating an AI-driven development loop.

## Story Flow
- **Beginning:** An introduction to a simple AI agent (`agent.py`) designed to triage and respond to incoming emails based on a detailed system prompt. The speaker emphasizes that building the initial agent is easy, but the real challenge is ensuring it works correctly.
- **Middle:** The agent is run on an example email from a friend, Oliver Queen, requesting a meeting. The initial terminal output is hard to parse, so the view switches to LangSmith tracing, which clearly shows every step the agent took. Next, "Poly the parrot," a new tool in LangSmith, is used to conversationally summarize the trace, quickly revealing that the agent accepted a meeting that was too early (8 a.m.).
- **End:** To fix the issue of not wanting early meetings, the speaker showcases the `langsmith fetch` command, which pulls trace data from LangSmith into the local terminal. He then invokes a "coding agent" that uses `langsmith fetch` to read the execution history, understands the problem, and automatically modifies the system prompt (telling the agent to decline meetings before 9 a.m.). It also adds a `pytest` test case to ensure the fix is permanent.

## Key Insights
1.  **Initial Agent setup is simple, but validation and iteration are key:** The hard part of building agents isn't the first version; it's ensuring they behave as expected across various scenarios and continuously improving them.
2.  **Observability is fundamental for Agent development:** LangSmith tracing provides invaluable visibility into an agent's "thought process" and tool calls at each step.
3.  **Conversational debugging speeds up analysis:** The Poly tool allows developers to query complex agent traces as if in a chat, saving the tedious effort of manually clicking through and analyzing each step.
4.  **Bridging the gap between monitoring and local development:** `langsmith fetch` enables "coding agents" to programmatically access observability data, creating an automated loop of debugging, fixing, and testing.
5.  **Flexibility in testing agents is crucial:** Using standard testing frameworks like `pytest` allows for flexible assertions, such as checking if a specific tool was called or even using another LLM as a "judge" to evaluate the quality of the final output.

## Notable Moments
- **The introduction of Poly the parrot:** A charming tool is introduced that can read an agent's run history and answer questions about it in natural language.
- **A relatable motivation for the fix:** The entire debugging workflow is triggered by a very human problem: "I don't love waking up early," which makes the demonstration highly effective.
- **The Agent-driven development loop:** The highlight is seeing one agent (the `deep agent CLI`) use `langsmith fetch` to diagnose another agent's failure, automatically edit the code, add a test, and iterate until the test passes.
