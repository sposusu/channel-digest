# Tracing Claude Code to LangSmith

**Channel:** LangChain
**Published:** 2025-12-19
**Video:** [Watch on YouTube](https://youtube.com/watch?v=NoSmSVKMSMs)

---

# 深入解析 Claude Code：與 LangSmith 的整合實戰

## 重點摘要
這部影片介紹了 LangChain 為 Claude Code 開發的 LangSmith 整合功能。透過這項整合，開發者可以觀測 Claude Code 在執行任務時的每一個內部步驟，包含大型語言模型 (LLM) 的思考過程與工具呼叫，從而實現對 AI 工作流程的高度可視性。

## 故事大綱
- **開場：** 來自 LangChain 的 Tanish 介紹了這項新功能，並展示一個簡單的專案。他向 Claude Code 提問：「這個檔案中的系統提示是什麼？」藉此展示一個基本互動。
- **中段：** Tanish 接著在 LangSmith 中展示了該互動的追蹤紀錄 (trace)，清晰地呈現了 LLM 的推理、`read_file` 工具的呼叫以及最終的回應生成。隨後，他給出一個更複雜的任務：要求 Claude Code 修改程式碼，使用 Open Mateo API 來獲取舊金山的即時天氣。追蹤紀錄顯示 Claude Code 採用了多步驟策略：規劃、使用 `web_fetch` 工具研究 API 文件、生成程式碼，最後使用 `edit` 工具應用變更。
- **結尾：** Tanish 解釋了整合的運作原理。Claude Code 會自動生成對話紀錄 (transcripts)，一個「停止掛鉤」(stop hook) 會在每次互動後觸發，解析這些紀錄並將其格式化後傳送到 LangSmith，進而生成視覺化的追蹤圖表。他也簡述了設定過程，僅需一個掛鉤腳本與幾個環境變數即可啟用。

## 關鍵見解
1.  **深度可觀測性：** LangSmith 整合讓 Claude Code 的「思考過程」完全透明，將抽象的 AI 操作分解為具體的 LLM 呼叫與工具使用步驟。
2.  **複雜任務的分解：** 影片中的天氣 API 範例證明，Claude Code 會透過「規劃 -> 探索 -> 實作」的模式來解決複雜的程式設計問題。
3.  **輕量級的整合架構：** 此功能巧妙地利用 Claude Code 內建的對話紀錄與掛鉤 (hooks) 機制，無需對核心工具進行侵入式修改即可實現。
4.  **簡易的設定流程：** 開發者只需設定一個掛鉤腳本和相關的 LangSmith 環境變數，就能在自己的專案中啟用追蹤，控制門檻低。
5.  **除錯與優化的利器：** 透過視覺化的追蹤紀錄，開發者能輕易地診斷 AI 工作流程中的瓶頸或非預期行為，並對其進行優化。

## 精彩時刻
- 「能夠看到完整的追蹤紀錄，這實在太迷人了。」
- 將寫死的假天氣資料，改為呼叫即時天氣 API 的範例，完美展示了工具的強大能力。
- Tanish 解釋這項整合如何「揭開神秘面紗」(peel the curtain)，讓我們一窺 Claude Code 的幕後運作。

---

# Peeking Behind the Curtain: Claude Code & LangSmith Integration

## TL;DR
This video introduces a LangChain-built integration for Claude Code with LangSmith, an observability platform. This allows developers to see every step Claude Code takes to fulfill a request, including its internal LLM calls and tool usage, providing powerful observability into AI-driven workflows.

## Story Flow
- **Beginning:** Tanish from LangChain introduces the integration with a very simple agent. He starts a Claude Code session and asks a basic question: "What is the system prompt in this file?"
- **Middle:** He then shows the resulting trace in LangSmith, which visualizes the LLM's reasoning, the `read_file` tool call, and the final response. To demonstrate a more complex scenario, he asks Claude Code to modify the agent to fetch real-time weather for San Francisco using the Open Mateo API. The trace reveals a multi-step process: the LLM first plans its actions, uses the `web_fetch` tool to understand the API, generates the necessary code, and finally uses the `edit` tool to apply it.
- **End:** Tanish explains how the integration works. It leverages two Claude Code features: auto-generated conversation transcripts and "stop hooks." A custom script, triggered by the stop hook after each response, parses the transcript and sends the structured data to LangSmith to create the visual trace. He briefly covers the simple setup process, which involves the hook script and a few environment variables.

## Key Insights
1.  **Deep Observability:** The LangSmith integration makes Claude Code's "thought process" transparent, breaking down abstract AI actions into concrete LLM calls and tool invocations.
2.  **Complex Task Decomposition:** The weather API example shows that Claude Code approaches complex coding problems with a "plan, explore, implement" strategy, which is fully visible in the trace.
3.  **Lightweight Architecture:** The integration cleverly uses Claude Code's built-in transcript and hook features, making it a non-invasive way to add observability.
4.  **Simple Setup:** Developers can enable tracing per-project by configuring a hook script and adding their LangSmith API key and project settings to a local JSON file.
5.  **A Powerful Debugging Tool:** The visual trace makes it easy to diagnose unexpected behavior or inefficiencies in an AI's workflow and provides clear insights for optimization.

## Notable Moments
- "It's pretty fascinating to see the entire trace."
- The demonstration of changing a hardcoded value to a live API call is a great highlight of the tool's practical power.
- The explanation of how the integration helps "peel the curtain" and look behind the scenes of Claude Code's operations.
