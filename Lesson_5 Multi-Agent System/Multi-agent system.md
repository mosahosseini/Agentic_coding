### **Lesson 5: Multi-Agent Systems (AutoGen, CrewAI)**  
- **Topics:**  
  - Role-based agents (e.g., "Researcher," "Summarizer")  
  - Agent collaboration (chat, function calling)  
- **Exercise:**  
  - Create a team of agents that research and summarize a topic.  
- **Tools:**  
  - [Microsoft AutoGen](https://microsoft.github.io/autogen/)  
  - [CrewAI](https://crewai.com/)  

A Multi-Agent System (MAS) is a system composed of multiple autonomous agents that:

* Perceive their environment,

* Make decisions,

* Interact with other agents and the environment.



---

## 🔥 What Are Role-Based Agents? (General Definition)

**Role-based agents** are:

> **Autonomous agents in a multi-agent system that are assigned specific roles defining their behavior, responsibilities, goals, and interaction patterns within the system.**

---

### Why Assign Roles?

* **Structure & Organization:** Helps organize the system by distributing different responsibilities.
* **Specialization:** Each agent focuses on a defined subset of tasks, improving efficiency.
* **Coordination:** Roles help agents know *how* to interact with others, who to listen to, and when to act.
* **Scalability:** Easier to add, remove, or replace agents without disrupting the whole system.

---

### Example from Real World

Think of a **soccer team**:

| Role       | Behavior & Responsibility       |
| ---------- | ------------------------------- |
| Goalkeeper | Defends the goal                |
| Defender   | Stops opposing attackers        |
| Midfielder | Controls ball flow and strategy |
| Forward    | Scores goals                    |

Each player (agent) knows what to do based on their role, and the team works together.

---

### How Roles Are Used in Multi-Agent Systems

* **Task allocation:** Assign different subtasks to different agents based on roles.
* **Communication protocols:** Agents follow role-specific communication rules.
* **Behavior control:** Roles determine which actions agents can or should perform.
* **Decision making:** Role affects agent priorities and planning strategies.

---

### Formal Definition (from MAS literature)

> A **role** in MAS is a set of expected behaviors and responsibilities that an agent may adopt to fulfill a part of the system’s overall goal.

Roles are often defined as tuples or structures containing:

* **Permissions:** Actions allowed
* **Obligations:** Actions required
* **Norms:** Rules governing behavior
* **Interaction protocols:** How roles communicate or negotiate

---
| Role          | Description                      | Example Task                               |
| ------------- | -------------------------------- | ------------------------------------------ |
| 🧠 Researcher | Gathers and analyzes data        | “Find the 5 newest LLM papers on ArXiv”    |
| ✍️ Writer     | Translates info into blog format | “Write blog post from research findings”   |
| 🧑‍⚖️ Editor  | Reviews for quality + tone       | “Proofread and fix clarity and citations”  |
| 📊 Analyst    | Breaks down business data        | “Summarize customer churn rates by region” |
| 👩‍💼 PM      | Plans tasks, prioritizes output  | “Organize subtasks and set deadlines”      |
----


### Why roles matters.

| Without Roles                | With Roles                      |
| ---------------------------- | ------------------------------- |
| 🤖 Generic, weak reasoning   | 🧠 Purpose-driven reasoning     |
| 🤷 Doesn’t “know” who it is  | 🎭 Understands its identity     |
| 🐌 May stall or go off-track | 🎯 Focuses tightly on its task  |
| 🤝 Bad collaboration         | 🤝 Agents cooperate effectively |
| 🧩 Hard to scale complexity  | 🧱 Easy to build expert teams   |


Roles help the LLM simulate expert behavior, improving:

* Accuracy

* Coherence

* Collaboration

* Scalability

--- 

### 🧠 Tip: Roles Can Be Creative

You can go beyond simple job titles. For example:

* "🧙 Prompt Alchemist" → expert in LLM prompt tuning

* "🎨 Visual Thinker" → only communicates via diagrams

* "🕵️ Truth Enforcer" → fact-checks and cross-verifies all info

The stronger the persona, the better the agent's performance.