# Model Call Limit Middleware (Python)

**Channel:** LangChain
**Published:** 2025-11-20
**Video:** [Watch on YouTube](https://youtube.com/watch?v=nJEER0uaNkE)

---

# LangChain 中介軟體示範：模型呼叫次數限制

## 重點摘要
LangChain 的「模型呼叫次數限制」中介軟體是一個關鍵的防護機制，能防止自主代理 (agent) 進行過多的 API 呼叫。透過為單次互動或整個對話設定上限，開發者可以確保代理高效、可預測地運作，並在達到限制時優雅地將問題升級處理。

## 故事大綱
- **開場**：LangChain 的 Sydney 介紹了自主代理的潛在風險——它們可能因無限循環呼叫而耗盡 API 額度。她展示了「模型呼叫次數限制」中介軟體，作為控制此問題的簡單解決方案。
- **中段**：影片透過一個客服場景展示此功能。一個主代理會將帳務問題委派給一個「帳務子代理」。此子代理被設定了「單次執行最多 2 次模型呼叫」的限制。當面對簡單問題（如查詢退款政策）時，子代理能順利在限制內完成任務。然而，當被問及一個需要多次工具呼叫的複雜問題（「我被重複收費，請幫我查帳並搜尋知識庫」）時，它很快就達到了 2 次呼叫的上限。
- **結尾**：子代理在達到呼叫上限後，如預期地拋出一個錯誤。主代理成功捕捉到這個錯誤，並觸發「轉接真人客服」的工具，完美演示了如何利用此中介軟體建立一個可預測且安全的代理系統。

## 關鍵見解
1.  **自主性 vs. 控制**：代理的強大在於其自主性，但這也帶來了失控的風險（如無限迴圈或高昂成本），因此防護機制至關重要。
2.  **兩種限制類型**：此中介軟體可以限制「單次執行」（`run`，即一次使用者訊息的處理過程）或「整個對話」（`thread`）中的模型總呼叫次數。
3.  **可預測的錯誤處理**：透過將退出行為設定為 `error`，開發者可以捕捉 `ModelCallLimitExceeded` 錯誤並實作自訂邏輯，例如將問題升級給真人客服。
4.  **監督者架構的應用**：示範中使用了一種監督者模式 (supervisor architecture)，由一個主代理將任務委派給專門的子代理，但始終保留最終控制權。
5.  **簡易的實作**：只需幾行程式碼即可加入此中介軟體，為你的代理帶來顯著的安全性與成本控制效益。

## 精彩時刻
- **核心引言**：「代理之所以如此強大，是因為它們是自主的……但這種自主性也伴隨著風險。」
- **示範亮點**：當複雜查詢導致子代理失敗，而主代理流暢地將問題升級給真人時的「頓悟時刻」，完美展示了系統按預期運作的過程。
- **關鍵術語**：「單次執行限制 (Run limit)」針對單次呼叫；「對話線程限制 (Thread limit)」針對整個對話。

---

# LangChain Middleware Demo: Model Call Limit

## TL;DR
LangChain's model call limit middleware acts as a crucial guardrail to prevent autonomous agents from making excessive API calls. By setting limits per interaction or conversation, developers can ensure agents operate efficiently and predictably, gracefully escalating when limits are reached.

## Story Flow
- **Beginning**: Sydney from LangChain introduces the problem: autonomous agents can go "off the rails" and burn through API quotas. She presents the model call limit middleware as a simple solution to control this.
- **Middle**: The video demonstrates the feature with a customer service agent that delegates billing questions to a "billing sub-agent." This sub-agent is configured with a limit of two model calls per run. When faced with a simple query (like the refund policy), it succeeds within the limit. However, a complex query designed to overwhelm it ("I was charged twice, check my account and search the knowledge base") quickly hits the two-call maximum.
- **End**: Upon hitting its call limit, the sub-agent errors out as designed. The main agent successfully catches this error and triggers an "escalate to human" tool, perfectly demonstrating how the middleware creates a predictable and safe agent system.

## Key Insights
1.  **Autonomy vs. Control**: Agents are powerful because they're autonomous, but this creates risks like infinite loops or high costs. Guardrails are essential.
2.  **Two Limit Types**: The middleware can limit model calls within a single `run` (one user message) or across an entire `thread` (the whole conversation).
3.  **Predictable Error Handling**: By setting the exit behavior to `error`, you can catch the `ModelCallLimitExceeded` error and implement custom logic, like escalating to a human agent.
4.  **Supervisor Architecture**: The demo uses a supervisor pattern where a main agent delegates tasks to specialized sub-agents but retains ultimate control.
5.  **Easy Implementation**: The middleware can be added in just a few lines of code to provide significant safety and cost-control benefits for your agents.

## Notable Moments
- **Memorable Quote**: "Agents are so powerful because they are autonomous... But that autonomy comes with risk."
- **Demo Highlight**: The "Aha!" moment when the complex query causes the sub-agent to fail and the main agent smoothly escalates to a human, showing the system working exactly as intended.
- **Key Terminology**: "Run limit" (for a single invocation) vs. "Thread limit" (for a whole conversation).
