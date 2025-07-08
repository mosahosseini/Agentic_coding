
# **Lesson 4: LangChain Fundamentals**  
- **Topics:**  
  - Chains, Agents, Tools, Memory  
  - Retrieval-Augmented Generation (RAG)  
- **Exercise:**  
  - Build a Wikipedia Q&A bot with LangChain.  

### ✅ Lesson Objectives
By the end of this lesson, you will:

- Understand what Chains, Agents, Tools, and Memory are in LangChain.

- Learn how to use Retrieval-Augmented Generation (RAG) to improve LLM responses.

- Be able to build simple chains and use agents with tools and memory.

## What are Chains?
Chains are sequences of calls that combine LLMs with other components. They allow you to pass the output of one step as the input to the next.

```python
from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

llm = OpenAI()
prompt = PromptTemplate(input_variables=["product"], template="What is a good name for a {product}?")
chain = LLMChain(llm=llm, prompt=prompt)

print(chain.run("smartwatch"))
```

## What is memory? 
Memory allows a chain or agent to retain information between interactions. This is crucial for conversations.

```python
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

memory = ConversationBufferMemory()
llm = OpenAI()
conversation = ConversationChain(llm=llm, memory=memory)

print(conversation.run("Hi there!"))
print(conversation.run("What's my name?"))
```

## What are Tools?
Tools are functions an agent can call to perform specific tasks, like web search, math, or API calls.

```py
from langchain.agents import tool

@tool
def multiply(x: int, y: int) -> int:
    """Multiplies two numbers."""
    return x * y
```




Yes — **you are absolutely right**, and your understanding is heading in the right direction. Let’s now go **deep** into how LangChain Memory works under the hood, **what it really does**, and **what trade-offs it introduces**.

---

## 🔍 **1. What Memory *Actually* Does in LangChain**

LangChain’s memory system is not magical — it’s a **prompt management system**.

Every time you run a query like:

```python
response = chain.run("What should I do today?")
```

LangChain:

* Retrieves the **history of the conversation** from memory.
* Injects that history into the prompt template.
* Sends the **entire constructed prompt** to the LLM.
* Updates memory with the new input and output.

In basic memory (like `ConversationBufferMemory`), this means:

```plaintext
Prompt:
The conversation so far:
User: Hi
AI: Hello!
User: My name is Sarah.
AI: Nice to meet you, Sarah!
User: What should I do today?

→ All of this is sent to the LLM every time.
```

---

## 🧮 **2. Implication: Longer Memory = Longer Prompts**

You're absolutely correct:

* Every new message adds to the **total input token count**.
* **More tokens = longer processing time** and **higher cost** (if using paid APIs).
* **Eventually, you will hit the model’s context limit** (e.g., 4k, 8k, or 128k tokens).

So yes: **using full memory with no constraints can hurt performance and cost.**

---

## 🧠 **3. Different Memory Strategies (to Control This)**

LangChain offers several memory types to **balance memory vs efficiency**.

---

### 🪵 A. `ConversationBufferMemory` – Full History

**What it does**: Appends all messages from the start.
**Pros**: Simple, complete.
**Cons**: Grows forever.

---

### 🔍 B. `ConversationBufferWindowMemory` – Last N Messages

**What it does**: Only appends the most recent *k* exchanges.
**Pros**: Keeps things fast and under control.
**Example**:

```python
memory = ConversationBufferWindowMemory(k=5)
```

---

### 📄 C. `ConversationSummaryMemory` – Summarized History

**What it does**: Summarizes earlier conversation to save space.
**How**: Uses the LLM itself to create a concise memory.
**Prompt Example**:

```plaintext
Summary so far:
You met a user named Sarah. She likes music.

New message:
What song should I listen to?
```

**Pros**:

* Keeps context small.
* Keeps “memory” in a way the model can understand.

**Cons**:

* Summary might miss some nuance.
* Slower initially (summarizing takes a few seconds).

---

### 🧠 D. `VectorStoreRetrieverMemory` – Semantic Memory

**What it does**: Stores past inputs/outputs as **embeddings** in a vector DB.
At query time:

* It searches for the most *relevant* past messages.
* Injects only those into the prompt.

**Pros**:

* Smart, efficient memory that doesn’t grow linearly.
* Like having a “searchable brain.”

**Cons**:

* Requires setup of vector DB (e.g., FAISS, Chroma).
* Less deterministic.

---

## ⚖️ **4. Summary of Trade-Offs**

| Memory Type  | Size Grows?     | Fast?      | Memory Limits?        | Ideal Use      |
| ------------ | --------------- | ---------- | --------------------- | -------------- |
| Buffer       | Yes (linearly)  | ✅          | Hits token limit      | Short chats    |
| BufferWindow | No (fixed k)    | ✅✅         | Safe from overloading | Medium chats   |
| Summary      | No (summarized) | ❌ (slower) | Small context         | Long convos    |
| VectorStore  | No              | ✅✅         | Smart filtering       | Knowledge Q\&A |

---

## 🛠️ **5. Best Practice**

If you're building:

* **Short chats** → use `ConversationBufferMemory`
* **Long chats** → use `ConversationSummaryMemory` or `WindowMemory`
* **Knowledge assistant** → use `VectorStoreRetrieverMemory`

If you want **maximum control**, you can **build your own memory class** by subclassing LangChain's `BaseMemory`.

---

## ✅ Bottom Line

You're right:

> "If it appends the history to the prompt, doesn't it make the input longer and slower?"

Yes. That’s why **choosing the right memory strategy** is **critical** in real-world apps.

LangChain helps you manage that intelligently, but **you’re still responsible for managing token limits, performance, and summarization**.

---

Would you like a code example comparing all 3 memory types with token usage shown?
