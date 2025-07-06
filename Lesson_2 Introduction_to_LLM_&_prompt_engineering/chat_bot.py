from openai import OpenAI
import os
from dotenv import load_dotenv


load_dotenv()
api =   os.getenv('api_key')


client = OpenAI(api_key = api) 

conversation = [
    {"role": "system", "content": "You are a helpful assistant."}
]


print("Chat gpt chatbot: enter quit or exit  for exiting the chatbot")

while (True):
    user_input = input("You: ")
    
    if user_input.strip().lower() in ["quit" , "exit"]:
        print("Goodbye!!! ")
        break
    
    conversation.append({"role":"user" , "content": user_input})
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=conversation,
            temperature=0.7,
            max_tokens=512 
        )
        reply = response.choices[0].message["content"].strip()
        print(f"Chatbot: {reply}")
        conversation.append({"role": "assistant", "content": reply})

    
    except Exception as e:
        print(f"Error: {e}")
