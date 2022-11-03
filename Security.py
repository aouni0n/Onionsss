import speech_recognition as sr
import pyttsx3
import os
import serial

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.setProperty('rate', 160)
    engine.say(text)
    engine.runAndWait()


try:
    port = serial.Serial("COM3", 9600, timeout=1)
    talk("Successfully Executed Security Protocol")
    print("Executed Security Protocol.")
except:
    talk("Unable to connect to my physical body")
    print("Security Protocol Execution Failed")



def take_command():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("Detecting....")
        command.pause_threshold = 1
        audio = command.listen(source)

        try:
            print("Processing....")
            query = command.recognize_google(audio,language='en-US')

        except:
            return "No Motion"

        return query.lower()




while True:
    inp = str(port.readline())
    command = take_command()
    if 'motion' in inp:
        print("Motion Detected!!!!")
        talk('My Passive Infra red sensor can detect PIR rays which means there is a living object around me')
    elif 'security protocol' in command:
        print('Terminated Security Protocol')
        talk('Terminating Security Protocol')
        os.startfile(r"C:\Users\DELL\Downloads\pythonProject\main.py")
        exit(talk('Returned To Normal Mode'))
    elif 'gas' in inp:
        print("Gas Detected!!")
        talk('I can smell gas around here........for your safety you should check if there is a leak')
    else:
        talk('')