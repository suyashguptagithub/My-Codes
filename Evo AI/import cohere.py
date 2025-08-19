import cohere
import speech_recognition as sr
import pyttsx3
import webbrowser
import subprocess
import os
import smtplib
import pyautogui
import asyncio
import time

# Set up Cohere API key
cohere_client = cohere.Client('IUg3SPUP2V5pSxdgyqMFfVYy9Jvxgbkj23uglxAB')

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Define the log file path
log_file_path = "user_conversations.txt"

# Function to log the conversation in a file
def log_conversation(user_input, ai_response):
    with open(log_file_path, 'a') as log_file:
        log_file.write(f"User: {user_input}\n")
        log_file.write(f"EVO: {ai_response}\n\n")

# Function to recognize speech with increased speed
def recognize_speech():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    try:
        with microphone as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source, timeout=5)  # Increased speed by reducing timeout to 5 seconds

        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command

    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
        return None

    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return None

    except sr.WaitTimeoutError:
        print("Listening timed out. Please speak again.")
        return None

# Function to get response from Cohere (concise response)
async def get_cohere_response(command):
    try:
        response = cohere_client.generate(
            model='command-xlarge-nightly',  
            prompt=f"Your name is EVO (Electronic Virtual Operations) made by suyash , a sophisticated virtual assistant. Perform the task as requested by the user. Do not over-explain or provide unnecessary information. Respond succinctly. {command}",
            max_tokens=100,  # Shorter response for quicker replies
            temperature=0.5  # Set to 0.5 for more direct answers
        )
        response_text = response.generations[0].text.strip()
        print(f"EVO says: {response_text}")
        return response_text
    except cohere.error.CohereError as e:
        print(f"An error occurred with the Cohere API: {e}")
        return "Sorry, there was an issue processing your request."
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return "Sorry, an unexpected error occurred."

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to open a web browser tab
def open_web(url):
    webbrowser.open(url)

# Function to open a YouTube video
def open_youtube(video_name):
    url = f"https://www.youtube.com/results?search_query={video_name.replace(' ', '+')}"
    open_web(url)

# Function to write and send an email
def send_email(receiver_email, body):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = "suyashguptapc2@gmail.com"
    password = "wk89f8u2iv"  
    
    subject = "email by evo"
    
    # Create SMTP session
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, password)
    
    # Send email
    message = f"Subject: {subject}\n\n{body}"
    server.sendmail(sender_email, receiver_email, message)
    
    # Close SMTP session
    server.quit()

# Function to open PC files or settings
def open_file_or_settings(file_name):
    try:
        if file_name.lower() == "about pc":
            os.system('start ms-settings:about')
        elif os.path.isfile(file_name):
            os.startfile(file_name)  
        else:
            print(f"{file_name} not found.")
    except Exception as e:
        print(f"Error opening file/settings: {e}")

# Function to execute various PC tasks
def perform_task(task_name):
    tasks = {
        "open notepad": lambda: os.system('notepad'),
        "open calculator": lambda: os.system('calc'),
        "open paint": lambda: os.system('mspaint'),
        "open file explorer": lambda: os.system('explorer'),
        "open task manager": lambda: os.system('taskmgr'),
        "open command prompt": lambda: os.system('cmd'),
        "open settings": lambda: os.system('start ms-settings:'),
        "open about pc": lambda: os.system('start ms-settings:about'),
        "shutdown pc": lambda: os.system('shutdown /s /f /t 0'),
        "restart pc": lambda: os.system('shutdown /r /f /t 0'),
        "log off pc": lambda: os.system('shutdown /l'),
        "lock pc": lambda: os.system('rundll32.exe user32.dll,LockWorkStation'),
        "open browser": lambda: webbrowser.open("https://www.google.com"),
        "open google chrome": lambda: subprocess.Popen("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"),
        "open wikipedia": lambda: webbrowser.open("https://www.wikipedia.org"),
        "open google maps": lambda: webbrowser.open("https://maps.google.com"),
        "open youtube": lambda: webbrowser.open("https://www.youtube.com"),
        "close chrome": lambda: os.system("taskkill /f /im chrome.exe"),
        "close notepad": lambda: os.system("taskkill /f /im notepad.exe"),
        "close calc": lambda: os.system("taskkill /f /im calc.exe"),
        "close paint": lambda: os.system("taskkill /f /im mspaint.exe"),
        "close explorer": lambda: os.system("taskkill /f /im explorer.exe"),
        "open control panel": lambda: os.system('control'),
        "open firewall settings": lambda: os.system('start ms-settings:windowsdefender'),
        "open display settings": lambda: os.system('start ms-settings:display'),
        "open network settings": lambda: os.system('start ms-settings:network-status'),
        "open bluetooth settings": lambda: os.system('start ms-settings:bluetooth'),
        "open sound settings": lambda: os.system('start ms-settings:sound'),
        "open date and time settings": lambda: os.system('start ms-settings:dateandtime'),
        "open language settings": lambda: os.system('start ms-settings:regionlanguage'),
        "open storage settings": lambda: os.system('start ms-settings:storage'),
        "clear cache": lambda: os.system('del /q /f %temp%\\*'),
        "close task manager": lambda: os.system("taskkill /f /im taskmgr.exe"),
        "take screenshot": lambda: pyautogui.screenshot("screenshot.png"),
        "open calendar": lambda: os.system('start outlookcal:'),
        "open mail app": lambda: os.system('start outlookmail:'),
        "open skype": lambda: subprocess.Popen('C:\\Program Files (x86)\\Microsoft\\Skype for Desktop\\Skype.exe'),
        "open spotify": lambda: subprocess.Popen('C:\\Users\\User\\AppData\\Roaming\\Spotify\\Spotify.exe'),
        "open discord": lambda: subprocess.Popen('C:\\Users\\User\\AppData\\Local\\Discord\\app-1.0.9003\\Discord.exe'),
        "open steam": lambda: subprocess.Popen('C:\\Program Files (x86)\\Steam\\steam.exe'),
        "open file manager": lambda: os.system('explorer'),
        "open chrome incognito": lambda: subprocess.Popen("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe --incognito"),
        "open edge": lambda: subprocess.Popen("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"),
        "open notepad++": lambda: subprocess.Popen('C:\\Program Files (x86)\\Notepad++\\notepad++.exe'),
        "open vlc": lambda: subprocess.Popen('C:\\Program Files\\VideoLAN\\VLC\\vlc.exe'),
        "open powerpoint": lambda: subprocess.Popen('C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE'),
        "open excel": lambda: subprocess.Popen('C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE'),
        "open word": lambda: subprocess.Popen('C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE'),
        "open pdf reader": lambda: subprocess.Popen('C:\\Program Files (x86)\\Adobe\\Acrobat Reader DC\\Reader\\AcroRd32.exe'),
    }

    task = tasks.get(task_name.lower())
    if task:
        task()
    else:
        print("Sorry, I couldn't recognize the task.")

# Main function to integrate speech and task execution
async def main():
    speak("Hello, Master Evo here. How can I assist you today?")
    
    while True:
        command = recognize_speech()
        if command:
            response = await get_cohere_response(command)
            speak(response)
            log_conversation(command, response)  # Log the conversation
            perform_task(command.lower())

if __name__ == "__main__":
    asyncio.run(main())
