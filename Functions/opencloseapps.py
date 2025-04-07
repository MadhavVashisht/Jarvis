import pyttsx3
import speech_recognition as sr
import os
import pywhatkit
import mainjaadu

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

def openapps(app):
        Speak('Ok Sir, Wait a second')
        if 'code' in app:
            os.startfile("C:\\Users\\madha\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe")
            Speak('Done Sir, here is your application')

        elif 'minecraft' in app:
            os.startfile("C:\\Users\\madha\\AppData\\Roaming\\.minecraft\\tlauncher.exe")
            Speak('Done Sir, here is your application')
        
        elif 'browser' in app:
            os.startfile("C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe")

            #query=app.replace("open","")
            #pywhatkit.search(query)
            #Speak("Hear's what i found on google")

def closeapps(app):
        Speak('Ok Sir, Wait a second')
        if 'code' in app:
            os.system("TASKKILL /F /IM code.exe")
            Speak('Done Sir, here is your application closed!')

        elif 'minecraft' in app:
            os.system("TASKKILL /F /IM tlauncher.exe")
            Speak('Done Sir, here is your application closed!')
        
        elif 'browser' in app:
            os.system("TASKKILL /F /IM brave.exe")
            Speak('Done Sir, here is your application closed!')