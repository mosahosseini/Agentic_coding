# Lesson 2: Introduction to LLMs & Prompt Engineering

**Topics:**
1. How LLMs work (transformers, tokens, inference)
2. OpenAI API / Hugging Face transformers
3. Basic prompting (zero-shot, few-shot)

## 1 How LLMs work
LLM stand for Large Language Models and is the AI breakthrough of the recent years. Language models a predictive model that are used to predict the next token/word given n previouse word. I will not go though the transformer architecture in datail i will just give you a quick overview on how does it work and how the chat interfaces like chatgpt are built.  So language model will generate the next word give the n previouse word/token. How can the chatbots use it? For this purpose they train the transformer with pair of questions and answers , and add a special charachter at the end of the chats `<\EOS>` special charachter for terminating the generation of the text. Now when you ask a question , the language model will also generate the special charachter. This special charachter is used to stop the generation. 



## OpenAI API /Hugging Face transformers. 

You can use openAi with api and here is how :

```
import openai

openai.api_key = "your-api-key"

response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "user", "content": "Tell me a joke"}
    ]
)

print(response['choices'][0]['message']['content'])
```

You will of couse need an api key for this to work. 


### What is Huggingface
Hugging Face is a company and an open-source platform focused on democratizing artificial intelligence, particularly in natural language processing (NLP) and machine learning (ML). It offers tools, pre-trained models, datasets, and a community for building, deploying, and sharing AI models. Essentially, it's a hub where developers and researchers can collaborate, access resources, and build AI applications. 

There are alot of opensoruce models available on huggingface. Therer you can find some of the state of the art opensource  models. Huggingface often provide example code on how to run the model. The code depends on which model you use.


---

## ✅ Step-by-Step Guide: How to Write a Prompt in ChatGPT

---
An important part of the LLM is the instruction you give to it. It can be a question or instruction , and it will guid the llm to generate the answer. 

Sure! Here's a **step-by-step guide** to writing effective prompts in **ChatGPT** — whether you're aiming for writing, coding, summarizing, planning, or any other task.
### **Step 1: Define Your Goal Clearly**

Ask yourself:

* What do I want ChatGPT to do?
* Am I asking for information, content generation, analysis, or help brainstorming?

**Examples:**

* ✅ *"Summarize this article in 5 bullet points."*
* ✅ *"Write a formal email to a client about project delay."*

---

### **Step 2: Add a Clear Task Verb**

Start with an action word:

* **Write**, **Summarize**, **Explain**, **List**, **Generate**, **Translate**, **Convert**, etc.

**Examples:**

* ✅ *"List 10 creative marketing ideas for a new coffee shop."*
* ✅ *"Explain quantum entanglement like I’m five."*

---

### **Step 3: Add Context (If Needed)**

Tell ChatGPT the background:

* Who are you?
* What is this about?
* What are the constraints or tone?

**Examples:**

* ✅ *"You're a career coach. Give resume advice for a software engineer with 2 years of experience."*
* ✅ *"I’m a teacher. Rewrite this paragraph so 12-year-olds can understand it."*

---

### **Step 4: Specify Format or Style**

If you want a specific format, mention it:

* Bullet points
* Table
* Email format
* Code snippet
* Poem, story, etc.

**Examples:**

* ✅ *"Summarize this text as 5 bullet points."*
* ✅ *"Write a Python function to calculate factorial using recursion."*

---

### **Step 5: Iterate and Refine**

Not happy with the first response? Ask follow-ups:

* *“Make it shorter”*
* *“Use a more casual tone”*
* *“Add more detail about X”*
* *“Can you explain this with a real-life example?”*

---

## 🔁 Prompt Template

Here's a simple fill-in-the-blank template you can follow:

> **\[Action]** a **\[format]** for **\[audience or purpose]** using **\[specific context or input]**. Use a **\[tone/style]**.

**Example:**

> *Write a professional email to a customer apologizing for a shipping delay. Use a polite and empathetic tone.*

---

## ✅ Good vs. Bad Prompt Example

**❌ Bad Prompt:**

> *Marketing tips.*

**✅ Good Prompt:**

> *Give me 5 creative marketing tips for a new fitness app targeting Gen Z. Use a casual tone and short bullet points.*

---

Want to practice a prompt? Tell me what you want to do and I’ll help you write one!

### Zero-shot 
When you provide the prompt without the example of input output. Forexample: What is the capital of Paris? 

### Few-shot
When you provide the prompt with number of input output example in order to guide the answers. 


Translate everything i write from now on to swedish? 

Example: 

User: Hi how are you?
Assistant: Hej hur mår du?






Exercise:
Create a CLI chatbot using gpt-3.5-turbo.


