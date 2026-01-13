# Streaming Typed Agent Messages in LangChain and React

**Channel:** LangChain
**Published:** 2026-01-13
**Video:** [Watch on YouTube](https://youtube.com/watch?v=PH5kunmAAjA)

---

# 如何為生成式 UI 串流 LangGraph Agent 的回應

## 重點摘要
這部影片教學如何將 LangChain/LangGraph Agent 的執行過程與回應，即時串流到前端應用程式，以打造「生成式 UI」。影片核心展示了如何使用 LangGraph 開發伺服器與 LangChain 的 React `useStream` 鉤子 (hook)，來處理訊息串流並根據 Agent 的工具調用 (tool calls) 渲染客製化 UI 元件。

## 故事大綱
- **開場**：影片點出過去雖已討論如何建構 Agent，卻從未深入探討如何將其回應串流至前端。講者介紹將透過一系列影片，在一個新的沙盒專案（Vite + React 前端與 LangGraph 後端）中，探索為「生成式 UI」設計的各種串流模式。
- **中段**：講者詳細說明實作步驟。首先，他展示如何設定並啟動 LangGraph 開發伺服器，來託管一個具備天氣查詢和網路搜尋工具的 Agent。接著，他深入前端 React 程式碼，解釋 `useStream` 鉤子如何與後端 Agent 連接、收發訊息，並處理不同類型的訊息（如：人類、AI）。最關鍵的部分是，他示範了如何偵測 AI 訊息中的工具調用，並為其渲染特定的 UI 卡片（例如天氣資訊卡），並透過天氣查詢（觸發卡片）和新聞搜尋（僅回傳文字）兩個範例來對比展示。
- **結尾**：影片最後，講者引導觀眾查閱官方新增的前端串流文件，並預告後續影片將涵蓋更進階的主題，如：人機協作 (human-in-the-loop)、中斷點續傳 (resuming streams) 等。他鼓勵觀眾追蹤頻道並留言提出想了解的特定串流難題。

## 關鍵見解
1.  **LangGraph 開發伺服器**：它簡化了在本機託管和管理多個 Agent 的流程，讓前端可以透過一個標準化的 API 端點與之互動，實現了前後端的分離。
2.  **`useStream` React 鉤子**：這是前端串流的核心。它封裝了 WebSocket 連線管理的複雜性，開發者只需使用它提供的 `stream.messages` 來渲染畫面，並用 `stream.submit` 來發送使用者輸入，極大簡化了開發工作。
3.  **工具調用的視覺化**：Agent 的工具調用資訊是內嵌在 AI 訊息中的。前端應用程式可以解析這些資訊，並根據不同的工具，渲染出對應的客製化、互動式 UI 元件，而不僅僅是顯示純文字，從而創造更豐富的使用者體驗。
4.  **生成式 UI 不只是文字**：影片傳達的核心理念是，現代 AI 應用的 UI 應該是動態且具生成性的。它能根據 Agent 的思考路徑和工具使用情況，即時產生豐富的視覺元素和互動組件。
5.  **可擴充的 Agent 架構**：透過 LangGraph 的設定檔，可以輕鬆定義和部署多個不同的 Agent。前端的 `useStream` 鉤子只需透過名稱就能指定與哪個 Agent 互動，讓單一應用程式能同時與多個特製 Agent 溝通。

## 精彩時刻
- **經典開發哏**：「在展示 Agent 行為時，每個人都喜歡用天氣工具。」這句話展現了開發者社群的共同經驗和影片的輕鬆風格。
- **關鍵展示**：當輸入「舊金山現在天氣如何？」時，畫面即時渲染出一個精美的天氣卡片；而當搜尋「AI 新聞」時，則僅顯示文字回覆。這個對比清楚地展示了條件式 UI 渲染的核心概念。
- **未來預告**：影片結尾預告了未來將探討「人機協作」、「中斷點續傳」、「顯示推理過程」等更複雜的串流模式，為整個系列影片提供了明確的藍圖和期待感。

---

# How to Stream LangGraph Agent Responses for Generative UI

## TL;DR
This video teaches how to stream the execution process and responses from a LangChain/LangGraph agent to a front-end application to build "Generative UIs." The core demonstration shows how to use the LangGraph dev server and LangChain's `useStream` React hook to handle the message stream and render custom UI components based on the agent's tool calls.

## Story Flow
- **Beginning**: The video highlights a gap in previous tutorials: how to stream agent responses to the front end. The presenter introduces the goal for a new series: to explore various streaming patterns for "Generative UI" within a new sandbox project (Vite + React front end with a LangGraph back end).
- **Middle**: The presenter details the implementation. First, he shows how to configure and run the LangGraph dev server to host an agent equipped with tools for getting weather and searching the web. He then dives into the front-end React code, explaining how the `useStream` hook connects to the agent, sends/receives messages, and handles different message types (Human, AI). The key part is demonstrating how to detect tool calls within an AI message and render a specific UI card for it (e.g., a weather info card), which is showcased with two contrasting examples: a weather query (triggering the card) and a news search (returning only text).
- **End**: The video concludes by directing viewers to the newly added official documentation on front-end streaming. The presenter teases future videos on advanced topics like human-in-the-loop and resuming streams, encouraging viewers to follow the channel and suggest specific streaming challenges they face.

## Key Insights
1.  **LangGraph Dev Server**: It simplifies hosting and managing multiple agents locally, making them accessible to the front end via a standardized API endpoint and enabling a clean front-end/back-end separation.
2.  **The `useStream` React Hook**: This is the core of the front-end streaming implementation. It abstracts away the complexity of WebSocket connection management, allowing developers to simply use `stream.messages` for rendering and `stream.submit` to send user input, greatly simplifying development.
3.  **Visualizing Tool Calls**: Agent tool call information is embedded within AI messages. The front-end application can parse this data and render corresponding custom, interactive UI components for different tools, creating a much richer user experience than just plain text.
4.  **Generative UI is More Than Text**: The video's core philosophy is that modern AI application UIs should be dynamic and generative. They should be able to produce rich visual elements and interactive components in real-time based on the agent's reasoning path and tool usage.
5.  **Scalable Agent Architecture**: The LangGraph config file makes it easy to define and deploy multiple, distinct agents. The `useStream` hook on the front end can target a specific agent by name, allowing a single application to communicate with multiple specialized agents simultaneously.

## Notable Moments
- **Classic Dev Humor**: "everyone likes weather tools uh when displaying agent behavior." This line captures the shared experience of the developer community and the video's relaxed tone.
- **The Key Demo**: When "What's the weather in San Francisco?" is entered, the UI instantly renders a polished weather card. In contrast, searching for "AI news" just displays a text response. This comparison clearly illustrates the core concept of conditional UI rendering.
- **Future Teasers**: The preview of upcoming topics like "human-in-the-loop," "resuming streams," and "displaying reasoning information" provides a clear and exciting roadmap for the video series.
