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




Exercise:
Create a CLI chatbot using gpt-3.5-turbo.


