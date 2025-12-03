# Building a Market Research Assistant with Langsmith Agent Builder

**Channel:** LangChain
**Published:** 2025-12-03
**Video:** [Watch on YouTube](https://youtube.com/watch?v=2GeTGEVyPfo)

---

# 使用 LangSmith Agent Builder 在幾分鐘內打造無程式碼的研究助理

## 重點摘要
LangSmith Agent Builder 現已進入公開測試版，它讓使用者能透過聊天介面，無需編寫任何程式碼，即可打造並部署生產級別的 AI 代理人。影片展示了如何快速建立一個客製化的市場研究助理，該助理能自動執行每週研究並將報告發送到 Slack。

## 故事大綱
- **開場**：影片由 LangChain 的 Jacob 開始，他宣布 LangSmith Agent Builder 進入公開測試階段，並說明這是一個無需編寫程式碼即可建立代理人的工具。他提議在幾分鐘內現場建立一個市場研究助理來展示其功能。
- **中段**：Jacob 提供一個簡單的初始指令，Agent Builder 隨即提出一連串澄清問題，以定義代理人的具體任務：研究主題（技術趨勢、公司動態）、執行頻率（每週一次）以及結果交付方式（透過 Slack）。接著，Jacob 透過後續的聊天指令進一步微調代理人的行為，要求它將結果限制為最重要的三項。設定完成後，他啟動了一次測試運行。
- **結尾**：代理人在背景執行了大量的研究後，將一份格式精美的摘要（包含三則最重要的產業新聞）直接發送到指定的 Slack 頻道。Jacob 最後邀請觀眾親自到 langsmith.com 免費試用這個工具。

## 關鍵見解
1. **無程式碼代理人創建**：平台的核心價值在於讓非開發者也能使用自然語言，透過對話式介面來建構複雜、自主的 AI 代理人。
2. **迭代式開發與微調**：使用者無需一開始就提供完美的指令。可以從一個模糊的想法開始，然後透過後續的對話與反饋，逐步完善代理人的行為與產出。
3. **工作流程自動化**：代理人可以被設定為按計畫（例如每週）自動運行，並將報告發送到 Slack 等日常工作平台，從而無縫地簡化資訊收集流程。
4. **智慧化的代理人結構**：系統會根據任務需求，自動設計出高效的代理人架構，例如建立一個主監督者和多個配備專用工具（如網路搜尋）的專業化子代理人。
5. **使用者控制與除錯**：平台內建了除錯模式，允許使用者在測試階段監控代理人的行為，並可設定手動批准工具的使用，確保了開發過程中的可見性與控制權。

## 精彩時刻
- **「啊哈！」時刻**：當一個簡單的指令「建立一個市場研究助理」觸發 Agent Builder 提出一系列智慧化的澄清問題時，展現了其強大的理解能力。
- **即時反饋迴圈**：僅用一句話「每週只給我你找到的前三項」，就立即更新了代理人的核心系統指令，操作非常直觀。
- **具體的最終成果**：最終在 Slack 中收到的那份簡潔、專業的自動化報告，將這個工具的實用價值具象化，令人印象深刻。

---

# Building a No-Code Research Agent in Minutes with LangSmith Agent Builder

## TL;DR
LangSmith Agent Builder is now in public beta, enabling anyone to build and deploy production-grade AI agents through a chat-based interface with no coding required. The video demonstrates creating a custom market research assistant that automates weekly reporting directly to Slack.

## Story Flow
- **Beginning**: Jacob from LangChain introduces the public beta of LangSmith Agent Builder, a tool for creating agents without code. He sets out to build a market research assistant live in just a few minutes to showcase its capabilities.
- **Middle**: Jacob provides a simple initial prompt. The Agent Builder responds with clarifying questions to define the agent's task: what to research (tech trends, companies), how often (weekly), and where to deliver the results (Slack). He then refines the agent's behavior with a follow-up chat command to limit the output to the top three results and initiates a test run.
- **End**: After performing extensive background research, the agent delivers a perfectly formatted summary of the top three industry news stories directly to a Slack channel. Jacob concludes with a call to action for viewers to try the tool for free at langsmith.com.

## Key Insights
1. **No-Code Agent Creation**: The platform's main feature is the ability to construct complex, autonomous agents using natural language, removing the need for programming skills and making it accessible to a wider audience.
2. **Iterative Development**: Users can start with a vague idea and iteratively refine the agent's instructions and behavior through a conversational feedback loop, rather than needing a perfect prompt upfront.
3. **Workflow Automation**: Agents can be scheduled to run automatically and deliver reports to common workplace tools like Slack, streamlining information gathering and integrating into existing workflows.
4. **Intelligent Agent Composition**: The system automatically designs an effective agent structure, creating specialized sub-agents (e.g., for company research, technical trends) and equipping them with the right tools (e.g., web search) to perform their tasks.
5. **Control and Debugging**: A built-in debug mode allows users to monitor the agent's actions and require manual approval for tool use, ensuring control and visibility during the testing and development phase.

## Notable Moments
- **The "Aha!" Moment**: The initial, simple prompt ("create a market research assistant") kicking off an intelligent, clarifying conversation with the Agent Builder is a powerful demonstration of its capabilities.
- **The Direct Feedback Loop**: The ease of refining the agent's core instructions with a single, natural sentence: "only give me the top three items you find each week."
- **The Tangible Result**: The final Slack message is a polished, practical, and fully automated output, making the tool's value proposition concrete and easy to understand.
