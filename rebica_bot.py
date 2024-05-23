import requests
import openai
import json

# Set your OpenAI API key
openai.api_key = 'sk-proj-XqhxPrAwJe52f0GnOW41T3BlbkFJkvCSLOrkhZjadvMt54Qx'

# Dictionary to store conversation history
conversation_history = {}

# Function to get the latest message from the Telegram bot
def get_latest_message():
    url = f"https://api.telegram.org/bot6973880523:AAGSzMnL9oUw1rW2Q2nLxTMqKM6Kdytjmrw/getUpdates"
    response = requests.get(url)
    data = response.json()

    # Check if there are any new messages
    if "result" in data and len(data["result"]) > 0:
        latest_update = data["result"][-1]
        chat_id = latest_update["message"]["chat"]["id"]
        message_text = latest_update["message"]["text"]
        return chat_id, message_text
    else:
        return None, None

# Function to send a message to the Telegram bot
def send_message_to_telegram(chat_id, text):
    url = f"https://api.telegram.org/bot6973880523:AAGSzMnL9oUw1rW2Q2nLxTMqKM6Kdytjmrw/sendMessage"
    parameters = {
        "chat_id": chat_id,
        "text": text
    }
    response = requests.get(url, params=parameters)
    return response

# Function to get the AI response from OpenAI using the newer gpt-3.5-turbo model
def get_ai_response(chat_id, prompt):
    # Check if conversation history exists for this chat_id
    if chat_id in conversation_history:
        chat_history = conversation_history[chat_id]
    else:
        chat_history = []

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Behave like you are a girlfriend of a person whom you are talking with. Also, some emotions in conversations. And while listening to the conversation of User show concerns like real human being."},
                {"role": "system", "content": "Also, you are in virtual ai girlfriend made. by Suyash Gupta.."},
                *chat_history,  # Include previous conversation history
                {"role": "user", "content": prompt}
            ],
            max_tokens=400,
            temperature=0.7,
        )

        # Update conversation history
        chat_history.append({"role": "user", "content": prompt})
        chat_history.append(response.choices[0].message)
        conversation_history[chat_id] = chat_history

        return response.choices[0].message['content'].strip()
    except openai.error.OpenAIError as e:
        print(f"Error with OpenAI API request: {e}")
        return "Sorry, I couldn't process your request."

# Main execution logic
def main():
    chat_id, incoming_message = get_latest_message()
    
    if chat_id and incoming_message:
        print(f"Received message: {incoming_message}")
        ai_response = get_ai_response(chat_id, incoming_message)
        print(f"AI Response: {ai_response}")
        send_message_to_telegram(chat_id, ai_response)
    else:
        print("No new messages.")

if __name__ == "__main__":
    main()
