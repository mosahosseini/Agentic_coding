import openai 
import openai
import os

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY") or "your-api-key-here" ## you can make a .env file and write OPENAI_API_KEY = "your-api-key" 

# Store the conversation
conversation = [
    {"role": "system", "content": "You are a helpful assistant."}
]

print("🤖 GPT-3.5 Chatbot. Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")
    if user_input.strip().lower() in ["exit", "quit"]:
        print("Chatbot: Goodbye!")
        break

    # Add user's message
    conversation.append({"role": "user", "content": user_input})

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=conversation,
            temperature=0.7,
            max_tokens=512
        )

        reply = response.choices[0].message["content"].strip()
        print(f"Chatbot: {reply}")
        conversation.append({"role": "assistant", "content": reply})

    except Exception as e:
        print(f"Error: {e}")
