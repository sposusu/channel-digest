# Build Better Agent UX: Streaming Progress, Status, and File Ops with LangChain

**Channel:** LangChain
**Published:** 2026-01-15
**Video:** [Watch on YouTube](https://youtube.com/watch?v=3daSUNpWErQ)

---

# 使用 LangChain 自訂串流事件，打造即時 AI Agent UI

## 重點摘要
本影片探討當 AI Agent 的工具調用（tool call）耗時過長時，如何改善使用者體驗。影片展示了如何使用 LangChain 的自訂串流事件（custom stream events），從後端 Agent 向前端 React 應用程式發送即時進度更新，從而打造出反應更靈敏、資訊更透明的介面。

## 故事大綱
- **開場**：影片首先點出一個常見問題——當工具調用需要較長時間（例如觸發一個子 Agent）時，使用者介面只會顯示一個單調的載入指示器，使用者無法得知背景處理的進度，體驗不佳。
- **中段**：影片提出了「自訂串流事件」作為解決方案。在後端，透過工具函式中的 `config.writer`，Agent 可以在執行過程中，主動發送包含進度資訊的任意事件。這些事件應包含 `type` 以供前端識別，以及 `tool_call_id` 以便將進度與特定的工具調用關聯。在前端 React 應用中，則使用 `useStream` 鉤子中的 `onCustomEvent` 處理器來接收這些事件，並透過輔助函式進行類型驗證，最終將即時進度呈現在對應的 UI 元件上。
- **結尾**：影片展示了改進前後的對比：從一個單純的載入中狀態，變為一個能即時顯示各個工具調用進度的動態介面。影片總結，此方法能大幅提升應用的響應速度與使用者體驗，並鼓勵觀眾查看完整的範例程式碼與官方文件。

## 關鍵見解
1.  **使用者體驗至關重要**：對於非即時完成的操作，提供持續的背景進度回饋是維持良好使用者體驗的關鍵。
2.  **後端主動推送**：LangChain 的 `config.writer` 函式是核心，它讓工具在執行期間能主動、任意地向客戶端推送自訂事件。
3.  **事件結構化**：為了讓前端能正確解析並呈現資訊，發送的自訂事件應包含 `type`（事件類型）和 `tool_call_id`（關聯的工具調用），這是一個最佳實踐。
4.  **前端事件處理**：前端需透過 `onCustomEvent` 這類專門的處理器來捕獲串流事件，並搭配 TypeScript 的類型防禦（type guards）來安全地處理與呈現資料。
5.  **提升感知效能**：即使工具執行的總時間不變，透過串流即時更新，能讓應用程式感覺上更快速、更具互動性，有效緩解使用者的等待焦慮。

## 精彩時刻
- 點出問題核心：「一個真正反應靈敏的 UI 應該給予使用者持續的更新，確保他們知道背景有事情正在發生。」
- 揭示後端解法：「我們透過 `config.writer` 函式來做到這一點。」
- 介紹前端串接：「在前端，我們透過 `useStream` 鉤子裡的 `onCustomEvent` 處理器來取得這些自訂事件。」

---

# Building Responsive AI UIs with LangChain Custom Stream Events

## TL;DR
This video addresses how to improve user experience when an AI agent's tool calls are time-consuming. It demonstrates using LangChain's custom stream events to send real-time progress updates from the backend agent to a React frontend, resulting in a much more responsive and informative interface.

## Story Flow
- **Beginning**: The video starts by highlighting a common problem: when a tool call takes a long time (e.g., triggering a sub-agent), the UI just shows a generic loading indicator, leaving the user uninformed about the background progress, which leads to a poor experience.
- **Middle**: The solution, "custom stream events," is introduced. In the backend, the `config.writer` function within a tool allows the agent to actively send arbitrary events with progress information during its execution. These events should include a `type` for identification and a `tool_call_id` to associate the progress with the specific tool call. In the React frontend, the `onCustomEvent` handler within the `useStream` hook is used to receive these events, which are then type-checked with helper functions and rendered as real-time updates in the appropriate UI components.
- **End**: The video shows a before-and-after comparison: a simple loading state versus a dynamic interface that displays live progress for each tool call. It concludes that this method significantly improves application responsiveness and user experience, encouraging viewers to check out the full example code and documentation.

## Key Insights
1.  **User Experience is Key**: Providing continuous feedback on background progress is crucial for a good UX when operations are not instantaneous.
2.  **Active Push from the Backend**: LangChain's `config.writer` function is the core mechanism that allows a tool to actively and arbitrarily push custom events to the client during its runtime.
3.  **Structured Events**: It's a best practice to structure custom events with a `type` (for event identification) and `tool_call_id` (for association) so the frontend can correctly parse and display the information.
4.  **Frontend Event Handling**: The frontend needs a dedicated handler like `onCustomEvent` to capture streamed events, coupled with TypeScript type guards to safely process and render the data.
5.  **Improved Perceived Performance**: Even if the tool's total execution time remains the same, streaming real-time updates makes the application feel faster and more interactive, effectively reducing user anxiety while waiting.

## Notable Moments
- On the core problem: "A really responsive UI should give a user constant updates to ensure they know something is happening in the background."
- On the backend solution: "We do this with the `config.writer` function."
- On the frontend connection: "In our front end, we get access to these custom events through the `onCustomEvent` handler which is part of the `useStream` hook that we have."
