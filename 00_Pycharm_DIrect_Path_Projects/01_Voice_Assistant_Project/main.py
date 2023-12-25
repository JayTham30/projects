import speech_recognition as sr
import pyttsx3
import webbrowser


# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to speak text
def speak(text):
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 0.8)
    engine.say(text)
    engine.runAndWait()

# Function to recognize speech
def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(f"User: {query}")
        return query.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't understand. Could you please repeat?")
        return recognize_speech()
    except sr.RequestError:
        speak("Sorry, I'm facing some technical difficulties. Please try again later.")
        return None

# Function to set reminders
    speak("Sure, what would you like to set a reminder for?")
    reminder = recognize_speech()
    if reminder:
        speak(f"Reminder set for {reminder}.")

# Function to create a to-do list
def create_todo_list():
    speak("What would you like to add to your to-do list?")
    task = recognize_speech()
    if task:
        with open('todo.txt', 'a') as file:
            file.write(f"{task}\n")
        speak(f"Task '{task}' added to your to-do list.")

# Function to read the to-do list
def read_todo_list():
    with open('todo.txt', 'r') as file:
        todo_list = file.readlines()
        if todo_list:
            speak("Here is your to-do list:")
            for task in todo_list:
                speak(task.strip())
        else:
            speak("Your to-do list is empty.")

# Function to search the web
def search_web():
    speak("What would you like to search on the web?")
    query = recognize_speech()
    if query:
        url = f"https://www.google.com/search?q={query}"
        webbrowser.open(url)
        speak(f"Here are the search results for '{query}'.")

# Main loop
while True:
    speak("How can I help you?")
    command = recognize_speech()
    if command:
        #if 'reminder' in command:
         #   set_reminder()
        if 'to-do list' in command or 'todo list' in command:
            create_todo_list()
        elif "read to-do list" in command or "read to do list" in command or "what is in my todo list" in command or "what is in my to-do list" in command:
            read_todo_list()
        elif 'search' in command or 'web' in command:
            search_web()
        #elif 'exit' in command or 'quit' in command or "stop" in command:
        elif command in ["stop", "exit", "quit"]:
            speak("Goodbye!")
            break
        else:
            speak("Sorry, I can't help with that.")
