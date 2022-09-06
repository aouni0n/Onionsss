import os
import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        command.pause_threshold = 1
        audio = command.listen(source)

        try:
            print("Recognizing....")
            query = command.recognize_google(audio,language='en-US')
            print(f"you said : {query}")

        except:
            return "none"

        return query.lower()



while True:


    wakeup = take_command()

    if 'wake up' in wakeup:
        os.startfile(r"C:\Users\DELL\Downloads\pythonProject\main.py")
        talk('Intializing Onion, Checking parameters, Executing Servers')
        talk('here you go')
    elif 'onion' in wakeup:
        os.startfile(r"C:\Users\DELL\Downloads\pythonProject\main.py")
        talk('Intializing Onion, Checking parameters, Executing Servers')


