# How I built an AI agent to automate my emails with LangSmith Agent Builder

**Channel:** LangChain
**Published:** 2026-01-13
**Video:** [Watch on YouTube](https://youtube.com/watch?v=bzcAZJTxOrs)

---

# 使用 Langsmith Agent Builder 設定無程式碼 AI 郵件助理

## 重點摘要
本影片教學如何使用 Langsmith 的無程式碼 Agent Builder，設定、修改並監督一個能代為讀取和回覆郵件的 AI 助理。其核心特色是透過事件（如收到新郵件）自動觸發，並設有「真人審核」機制，讓使用者在 AI 執行關鍵操作前回顧與批准，實現安全又自主的自動化。

## 故事大綱
- **開場：** 影片開頭直接點明目標——建立一個無程式碼的郵件助理。講者從 Langsmith 的範本頁面選擇「Email Assistant」範本，並引導觀眾完成 Google 帳號授權，賦予助理讀取 Gmail 和行事曆的權限。
- **中段：** 核心內容是設定與客製化助理。講者解釋了「觸發器」（Trigger）如何讓助理在背景中因收到郵件而自動運作。接著，他展示了如何檢視助理的工具箱（如寄信、讀取郵件），並特別強調「暫停執行」功能，確保助理在寄信或建立會議等對外操作前，會等待使用者批准。最關鍵的展示是，使用者可以直接用自然語言（聊天）來修改助理的指令，例如要求它「標記所有來自同事的郵件」，系統會自動更新設定檔。
- **結尾：** 影片最後展示如何監督運作中的助理。透過「Feed」介面，使用者可以看到所有 AI 的活動紀錄，並處理需要真人決策的任務，例如回答助理提出的問題（「這封信重要嗎？」）或批准它更新記憶（「記住以後忽略這類通知」）。講者總結，這個強大的工具整合了記憶、觸發器、技能和子代理等多種技術，並鼓勵觀眾親自體驗。

## 關鍵見解
1.  **無程式碼實現 AI 自動化：** 無需撰寫任何程式碼，即可建立、客製化並部署功能強大的 AI 代理人。
2.  **觸發器驅動的自主運作：** 助理由特定事件（如收到郵件）觸發，在背景中自主運行，無需手動啟動。
3.  **真人審核機制確保安全：** 對於傳送郵件、建立行事曆邀請等關鍵操作，系統會暫停並等待使用者批准，兼顧了自動化效率與人工監督的安全性。
4.  **自然語言即時修改配置：** 可以直接透過聊天下指令來修改助理的核心行為，讓客製化過程極為直觀。
5.  **持續學習的代理人記憶：** 助理會根據使用者的回饋（例如「忽略這類信件」）來學習並更新自己的行為模式，變得越來越聰明。

## 精彩時刻
- 「你可以僅僅使用自然語言就修改代理人的任何部分。」（You can modify any part of the agent just by using natural language.）—— 這點凸顯了其易用性的強大之處。
- 助理會主動提問並提供選項，例如：「這封信看起來像垃圾郵件，我該怎麼處理？[選項A: 標為已讀] [選項B: 以後自動標為已讀]」，讓使用者能輕鬆地訓練它。
- 整個過程——從建立範本、連接帳號、設定觸發器到透過聊天介面進行監督——流暢地展示了一個完整、安全且實用的 AI 助理工作流程。

---

# Setting Up a No-Code AI Email Assistant with Langsmith Agent Builder

## TL;DR
This video demonstrates how to use Langsmith's no-code Agent Builder to set up, modify, and supervise an AI assistant that can read and respond to emails on your behalf. The core features are its ability to run autonomously via triggers (like a new email) and a "human-in-the-loop" approval process for key actions, ensuring safe and supervised automation.

## Story Flow
- **Beginning:** The video starts by defining the goal: to build a no-code email assistant. The presenter navigates to the Langsmith templates page, selects the "Email Assistant" template, and connects a Google account to grant it the necessary permissions for Gmail and Calendar.
- **Middle:** The main part of the video focuses on configuring and customizing the agent. The presenter explains how a "trigger" allows the assistant to run autonomously in the background upon receiving an email. He then shows how to view the agent's toolbox (e.g., send email, read messages) and emphasizes the "pause before executing" feature, which requires user approval before the agent sends an email or creates a calendar event. Crucially, it's shown that the agent's instructions can be modified simply by chatting with it in natural language, such as telling it to "always flag emails that are from other LangChain employees," which automatically updates its configuration files.
- **End:** The video concludes by showing how to supervise the running agent. Through the "Feed," the user can see all AI activities and handle items requiring human intervention, such as answering questions the agent asks ("Is this email important?") or approving its requests to update its memory ("Remember to ignore these notifications in the future"). The presenter summarizes that this powerful tool combines memory, triggers, skills, and sub-agents, and encourages viewers to try it.

## Key Insights
1.  **No-Code AI Automation:** You can build, customize, and deploy powerful AI agents without writing any code.
2.  **Trigger-Based Autonomy:** The assistant is driven by events (like an incoming email) and operates autonomously in the background without needing manual initiation.
3.  **Human-in-the-Loop for Safety:** Critical actions, like sending emails or calendar invites, are paused for user approval, balancing automation with secure human oversight.
4.  **Configuration via Natural Language:** You can modify the agent's core behavior just by giving it commands in a chat interface, making customization incredibly intuitive.
5.  **Persistent Memory and Learning:** The assistant learns from user feedback (e.g., "ignore these types of emails") to adapt and improve its behavior over time, becoming progressively smarter.

## Notable Moments
- "You can modify any part of the agent just by using natural language." - This highlights the incredible ease of use.
- The agent proactively asks questions with suggested options, such as: "This email looks like spam, how should I handle it? [Option A: Mark as read] [Option B: Automatically mark as read in the future]," making it easy for the user to train it.
- The entire workflow—from creating the template, connecting accounts, setting triggers, to supervising through a feed—smoothly demonstrates a complete, safe, and practical AI assistant in action.
