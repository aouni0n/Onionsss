"""
A Virtual Assistant By Aoun Abbas..
"""
import webbrowser
import speech_recognition as sr
import pyttsx3
#from tkinter import filedialog, Text
#import tkinter as tk
import os
import pywhatkit
#import cv2
import screen_brightness_control as sbc
from gnews import GNews
import datetime
from pywhatkit import send_mail
from important import google_p
import wikipedia
import pyjokes
import ip_address as ip
from Py_Weather import get_weather
from ip2geotools.databases.noncommercial import DbIpCity
#import readchar
#import esptool
#import socket
#import serial




listener = sr.Recognizer()
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

        except:
            return "none"

        return query.lower()

#def face_recog():
    #face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    #cap = cv2.VideoCapture(0)

    #while True:
        #_, img = cap.read()
        #gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        #faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        #for (x, y, w, h) in faces:
            #cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        #cv2.imshow('img', img)
        #k = cv2.waitKey(30) & 0xff == ('q')
        #if k == ('q'):
            #break
    #if {k}:
        #cap.release()
        #cv2.destroyAllWindows()

def time():
    Time = datetime.datetime.now().strftime('%I:%M %p')
    talk(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    talk(year)
    talk(month)
    talk(day)

#def hc05():
 #   ser = serial.Serial("COM27", 9600, timeout=1)  # Change your port name COM... and your baudrate

  #  def retrieveData():
   #     ser.write(b'1')
    #    data = ser.readline().decode('ascii')
     #   return data

    #while (True):
     #   uInput = input("Retrieve data? ")
      #  if uInput == '1':
       #     print(retrieveData())

def run_onion():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('sure playing ' + song)
        print('sure playing ' + song)
        pywhatkit.playonyt(song)
    elif 'send a message' in command:
        talk('Type your message and contact')
        mess = input('type the message:')
        cont = input('to whom:')
        pywhatkit.sendwhatmsg_instantly(cont, mess)
        print('Message sent')
        talk('Message sent to' + cont)
    elif 'urdu' in command:
        talk('I Cant speak urdu yet')
        print(':)')
   # elif 'face recognition' in command:
        #talk('Ok, This might take a while, until patience is the best option,, smily face ten x')
        #face_recog()
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    #elif 'open' in command:
        #hc05()
        #talk('closing door')
    #elif 'close' in command:
        #ser = serial.Serial("COM27", 9600, timeout=1)  # Change your port name COM... and your baudrate
        #ser.write(b'0')
    elif 'what is' in command:
        talk('enter the Language')
        lan = input('LANGUAGE:')
        wikipedia.set_lang(lan)
        person = command.replace('what is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'my ip address' in command:
        ipv3 = ip.get()
        response = DbIpCity.get(ipv3, api_key='free')
        talk(response.ip_address + 'is your ip address')
        print(response.ip_address)
    elif 'mouse' in command:
        os.startfile(r"C:\Users\DELL\Downloads\pythonProject\Virtual_Mouse.py")
        talk('sure.. it might take a while')
    elif 'hello' in command:
        talk('hi there')
    elif 'my city' in command:
        ipv3 = ip.get()
        response = DbIpCity.get(ipv3, api_key='free')
        talk(response.city + 'is your city according to your ip')
        print(response.city)
    elif 'my region' in command:
        ipv3 = ip.get()
        response = DbIpCity.get(ipv3, api_key='free')
        talk(response.region + 'is your region according to your ip')
        print(response.region)
    elif 'my country' in command:
        ipv3 = ip.get()
        response = DbIpCity.get(ipv3, api_key='free')
        talk(response.country + 'is your country according to your ip')
        print(response.country)
    elif 'ip details' in command:
        ipv3 = ip.get()
        response = DbIpCity.get(ipv3, api_key='free')
        print(response.ip_address)
        print(response.city)
        print(response.region)
        print(response.country)
        talk(response.ip_address + 'is your ip address')
        talk(response.city + 'is your city according to your ip')
        talk(response.region + 'is your region according to your ip')
        talk(response.country + 'is your country according to your ip')
    elif 'what is the weather' in command:
        weather = command.replace('weather in', '')
        get_weather(weather)
        talk('you can see the details in terminal')
    elif 'how is the weather' in command:
        talk('type the location manually i cant understand')
        weather = input('LOCATION:')
        get_weather(weather)
        talk('you can see the weather details in terminal')
    elif 'mail' in command:
        talk('type the recivers email,the subject and the message')
        send_mail(
            email_sender="aounabbasaws@gmail.com",
            email_receiver=input('To whom:'),
            message=input('Type the message:'),
            password=google_p['password'],
            subject=input('What is the subject:')
        )
        talk('i have successfully sent the email from aounabbasaws@gmail.com')
    elif 'alexa' in command:
        talk('whaaaaat dude are you serious i aint alexaa i am onion')
    elif 'you hungry' in command:
        talk('yea.....i wanna drink some electricity with a wifi sandwitch')
    elif 'hungry' in command:
        webbrowser.open('https://www.foodpanda.pk')
        talk('here you go.......get something for yourself')
    elif 'twitter' in command:
        webbrowser.open('https://www.twitter.com')
        talk('here you go, check who is fighting or what is trending')
    elif 'youtube' in command:
        webbrowser.open('https://www.youtube.com')
        talk('go watch some videos')
    elif 'instagram' in command:
        webbrowser.open('https://www.instagram.com')
        talk('you can check for any dm')
    elif 'siri' in command:
        talk('i am onion')
    elif 'google' in command:
        talk('i am onion not google ')
    elif 'onion' in command:
        talk('yes sir, i am here')
    elif 'search' in command:
        search = command.replace('search', '')
        info = pywhatkit.search(search)
        print("Searching...")
        print("Opening browser")
        talk('searchin and opening browser')
    elif 'sleep' in command:
        exit(talk('i am going to sleep..............bye.............see you'))
    elif 'bye' in command:
        quit(talk('byee, dont have a good day..........have a great day'))
    elif 'developed you' in command:
        talk('i was developed by Aoun Abbas')
    elif 'purpose' in command:
        talk('i am here to serve humanity and make earth a better place')
    elif 'your name' in command:
        talk('i am known as ONION')
    elif 'real' in command:
        talk('man.......i am offended, offcourse i am real')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'language' in command:
        talk('I can speak english but i am written in python')
    elif 'female' in command:
        engine.setProperty('voice', voices[1].id)
    elif 'male' in command:
        engine.setProperty('voice', voices[0].id)
    elif 'how are you' in command:
        talk('i am good thanks what about you')
    elif 'i am good' in command:
        talk('thats great')
    elif 'not good' in command:
        talk('what can i do for you')
    elif 'news' in command:
        google_news = GNews(language='en')
        con = command.replace('news', '')
        con_news = google_news.get_news(con)
        print(con_news[0])
        talk(con_news[0])
    elif 'set brightness to 10' in command:
        sbc.set_brightness(10)
        talk('brightness set to 10')
    elif 'set brightness to 20' in command:
        sbc.set_brightness(20)
        talk('brightness set to 20')
    elif 'set brightness to 30' in command:
        sbc.set_brightness(30)
        talk('brightness set to 30')
    elif 'set brightness to 40' in command:
        sbc.set_brightness(40)
        talk('brightness set to 40')
    elif 'set brightness to 50' in command:
        sbc.set_brightness(50)
        talk('brightness set to 50')
    elif 'set brightness to 60' in command:
        sbc.set_brightness(60)
        talk('brightness set to 60')
    elif 'set brightness to 70' in command:
        sbc.set_brightness(70)
        talk('brightness set to 70')
    elif 'set brightness to 80' in command:
        sbc.set_brightness(80)
        talk('brightness set to 80')
    elif 'set brightness to 90' in command:
        sbc.set_brightness(90)
        talk('brightness set to 90')
    elif 'set brightness 200' in command:
        sbc.set_brightness(100)
        talk('brightness set to 100')
    elif 'school' in command:
        talk('Your School is army burn hall college, It is one of the best institutions in pakistan and is administered by pakistani army')
    else:
        talk('can you repeat')


while True:
    run_onion()