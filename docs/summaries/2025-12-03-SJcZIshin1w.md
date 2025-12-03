# Building a Linear issue agent with Langsmith Agent Builder

**Channel:** LangChain
**Published:** 2025-12-03
**Video:** [Watch on YouTube](https://youtube.com/watch?v=SJcZIshin1w)

---

# Langsmith Agent Builder 導覽

## 重點摘要
Langchain 推出了 Langsmith Agent Builder 的公開測試版，這是一個讓使用者能以自然語言建立 AI 代理人的平台。影片示範了如何建立一個能監控 Slack 頻道中的錯誤回報、並自動在 Linear 中建立與管理任務的代理人，展現了強大的工作流程自動化能力。

## 故事大綱
- **開場**：Langchain 的產品經理 Sam 介紹了 Agent Builder，並以他團隊實際在用的「Linear 任務管理器」作為主要範例，這個代理人能自動將 Slack 的對話轉為 Linear 的開發任務。
- **中段**：他從頭開始，僅用一段自然語言描述（「我想要一個代理人能監聽 Slack 訊息，並管理我們的 Linear 看板」）來建立一個新代理人。系統中的「代理人創建者」會理解需求、選擇工具，並反問關鍵問題（例如：要用哪個 Linear 團隊、如何區分錯誤和功能請求）來完成設定。設定完成後，Sam 直接在測試介面中對新代理人下指令，成功查詢到 Linear 上的現有任務。
- **結尾**：Sam 展示了團隊在正式環境中使用的代理人如何從一則真實的 Slack 對話中被呼叫，並自動建立 Linear 票證，最後還附上連結回報。他總結時秀出代理人的後台視圖，揭示了它接收訊息、呼叫多個工具、完成工作並回覆的完整思考鏈。

## 關鍵見解
1.  **自然語言創建**：使用者可以透過簡單描述需求來建立代理人，大幅降低了技術門檻。
2.  **互動式設定**：系統中有一個「代理人創建者」，會像助理一樣透過提問來協助使用者完成設定，確保觸發器與工具都正確配置。
3.  **檔案系統即記憶**：代理人的記憶（包含系統提示、工具配置等）是以檔案系統的形式管理的，這代表代理人本身也能夠對其進行修改。
4.  **環境自動化 (Ambient Automation)**：代理人可以在背景中安靜地運行，監控像 Slack 這類的系統並在需要時自動採取行動，不需使用者在聊天視窗中直接互動。
5.  **基於工具的操作**：代理人的核心是透過智慧地選擇和使用一套預先提供的工具（例如 Linear 和 Slack 的 API）來拆解並完成其目標。

## 精彩時刻
- 當「代理人創建者」在收到模糊指令後，能主動反問「要為哪個 Linear 團隊建立任務？」等具體問題時，完美展示了其理解工具需求的智慧。
- 真實世界中的應用範例：團隊成員在 Slack 中簡單說一句：「Linearbot，請建一個 issue」，機器人就立刻完成任務並回覆連結。
- 整個示範在短短幾分鐘內，僅用幾句自然語言，就從無到有建立了一個功能完整的自動化代理人。

---

# A Tour of the Langsmith Agent Builder

## TL;DR
Langchain is launching the Langsmith agent builder in public beta, a platform allowing users to create AI agents with natural language. The demo showcases building an agent that monitors a Slack channel for bug reports and feature requests, then automatically creates and manages issues in Linear, demonstrating powerful workflow automation.

## Story Flow
- **Beginning**: Sam, a Product Manager at Langchain, introduces the agent builder and an example agent his team uses: the "linear issue manager," which automates creating Linear development tickets from Slack messages.
- **Middle**: He demonstrates creating a new agent from scratch by describing its task in natural language ("I want an agent that listens for messages in Slack and manages our Linear board"). An "agent creator agent" understands the request, selects tools, and asks clarifying questions (e.g., which Linear team to use, how to distinguish bugs from features) to finalize the configuration. He then tests the new agent in the chat interface, successfully asking it to list existing issues from Linear.
- **End**: Sam shows the production version of the agent being invoked in a real Slack conversation, where it automatically files a Linear ticket and replies with the link. He concludes by showing the agent's "behind-the-scenes" view, revealing its process of receiving a message, calling multiple tools, and reporting back.

## Key Insights
1.  **Natural Language Creation**: Users can build agents simply by describing what they want them to do, significantly lowering the technical barrier to entry.
2.  **Interactive Configuration**: An "agent creator agent" acts as an assistant, asking follow-up questions to help users correctly configure triggers and tools.
3.  **Memory as a File System**: The agent's memory, including its system prompt and tool configurations, is managed as a file system, which the agent itself can modify.
4.  **Ambient Automation**: Agents can run "ambiently" in the background, monitoring systems like Slack and taking action without needing direct interaction in a chat window.
5.  **Tool-Based Operation**: Agents function by intelligently selecting and using a set of provided tools (like APIs for Linear and Slack) to break down and accomplish their goals.

## Notable Moments
- The "aha!" moment when the "agent creator agent," after receiving a vague instruction, asks specific questions like, "Which Linear team should issues be created in?" This shows it understands the requirements of the tools it has selected.
- The real-world example where a team member simply says in Slack, "Linearbot, please file an issue," and the bot promptly completes the task and responds with a link.
- The entire process of creating a functional, automated agent from scratch was completed in just a few minutes using only natural language.
