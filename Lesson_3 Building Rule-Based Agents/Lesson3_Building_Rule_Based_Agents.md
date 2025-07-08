### **Lesson 3: Building Rule-Based Agents**  
- **Topics:**  
  - Finite State Machines (FSMs) for decision-making  
  - Simple chatbots with `Rasa` or `Dialogflow`  
- **Exercise:**  
  - Code a FAQ bot that answers questions based on rules.  
- **Tools:**  
  - [Rasa Open Source](https://rasa.com/docs/rasa/)  

---


Here's a clear explanation of both concepts:

---

## 🔸 Finite State Machines (FSMs) for Decision-Making

A **Finite State Machine (FSM)** is a mathematical model used to design logic-based systems that **respond to inputs by transitioning between a fixed number of states**.

### 🔧 Key Concepts:

* **States**: Conditions the system can be in (e.g., `Idle`, `Asking`, `Responding`, `Ending`).
* **Transitions**: Rules that determine when the system moves from one state to another (e.g., when a user says “hello,” move from `Idle` to `Greeting`).
* **Events/Inputs**: External inputs that trigger transitions (e.g., button clicks, text input).
* **Actions**: What the system does when entering or exiting a state (e.g., displaying a message).

### ✅ Why use FSMs for decision-making?

* They **model predictable workflows** (like menus, command sequences).
* They **enforce logical structure**, making debugging easier.
* They're used in **games, UI design, robotic movement**, and **basic chatbots**.

### 🧠 Example (Chatbot FSM):

```text
States: Start → AskName → Greet → End

If input == "Hi" → move to AskName
If name is given → move to Greet
Then → End
```

FSMs are especially useful for **non-learning bots** where you want full control over the conversation flow.

---

## 🔸 Simple Chatbots with `Rasa` or `Dialogflow`

### 🛠️ **Rasa**:

* **Open-source** chatbot framework based on **NLU (natural language understanding)**.
* Lets you create **intelligent, customizable chatbots**.
* You define:

  * **Intents** (what users want to do)
  * **Entities** (extracted data like dates or names)
  * **Stories** (dialogue paths like FSMs)
* Can run locally (privacy-focused).
* Highly flexible and integrates well with Python.

**Example flow:**

```yaml
User: "Book a flight to Paris"
→ Intent: book_flight
→ Entity: destination=Paris
→ Action: ask for travel date
```

---

### 🛠️ **Dialogflow** (by Google):

* **Cloud-based NLP chatbot builder**.
* Uses **Google's pre-trained models** to classify intent and respond.
* Easy to set up and integrate with **Google Assistant**, **Messenger**, etc.
* Less customizable than Rasa, but faster for simple bots.

**Example flow:**

* User: "I want pizza"
* Dialogflow recognizes intent: `order_food`
* Responds with a fulfillment message or web hook

---

## ✅ Summary Comparison

| Feature         | FSM                 | Rasa                  | Dialogflow               |
| --------------- | ------------------- | --------------------- | ------------------------ |
| Type            | Rule-based logic    | ML-based NLU          | Cloud NLU (Google-based) |
| Control         | Full control        | Medium (customizable) | Lower (black-box)        |
| Offline support | Yes                 | Yes                   | No                       |
| Scalability     | Low (manual growth) | High                  | High                     |
| Learning curve  | Low–Medium          | Medium–High           | Low                      |

---

Let me know if you want a code example for FSM in Python or want to set up a basic Rasa/Dialogflow bot!
