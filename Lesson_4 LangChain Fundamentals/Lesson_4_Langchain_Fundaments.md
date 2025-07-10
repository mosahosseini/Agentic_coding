
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

### 🔍 **1. What Memory *Actually* Does in LangChain**

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

### 🧮 **2. Implication: Longer Memory = Longer Prompts**

You're absolutely correct:

* Every new message adds to the **total input token count**.
* **More tokens = longer processing time** and **higher cost** (if using paid APIs).
* **Eventually, you will hit the model’s context limit** (e.g., 4k, 8k, or 128k tokens).

So yes: **using full memory with no constraints can hurt performance and cost.**

---

### 🧠 **3. Different Memory Strategies (to Control This)**

LangChain offers several memory types to **balance memory vs efficiency**.

---

###  A. `ConversationBufferMemory` – Full History

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

### ⚖️ **4. Summary of Trade-Offs**

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




## What are Tools?
Tools are functions an agent can call to perform specific tasks, like web search, math, or API calls.

```py
from langchain.agents import tool

@tool
def multiply(x: int, y: int) -> int:
    """Multiplies two numbers."""
    return x * y
```


## Retrieval-Augmented Generation (RAG)

### What is RAG?
Retrieval-Augmented Generation (RAG) is a method that improves the quality of generated text by supplementing a generative model (like GPT or BART) with an external knowledge base. Instead of relying solely on what the model learned during training, it retrieves relevant documents or passages at runtime to help form more accurate and grounded responses.

### Key Components of RAG

**Retriever:** Finds relevant documents from a large corpus based on a query.

Example: Dense Passage Retrieval (DPR), BM25

**Generator:** Takes the query and retrieved documents to generate a response.

Example: BART, T5, or GPT-based models

### 📊 Workflow
**Step-by-Step:**
1. **Input Query:** User inputs a question or prompt.

2. **Retrieve Documents:** The retriever finds top-k relevant documents from a corpus.

3. **Augment Input:** The original query is combined with the retrieved documents.

3. **Generate Output:** The generator uses this augmented input to produce a coherent response.


### 🛠️ Implementation Example with Hugging Face 🤗
You can implement RAG using transformers and datasets.


You can implement RAG using `transformers` and `datasets`. 

### 🔧 Prerequisites

```bash
pip install transformers datasets faiss-cpu
```

### 📜 Code Example

```python
from transformers import RagTokenizer, RagRetriever, RagSequenceForGeneration

# Load tokenizer, retriever, and model
tokenizer = RagTokenizer.from_pretrained("facebook/rag-sequence-nq")
retriever = RagRetriever.from_pretrained("facebook/rag-sequence-nq", index_name="exact", use_dummy_dataset=True)
model = RagSequenceForGeneration.from_pretrained("facebook/rag-sequence-nq", retriever=retriever)

# Input question
question = "What is the capital of France?"

# Tokenize
input_dict = tokenizer.prepare_seq2seq_batch([question], return_tensors="pt")

# Generate response
generated = model.generate(**input_dict)
output = tokenizer.batch_decode(generated, skip_special_tokens=True)[0]

print("Generated Answer:", output)
```

> Note: This example uses a dummy dataset for the retriever. For a real application, you'd use a custom document index (e.g., Wikipedia or internal company docs).

---

## 🔎 When to Use RAG

* When your model needs **up-to-date** or **domain-specific knowledge**
* In **question answering**, **chatbots**, **enterprise search**, or **document summarization**
* To reduce **hallucinations** in generative models

---

## 📚 Best Practices

* **Use a high-quality retriever**: Dense retrievers like DPR often outperform traditional methods.
* **Preprocess documents**: Clean, chunk, and index your data effectively.
* **Fine-tune the generator**: Improves response relevance and fluency.
* **Caching**: Speed up inference by caching frequently accessed retrievals.

---

## 🚀 Advanced Concepts

* **Fusion-in-Decoder (FiD)**: Processes all documents simultaneously with the full attention mechanism.
* **RAG-Token vs. RAG-Sequence**: Different ways of attending to retrieved documents per token or per sequence.
* **Hybrid retrieval**: Combine dense and sparse (e.g., BM25 + DPR) for better recall.

---

## 📘 Summary

| Component | Role                      | Tools                |
| --------- | ------------------------- | -------------------- |
| Retriever | Finds relevant documents  | DPR, BM25, FAISS     |
| Generator | Produces the final output | BART, T5, GPT        |
| Index     | Stores the knowledge base | FAISS, Elasticsearch |

RAG bridges the gap between **static training knowledge** and **dynamic real-world knowledge**, making it ideal for real-world AI applications.

---

Would you like an **interactive notebook**, a **custom dataset example**, or a **diagram** to go along with this tutorial?


