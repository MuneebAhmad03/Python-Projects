
#install open ai package by pip install open ai
#grab your api key
from openai imprt OpenAI
key = "paste your key here"

messages =[]
client = OpenAI(
    api_key = key,
)

def completion(message):
    global messages

    messages.append(
        {
            "role": "user",
            "content": message,
        }
    )
    chat_completion = client.chat.completions.create(messages = messages, model= "gpt-4o")
    message ={
        "role":"assistant",
        "content":chat_completion.choices[0].message.content
    }
    messages.append(message)
    print(f"Assitant {message["content"]}")

if __name__ == "__main__":
    user_question = input("Hi i am assistant, How may I help you ")

    completion(user_question)

