# Model Call Limit Middleware (Python)

**Channel:** LangChain
**Published:** 2025-11-20
**Video:** [Watch on YouTube](https://youtube.com/watch?v=nJEER0uaNkE)

---

# LangChain教學：用模型呼叫限制中介軟體為你的AI代理加上「護欄」

## 重點摘要
本影片介紹了LangChain的「模型呼叫限制中介軟體」（Model Call Limit Middleware），這是一個關鍵的保護機制，能防止AI代理（agent）因無限循環或過度自主而濫用API。開發者可以透過設定單次任務或整個對話的呼叫次數上限，有效控制成本並確保系統穩定。

## 故事大綱
- **開場**：LangChain的Sydney點出AI代理的自主性是一把雙面刃，雖然強大但也有失控風險，可能導致API額度被耗盡。她接著介紹了「模型呼叫限制中介軟體」作為解決方案。
- **中段**：影片展示了如何設定此中介軟體，區分了兩種限制模式：「單次運行限制」（run limit）針對單一指令的處理過程，以及「對話線程限制」（thread limit）針對整個對話的總呼叫次數。接著，她透過程式碼建立一個客服代理，此代理會將帳務問題轉交給一個設有「單次運行最多2次」呼叫限制的「帳務子代理」。
- **結尾**：Sydney進行了兩次測試。第一次，一個簡單問題（退款政策），子代理在限制內成功完成。第二次，一個複雜問題（重複收費查詢），子代理嘗試呼叫工具兩次後達到上限，系統成功捕捉到錯誤並觸發「轉接真人客服」流程。這個結果完美展示了此護欄機制的功用。

## 關鍵見解
1.  **自主性的風險管理**：AI代理的自主決策能力需要搭配護欄機制，以避免失控行為和無法預期的資源消耗。
2.  **兩種限制模式**：開發者可以根據需求，精準控制單次互動（run）或整個對話（thread）的API呼叫上限。
3.  **優雅地處理失敗**：當代理達到呼叫上限時，系統可以設定為拋出錯誤，讓開發者能捕捉此狀況並執行備用方案，例如「轉接真人客服」，而非直接崩潰。
4.  **實用的監督者架構**：影片中的主代理與子代理設計，展示了一種「監督者模式」，主代理負責分派任務，而子代理在各自的規範下運作，實現了功能模組化與風險隔離。
5.  **簡易高效的實現**：只需幾行程式碼，就能為AI應用加上一道重要的安全防線，大幅提升系統的穩定性與可預測性。

## 精彩時刻
- **核心痛點**：「代理可能會失控，呼叫數百次工具，燒光你的API額度。」
- **「啊哈！」時刻**：在複雜問題測試中，從追蹤視圖（trace view）可以清楚看到子代理在兩次工具呼叫後，拋出了`ModelCallLimitExceeded`錯誤，並成功觸發了`escalate_to_human`工具，完美驗證了設計。
- **關鍵概念區分**：清楚解釋了「run limit」（針對單次調用）和「thread limit」（針對整個對話）的差異，幫助開發者選擇正確的限制策略。

---

# LangChain Demo: Guardrail Your AI Agent with Model Call Limit Middleware

## TL;DR
This video introduces LangChain's Model Call Limit Middleware, a critical guardrail to prevent AI agents from overusing APIs through infinite loops or excessive autonomy. By setting limits on model calls per invocation or across an entire conversation, developers can effectively control costs and ensure system stability.

## Story Flow
- **Beginning**: Sydney from LangChain highlights the double-edged sword of agent autonomy: while powerful, it carries the risk of agents going "off the rails" and burning through API quotas. She introduces the Model Call Limit Middleware as the solution.
- **Middle**: The video explains how to configure the middleware, distinguishing between a "run limit" (for a single invocation) and a "thread limit" (for an entire conversation). A code demo follows, building a customer service agent that delegates billing questions to a sub-agent configured with a `run_limit` of 2 model calls.
- **End**: Sydney runs two tests. First, a simple query (refund policy), which the sub-agent handles successfully within the limit. Second, a complex query designed to overwhelm it (duplicate charge investigation), which causes the sub-agent to hit its call limit. The system gracefully catches the error and triggers an escalation to a human, perfectly demonstrating the guardrail in action.

## Key Insights
1.  **Managing Autonomy Risk**: The decision-making power of autonomous agents needs guardrails to prevent uncontrolled behavior and unpredictable resource consumption.
2.  **Two Types of Limits**: Developers can precisely control API usage by setting limits per single interaction (`run`) or across an entire conversation (`thread`).
3.  **Graceful Failure & Escalation**: When an agent hits its call limit, the system can be set to raise an error. This allows developers to catch it and implement fallback logic, like escalating to a human, instead of crashing.
4.  **Practical Supervisor Architecture**: The main agent/sub-agent design showcases a "supervisor" pattern, where a primary agent delegates tasks to specialized agents that operate under their own constraints, enabling modularity and risk isolation.
5.  **Simple and Effective Implementation**: With just a few lines of code, developers can add a crucial safety feature to their AI applications, significantly improving reliability and predictability.

## Notable Moments
- **The Core Problem**: "Agents can go off the rails and call hundreds of tools and burn through your API quotas."
- **The "Aha!" Moment**: In the complex query test, the trace view clearly shows the `ModelCallLimitExceeded` error after two tool calls, followed by the successful invocation of the `escalate_to_human` tool, perfectly validating the design.
- **Key Concept Distinction**: The clear explanation of the difference between a `run limit` (for a single invocation) and a `thread limit` (for an entire conversation) helps developers choose the right strategy.
