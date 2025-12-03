# Building an Email Assistant with Langsmith Agent Builder

**Channel:** LangChain
**Published:** 2025-12-03
**Video:** [Watch on YouTube](https://youtube.com/watch?v=PwldOnb0eiU)

---

# 使用 Langsmith Agent Builder 打造免寫程式碼的電子郵件助理

## 重點摘要
Langsmith Agent Builder 讓使用者無需編寫任何程式碼，即可透過一個互動式的聊天介面，快速建立並客製化一個生產等級的 AI 代理人。影片示範了如何利用此工具，在幾分鐘內打造一個能夠自動整理、排序並草擬回覆的電子郵件助理。

## 故事大綱
- **開場**：影片由 LangChain 的 Jacob 開始，他介紹了新發布的公開測試版產品——Langsmith Agent Builder，一個無需寫程式碼即可建立 AI 代理人的工具，並預告將示範如何建立一個熱門應用：電子郵件助理。
- **中段**：Jacob 進入 Agent Builder 的聊天介面，系統透過一連串的問答（例如：如何啟動、需執行什麼任務、處理哪些郵件、如何輸出結果）來引導設定。設定完成後，他展示了代理人的詳細配置，包括系統提示、觸發器和可用工具。接著，他透過直接下達自然語言指令（「將內部團隊郵件的優先級設為最高」），成功地修改了代理人的行為，並展示了系統提示的即時更新。
- **結尾**：Jacob 測試了更新後的代理人，它成功地將一封來自內部的測試郵件識別為「高優先級」。他總結了整個過程的簡易性，並邀請觀眾前往 langsmith.com 免費試用。

## 關鍵見解
- **免程式碼開發**：核心價值在於讓非技術背景的使用者也能建立功能強大的 AI 代理人。
- **對話式設定**：建構過程就像與人對話，系統會主動提問以釐清需求，大幅降低了使用門檻。
- **即時反饋與迭代**：使用者可以用自然語言直接修改代理人的行為，系統會立即更新其核心邏輯（系統提示），讓調整和優化變得非常直觀。
- **透明與可控**：介面會清楚展示代理人的設定、工具和觸發條件，並提供一個「手動批准工具呼叫」的開關，讓使用者在測試時能完全掌控代理人的每一步行動。
- **專為實際應用**：此工具旨在解決真實世界的問題，如影片中的郵件助理，能處理分類、排序、摘要和草擬回覆等實用任務。

## 精彩時刻
- 在示範中，Jacob 承認為了讓結果乾淨，他先把自己的收件匣清空了，所以測試時只有一封他自己寄給自己的「有點老套（hokey）」的測試郵件。
- 最令人印象深刻的部分是，僅用一句日常對話般的指令：「我希望優先處理來自我們團隊成員的內部郵件」，代理人就立即更新了其優先級判斷標準。
- 影片開頭的預設提示直接點出：「建立一個 AI 郵件助理」，展示了其針對明確目標的快速啟動能力。

---

# Building a No-Code Email Assistant with Langsmith Agent Builder

## TL;DR
Langsmith Agent Builder allows users to create and customize production-grade AI agents without writing any code, using an interactive chat interface. The video demonstrates how to build an email assistant that can automatically organize, prioritize, and draft replies in just a few minutes.

## Story Flow
- **Beginning**: Jacob from LangChain introduces the newly released Langsmith Agent Builder, a no-code tool for creating agents. He proposes building a popular use case: an email assistant.
- **Middle**: Jacob uses the Agent Builder chat interface, where the system asks clarifying questions (how it should be activated, what tasks to perform, which emails to focus on, output format) to configure the agent. After setup, he shows the agent's detailed configuration, including its system prompt, triggers, and tools. He then modifies the agent's behavior by giving it a natural language command ("prioritize internal emails from our team members"), and the system prompt updates accordingly.
- **End**: Jacob tests the updated agent, which correctly identifies a test email from an internal source as "high priority." He concludes by highlighting the simplicity of the process and invites viewers to try it for free at langsmith.com.

## Key Insights
- **No-Code Development**: The core value is empowering non-technical users to build powerful AI agents.
- **Conversational Setup**: The building process is like a conversation, where the system actively asks questions to clarify requirements, significantly lowering the barrier to entry.
- **Real-time Feedback and Iteration**: Users can modify the agent's behavior with simple natural language commands, and the system instantly updates its core logic (the system prompt), making adjustments intuitive.
- **Transparency and Control**: The interface clearly displays the agent's configuration, tools, and triggers. It also features a toggle to "require tool approval," giving the user full control over the agent's actions during testing.
- **Built for Practical Applications**: The tool is designed to solve real-world problems, such as the email assistant, which can handle practical tasks like categorization, prioritization, summarization, and drafting replies.

## Notable Moments
- During the demo, Jacob admits the test result is "a little bit hokey" because he cleared out his inbox beforehand, leaving only a single test email he sent to himself.
- The most impressive moment is when the agent's priority logic is changed from "external customers" to "internal team members" with a simple, conversational command.
- The initial pre-built prompt, "Create an AI email assistant," shows how the tool can quickly start working towards a well-defined goal.
