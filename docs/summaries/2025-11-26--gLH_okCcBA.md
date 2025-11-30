# AI Agents in Production: Lessons from Rippling and LangChain

**Channel:** LangChain
**Published:** 2025-11-26
**Video:** [Watch on YouTube](https://youtube.com/watch?v=-gLH_okCcBA)

---

# LangChain 與 Rippling 的爐邊對談：深入探討企業級 AI Agent 的實戰與未來

## 重點摘要
Rippling 的 AI 主管 Anker 分享了他們從簡單的 AI 功能演進到複雜 Agent 的實戰歷程。他們發現，成功的關鍵是從僵硬、確定性的工作流程，轉向更能應對真實世界複雜性的「深度 Agent」範式，並強調快速迭代、強大的使用者回饋循環（內部測試）以及建立可重用的 AI 基礎設施是成功的核心。

## 故事大綱
- **開場**：LangChain 的 CEO Harrison 介紹了這次與 Rippling AI 主管 Anker 的爐邊對談，旨在深入了解 Rippling 在企業內部建構與部署 AI Agent 的真實經驗。

- **中段**：Anker 闡述了 Rippling 的 AI 發展三部曲：從初期的內容摘要，到開發獨立的 AI 產品（如 Talent Signal），再到目前專注的 Agent 系統。他深入探討了將 AI 從原型推向產品的挑戰，包括擁抱實驗文化、使用真實數據驗證，以及建立極為重要的使用者回饋循環（Rippling 內部全員測試，稱為「吃自己的狗食」）。對談的核心逐漸轉向 Agent 開發的典範轉移：他們最初嘗試確定性的、按領域劃分的 Agent，但發現效果不佳，因為人類的提問充滿模糊性；現在，他們轉向「深度 Agent」範式，給予 LLM 一系列工具和目標，讓其自主推理，取得了更驚喜的成果。

- **結尾**：對談展望了 Agent 的未來，認為結合兩者優點的混合模式是方向——將高度可靠的「工作流程」封裝成「工具」，供靈活的 Agent 調用。最後的 Q&A 環節則涵蓋了資安隱私、如何應對 AI 產生的劣質內容（AI Slop）、以及如何有效管理大量工具等實務問題。

## 關鍵見解
1.  **Agent 典範轉移**：趨勢正從僵硬、確定性的「工作流程導向」Agent，轉向更靈活、能處理現實世界邊緣案例的「深度 Agent」。後者更依賴 LLM 的推理能力，而非試圖強迫其遵循預設路徑。
2.  **回饋循環至上**：成功部署 AI 的關鍵在於建立一個快速、真實的使用者回饋循環。Rippling 透過內部「吃狗食」(dogfooding) 的方式，讓從 CEO 到基層員工親自測試並提供直接反饋，這是改進產品最有效的方法。
3.  **基礎建設是加速器**：建立一個包含數據層、Agent 層（如 LangChain）、評估系統等的「鋪平道路」(paved path)，能讓各產品團隊快速創新，而不用重複造輪子。AI 核心團隊的角色是與產品團隊共同建構，並從中提煉出可重用的基礎設施。
4.  **工作流程即工具**：過去被視為 Agent 核心的確定性工作流程，現在更適合被看作是 Agent 可以調用的「可靠工具」。這在需要執行精確、有交易性（如修改薪資）的動作時尤其重要，能兼顧準確性與 Agent 的靈活性。
5.  **擁抱實驗文化**：AI 開發與傳統軟體工程不同，充滿不確定性。團隊必須接受「某些實驗會失敗」的心態，並專注於從中學習和快速迭代。

## 精彩時刻
- **CEO 親自下場測試**：Anker 提到，Rippling 的 CEO Parker Conrad 親自擔任系統的超級管理員，積極測試 Agent 並直接在 Slack 上提供「殘酷或美好」的回饋。
- **AI 的究極責任制**：在討論 AI 產生劣質程式碼 (AI Slop) 的問題時，Rippling 的原則是：「AI 是你的超能力，但你仍需為你提交到生產環境的程式碼負全責。」
- **工具的「漸進式揭露」**：在管理大量工具時，一個有趣的想法是「漸進式揭露」(progressive disclosure)，意即 Agent 不需要一開始就知道所有工具，而是在需要時才動態去「發現」和學習如何使用它們。

---

# Fireside Chat with LangChain & Rippling: Building & Deploying Enterprise AI Agents in the Real World

## TL;DR
Rippling's Head of AI, Anker, shares their practical journey evolving from simple AI features to complex agents. They've found success by moving from rigid, deterministic workflows to a "deep agent" paradigm that better handles real-world complexity, emphasizing that rapid iteration, robust user feedback loops (dogfooding), and building foundational AI primitives are core to their success.

## Story Flow
- **Beginning**: LangChain's CEO, Harrison, introduces the fireside chat with Anker, Head of AI at Rippling, to dive into Rippling's real-world experience building and deploying AI agents within an enterprise.

- **Middle**: Anker outlines Rippling's three-stage AI evolution: starting with content summarization, moving to standalone AI products (like Talent Signal), and now focusing on agents. He details the challenges of moving from prototype to production, including embracing an experimental culture, using real data for validation, and the critical importance of a user feedback loop (achieved through company-wide "dogfooding"). The conversation pivots to a paradigm shift in agent development: they initially tried deterministic, domain-specific agents but found them brittle against the ambiguity of human questions. They are now seeing more surprising and successful results with a "deep agent" paradigm, which gives the LLM tools and lets it reason its way to a solution.

- **End**: The discussion looks to the future of agents, suggesting a hybrid model is the path forward—encapsulating highly reliable "workflows" as "tools" for a flexible agent to call. The final Q&A session covers practical topics like security/privacy, handling AI-generated "slop," and effectively managing a large number of tools.

## Key Insights
1.  **Paradigm Shift in Agents**: The trend is moving from rigid, deterministic, "workflow-centric" agents to more flexible "deep agents" that can handle real-world edge cases by relying on the LLM's reasoning capabilities rather than forcing it down a predefined path.
2.  **The Feedback Loop is King**: The key to successfully deploying AI is a fast, authentic user feedback loop. Rippling's internal "dogfooding," where everyone from the CEO down tests products and gives direct feedback, is the most effective way to iterate and improve.
3.  **Infrastructure as an Accelerator**: Creating a "paved path" with a data layer, agent layer (e.g., LangChain), and evaluation systems allows product teams to innovate quickly without reinventing the wheel. The core AI team's role is to co-build with product teams and extract reusable primitives from that process.
4.  **Workflows as Tools**: Deterministic workflows, once seen as the core of an agent, are now better viewed as reliable "tools" that an agent can call. This is especially crucial for transactional actions (e.g., modifying payroll) that require precision, balancing accuracy with the agent's flexibility.
5.  **Embrace the Experimental Culture**: AI development is not like traditional software engineering; it's inherently uncertain. Teams must adopt a mindset that accepts that "some experiments will not work" and focus on learning and iterating quickly.

## Notable Moments
- **CEO as a Super-User**: Anker mentioned that Rippling's CEO, Parker Conrad, actively acts as a system super-admin, personally testing agents and giving "brutal or good" feedback directly on Slack.
- **Ultimate Accountability for AI**: When discussing "AI slop" (poor-quality AI-generated code), Rippling's principle is: "AI is your superpower, but you are still accountable for the code you're pushing to production."
- **"Progressive Disclosure" of Tools**: An interesting idea for managing many tools is "progressive disclosure," where an agent doesn't need to know about all tools upfront but dynamically "discovers" and learns to use them as needed.
