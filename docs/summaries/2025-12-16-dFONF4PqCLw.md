# I Let an AI Control My Browser to Play Tic-Tac-Toe - LangChainJS Tutorials

**Channel:** LangChain
**Published:** 2025-12-16
**Video:** [Watch on YouTube](https://youtube.com/watch?v=dFONF4PqCLw)

---

# [在 LangChain.js 中使用原生工具讓 AI 玩井字遊戲]

## 重點摘要
這部影片介紹了 LangChain.js 的最新更新，它讓開發者能輕易地整合大型語言模型供應商（如 Anthropic）提供的「原生工具」。影片透過一個實際範例，展示如何讓 AI 控制瀏覽器，與人類玩井-字遊戲（Tic-Tac-Toe），並利用記憶工具從錯誤中學習，逐步提升棋藝。

## 故事大綱
- **開場**：影片主講人 Christian 首先介紹 LLM 供應商現在提供許多「原生工具」（如網頁搜尋、電腦控制），而 LangChain 的新套件讓使用者可以無縫、型別安全地使用這些工具，不需手動編寫 JSON schemas。他預告將展示一個 AI 使用 Anthropic 的電腦控制工具來玩井字遊戲。
- **中段**：Christian 解釋原生工具有兩種類型：一種在供應商端執行（如網頁搜尋），另一種則在使用者應用程式中執行（如電腦控制）。他展示了如何簡單地為 agent 加入網頁搜尋能力。接著，他詳細介紹井字遊戲的專案設定：使用 `computer_use` 工具連接 `webdriver.io` 來控制瀏覽器點擊，並加入 `memory` 工具讓 AI 記錄遊戲歷程、策略和錯誤。為了避免螢幕截圖佔滿 context window，他還使用了一個中介軟體來清除舊的截圖。
- **結尾**：在實際對戰中，AI 第一局犯了明顯錯誤而輸掉遊戲。賽後，AI 自動使用記憶工具分析：「我未能識別到列的威脅」。在第二局遊戲中，當同樣的局面出現時，AI 成功擋住了攻勢，最終該局以平手收場。Christian 總結，這展示了模型如何透過工具從經驗中學習並進步，並鼓勵觀眾查看 GitHub 上的完整範例程式碼。

## 關鍵見解
1.  **原生工具整合**：LangChain.js 的新 `tools` 元件，讓開發者能極其簡便地使用 Anthropic、OpenAI 等供應商提供的原生、模型優化過的工具。
2.  **工具組合的威力**：透過結合不同的工具（如用於操作的 `computer_use` 和用於學習的 `memory`），可以創造出更複雜、更智能的代理人（agent）。
3.  **從經驗中學習**：AI 能利用記憶工具記錄並分析過去的互動，從而改進其未來表現。影片中的 AI 從輸棋中學到教訓，並在下一局成功防守。
4.  **Context 管理的重要性**：在處理像螢幕截圖這樣的大量資料時，必須有效管理模型的 context window，例如透過清除舊的工具輸出來避免溢位。
5.  **模型即行動驅動者**：對於 `computer_use` 這類工具，模型負責決定「做什麼」（例如，點擊某個座標），而使用者的程式碼則負責「如何做」（例如，執行瀏覽器自動化指令）。

## 精彩時刻
- **AI 玩遊戲**：最吸睛的部分就是看著 AI 實際控制滑鼠指標，在螢幕上的井字遊戲棋盤中下棋。
- **AI 的自我檢討**：第一局輸掉後，AI 在筆記中準確地寫下自己的關鍵失誤：「在我方下了右上角後，對手已有右下角，我卻未能識別出同一列的威-脅。」
- **學習成果的展現**：在第二局遊戲中，AI 面對同樣的致勝陷阱時，成功地進行了防守，證明了它從上一局的失敗中學到了東西。
- **最終結果**：主講人提到，在多玩幾局之後，後續的遊戲全都以平手告終，顯示 AI 已經掌握了井字遊戲的最佳策略。

---

# [Using Native Tools in LangChain.js to Play Tic-Tac-Toe]

## TL;DR
This video demonstrates how the latest LangChain.js updates make it simple to integrate "native tools" from LLM providers like Anthropic. Through a live demo, an AI is shown controlling a web browser to play Tic-Tac-Toe against a human, using a memory tool to learn from its mistakes and improve its gameplay over time.

## Story Flow
- **Beginning**: Christian from LangChain introduces the concept of native provider tools (like web search or computer control) and explains that new LangChain packages allow seamless, type-safe use of them without manual glue code. He sets up the demo: an AI playing Tic-Tac-Toe using Anthropic's computer use tool.
- **Middle**: Christian explains the two types of native tools: those executed on the provider's side (e.g., web search) and those implemented in the user's app (e.g., computer use). He shows how easily web search can be added to an agent. He then details the Tic-Tac-Toe project, which uses the `computer_use` tool hooked to `webdriver.io` for browser clicks and a `memory` tool for the AI to record game history, strategies, and mistakes. A middleware is also used to clear old screenshots to manage the context window.
- **End**: In the live game, the AI makes a critical error in the first round and loses. Afterward, it uses the memory tool to analyze its mistake, noting, "I didn't recognize the column threat." In the second game, facing the same scenario, the AI successfully blocks the move, resulting in a draw. Christian concludes by highlighting how models can learn and improve from experience with these tools and points viewers to the full code on GitHub.

## Key Insights
1.  **Native Tool Integration**: LangChain.js's new `tools` primitive makes it incredibly easy to use native, model-optimized tools from providers like Anthropic and OpenAI.
2.  **The Power of Tool Combination**: By combining different tools (like `computer_use` for action and `memory` for learning), developers can create sophisticated and intelligent agents.
3.  **Learning from Experience**: The AI can use a memory tool to record and analyze past interactions, thereby improving its future performance. The agent in the video learned from a loss to defend correctly in the next game.
4.  **Importance of Context Management**: When dealing with rich data like screenshots, it's crucial to manage the model's context window effectively, for instance, by clearing old tool outputs to prevent overflow.
5.  **Model as the Action-Decider**: With tools like `computer_use`, the model decides *what* to do (e.g., click specific coordinates), while the user's code is responsible for *how* to do it (e.g., executing the browser automation command).

## Notable Moments
- **The AI Plays the Game**: The most engaging part is watching the AI literally control the mouse cursor to place its moves on the Tic-Tac-Toe board on screen.
- **The AI's Self-Critique**: After losing the first game, the AI accurately identifies its critical mistake in its notes: "After [I] took top right... I didn't recognize the column threat."
- **Demonstrating Learning**: In the second game, the AI successfully defends against the exact same winning trap it fell for previously, proving it learned from its failure.
- **The Final Outcome**: The presenter mentions that after playing a few more rounds, all subsequent games ended in a draw, indicating the AI had learned the optimal strategy for Tic-Tac-Toe.
