"""
A Virtual Assistant By Aoun Abbas..
"""

#Libraries
import webbrowser
import speech_recognition as sr
import pyttsx3
import os
import face_recognition
import pywhatkit
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
import cv2
import numpy as np



#Main_Variables
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
cascade_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

#Talk_Function
def talk(text):
    engine.setProperty('rate', 160)
    engine.say(text)
    engine.runAndWait()

#Speech_Recog_Input
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


#Face_Recog_Function
def face_recog():
    # list of known members
    # Member 1
    mohsin_image = face_recognition.load_image_file("mohsin.jpg")
    mohsin_face_encoding = face_recognition.face_encodings(mohsin_image)[0]

    # Member 2
    aoun_image = face_recognition.load_image_file("aoun.jpg")
    aoun_face_encoding = face_recognition.face_encodings(aoun_image)[0]

    known_face_encodings = [
        mohsin_face_encoding,
        aoun_face_encoding
    ]
    known_face_names = [
        "Mohsin",
        "On"
    ]

    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True

    while True:
        ret, frame = cap.read()

        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        rgb_small_frame = small_frame[:, :, ::-1]

        if process_this_frame:
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

            face_names = []
            for face_encoding in face_encodings:
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Unknown"

                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]
                    talk('Hello...' + name + '...Good to see you')
                    talk('i have recognized you so to start press q')


        process_this_frame = not process_this_frame

        for (top, right, bottom, left), name in zip(face_locations, face_names):
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            talk('system started')
            break
    cap.release()
    cv2.destroyAllWindows()

#Time_Function
def time():
    Time = datetime.datetime.now().strftime('%I:%M %p')
    talk(Time)

#Date_Function
def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    talk(year)
    talk(month)
    talk(day)

#Main_Onion_Function
def run_onion():
    command = take_command()
    print(command)
#IF.....ELIF.....ELSE.....STATEMENTS
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
    elif 'hi' in command:
        talk('Hello there..... How are you')
        print(':)')
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'what is' in command:
        talk('Wait.........imma tell you in a second')
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
        talk('i have successfully sent the email from your gmail')
    elif 'alexa' in command:
        talk('I am not alexa, i am onion')
    elif 'you hungry' in command:
        talk('I dont feel hunger')
    elif 'hungry' in command:
        webbrowser.open('https://www.foodpanda.pk')
        talk('here you go.......get something for yourself')
    elif 'twitter' in command:
        webbrowser.open('https://www.twitter.com')
        talk('here you go....opening twitter')
    elif 'youtube' in command:
        webbrowser.open('https://www.youtube.com')
        talk('here you go... opening youtube')
    elif 'instagram' in command:
        webbrowser.open('https://www.instagram.com')
        talk('Opening Insta ')
    elif 'siri' in command:
        talk('i am onion')
    elif 'google' in command:
        talk('i am onion not google ')
    elif 'onion' in command:
        talk('yes sir, i am here')
    elif 'search' in command:
        search = command.replace('search', '')
        pywhatkit.search(search)
        print("Searching...")
        print("Opening browser")
        talk('searching and opening browser')
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
    elif 'thanks' in  command:
        talk('my pleasure')
    elif 'thank you' in command:
        talk('welcome')
    elif 'real' in command:
        talk('I am not real... I am a virtual Assistant')
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


face_recog()

while True:
    run_onion()