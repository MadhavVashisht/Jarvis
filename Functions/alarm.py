import pyttsx3
import speech_recognition as sr
import os
import datetime
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate',170)

def Speak(Audio):
    print("   ")
    print(f": {Audio}")
    engine.say(Audio)
    print("    ")
    engine.runAndWait()

def takecommand(): 
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("          ")
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"Your Command :  {query}\n")

    except:   
        return "None"
        
    return query.lower()

def alarm():
    Speak("Enter The Time !")
    time = input(": Enter The Time :")
    n=random.randint(0,19)
    dir="D:\\Jaadu\\songs"
    while True:
        Time_Ac = datetime.datetime.now()
        now = Time_Ac.strftime("%H:%M:%S")

        if now == time:
            Speak("Time To Wake Up Sir!")
            n=random.randint(0,19)
            n=str(n)+'.mp3'
            dir="D:\\Jaadu\\songs\\"
            os.startfile(dir+n)

        elif now>time:
            Speak("Alarm Closed!")
            break
