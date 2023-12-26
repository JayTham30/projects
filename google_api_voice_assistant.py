import speech_recognition as sr
import pyttsx3
import webbrowser
import time
import openai
openai.api_key =








# Initialize the text-to-speech engine
engine = pyttsx3.init()


# Function to generate response from GPT
'''def generate_response(prompt):
   response = openai.Completion.create(
       engine="text-davinci-003",
       gpt_task=gpt_task,
       max_tokens=4000,
       n=1,
       stop=None,
       temperature=0.5,
   )
   return response["choices"][0]["text"]
   '''


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




# Function to generate response using Chat-GPT API
'''def gpt_response():
   speak("what would you like chat g-p-t to do for you")
   gpt_task = recognize_speech()
   response = openai.Completion.create(
       engine="text-davinci-003",
       gpt_task=gpt_task,
       max_tokens=4000,
       n=1,
       stop=None,
       temperature=0.5,
   )
   return gpt_task(["choices"] [0] ["text"])'''




# Function to give the local time
def local_time():
   current_time = time.localtime()
   hour = current_time.tm_hour
   minutes = current_time.tm_min
   speak(f"Current local time is {hour} hours and {minutes} minutes")


# Function to set reminders
def set_reminder():
   speak("Sure, what would you like to set a reminder for")
   reminder = recognize_speech()
   if reminder:
       speak(f"Reminder set for {reminder}.")


# Function to create a to-do list
def create_todo_list():
   speak("What would you like to add to your to-do list")
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


# Function to clear the to-do list
def clear_todo_list():
   with open('todo.txt', 'r+') as file:
       file.truncate(0)
   speak("your to-do list is cleared")


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
       '''if 'Chat GPT' in command:
           gpt_response()'''
       if 'reminder' in command:
           set_reminder()
       elif "read to-do list" in command or "read to do list" in command:
           read_todo_list()
       elif 'clear to do list' in command or 'clear to-do list' in command:
           clear_todo_list()
       elif 'to-do list' in command or 'todo list' in command:
           create_todo_list()
       elif 'what time is it' in command:
           local_time()
       elif 'search' in command or 'web' in command:
           search_web()
       #elif 'exit' in command or 'quit' in command or "stop" in command:
       elif command in ["stop", "exit", "quit"]:
           speak("Goodbye!")
           break
       else:
           speak("Sorry, I can't help with that.")


# Line to Test command function.
'''command = read_todo_list()'''
