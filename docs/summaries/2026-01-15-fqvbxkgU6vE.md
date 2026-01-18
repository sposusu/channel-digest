# Choosing the Right Multi-Agent Architecture

**Channel:** LangChain
**Published:** 2026-01-15
**Video:** [Watch on YouTube](https://youtube.com/watch?v=fqvbxkgU6vE)

---

# 如何選擇多代理人（Multi-Agent）架構

## 重點摘要
LangChain 的 Sydney 解釋了四種多代理人架構（子代理人、交接、技能、路由器），並根據四個標準（分散式開發、平行處理、多跳對話支援、使用者直接互動）進行評分。核心結論是，應從單一代理人開始，只有在任務變得極度複雜時，才考慮使用多代理人系統。

## 故事大綱
- **開場**：影片以一個重要的警告開始：你可能並不需要多代理人模式。許多任務透過一個設計精良的單一代理人就能解決。接著，講者介紹了用來評估不同架構的四個核心標準。
- **中段**：講者依序詳細介紹了四種主要的架構模式：
    1.  **子代理人（Supervisor）**：一個主代理人將其他子代理人作為工具來調度。此模式有利於分散式開發和平行處理，但在與使用者直接互動方面表現較差。
    2.  **交接（Handoffs）**：代理人之間可以互相交接控制權。此模式在多跳對話和使用者直接互動方面表現最佳，但在分散式開發上較為困難。
    3.  **技能（Skills）**：一個單一代理人根據需要動態載入特定技能（知識）。此模式在分散式開發、多跳對話和使用者互動上都表現優異，但在平行處理上略有折扣。
    4.  **路由器（Router）**：一個路由器將輸入導向給最適合的代理人。此模式最擅長平行處理，但在多跳對話方面幾乎為零分，因為它不適合連續性任務。
- **結尾**：講者展示了一張總結所有架構與評分的表格，並再次強調最重要的原則：「從簡單開始」。隨著問題的複雜性增加，才逐步擴展你的系統。

## 關鍵見解
1.  **非必要不使用多代理人**：在考慮複雜的多代理人系統之前，先確認一個擁有良好工具的單一代理人是否無法完成任務。
2.  **依需求選擇架構**：「交接」模式最適合需要與使用者進行深度、多步驟對話的場景。
3.  **分散式開發的首選**：「子代理人」和「技能」模式非常適合讓不同團隊獨立開發和維護各自負責的代理人或功能。
4.  **為平行而生的路由器**：「路由器」模式的核心優勢是能夠將任務分配給多個代理人同時處理，但犧牲了對話的連續性。
5.  **沒有完美的架構**：每種模式都有其取捨。例如，「交接」模式犧牲了開發獨立性以換取高度的互動性；「路由器」模式則犧牲了對話能力以換取高效率的平行處理。

## 精彩時刻
- 開場的直接警告：「我首先想提醒你。你可能並不需要為你的系統設計一個多代理人模式。」
- 「漸進式揭露」（Progressive Disclosure）：在「技能」模式中提到的一個概念，指代理人只在需要時才載入相關知識，這是一種越來越受歡迎的上下文管理策略。
- 最終的黃金法則：「這裡最重要的事情或許是——從簡單開始。」

---

# How to Choose a Multi-Agent Architecture

## TL;DR
Sydney from LangChain explains four multi-agent architectures (Sub-agents, Handoffs, Skills, Router) and evaluates them against four criteria: distributed development, parallelization, multihop conversational support, and direct user interaction. The core takeaway is to start with a single agent and only adopt a multi-agent pattern when complexity genuinely demands it.

## Story Flow
- **Beginning**: The video starts with a crucial caution: you might not actually need a multi-agent pattern. Many tasks are best handled by a single, well-tooled agent. The speaker then introduces the four criteria for evaluating different architectures.
- **Middle**: The speaker details four primary architectural patterns:
    1.  **Sub-agents (Supervisor)**: A main agent coordinates sub-agents as tools. This pattern excels at distributed development and parallelization but falls short on direct user interaction.
    2.  **Handoffs**: Agents can hand off control to one another. This pattern is the best for multihop conversations and direct user interaction but makes distributed development difficult.
    3.  **Skills**: A single agent loads specialized prompts and knowledge (skills) on demand. This pattern scores high on distributed development, multihop, and user interaction, with a slight compromise on parallelization.
    4.  **Router**: A routing step directs input to one or more specialized agents. This pattern is best for parallelization but scores zero for multihop conversations, as it's not suited for sequential tasks.
- **End**: The speaker presents a summary table with all the scores and reiterates the most important principle: "Start simple." Build up from there as your problem gets more complex.

## Key Insights
1.  **Don't Use Multi-Agent Unless Necessary**: Before building a complex multi-agent system, confirm that a single agent with well-designed tools can't do the job.
2.  **Choose an Architecture for Your Needs**: The "Handoffs" pattern is the best choice for scenarios requiring deep, multi-step conversations with the user.
3.  **Best for Distributed Development**: The "Sub-agents" and "Skills" patterns are ideal for allowing different teams to independently own and maintain their respective agents or capabilities.
4.  **Router is for Parallelism**: The "Router" pattern's core strength is dispatching tasks to multiple agents simultaneously, but it sacrifices conversational continuity.
5.  **There Are No Perfect Architectures**: Every pattern involves trade-offs. For example, the "Handoffs" pattern trades development independence for high interactivity, while the "Router" pattern trades conversational ability for efficient parallel processing.

## Notable Moments
- The direct opening caution: "First, I would actually like to caution you. You might not actually need a multi-agent pattern for your system."
- "Progressive Disclosure": A concept mentioned with the "Skills" pattern, where the agent loads knowledge only as needed, described as an "increasingly more popular context management strategy."
- The final golden rule: "Probably the most important thing here is to start simple."
