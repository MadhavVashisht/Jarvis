import pyttsx3
import speech_recognition as sr
import requests
from bs4 import BeautifulSoup
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

def Temp():
    if 'home' in mainjaadu.query:
        search = "temperature in Shivpuri"
        url = f"https://www.google.com/search?q={search}"
        r = requests.get(url)
        data = BeautifulSoup(r.text,"html.parser")
        temperature = data.find("div",class_ = "BNeawe").text
        Speak(f"The Temperature Outside Is {temperature} celcius")

        Speak("Do I Have To Tell You Another Place Temperature ?")
        next = takecommand()

        if 'yes' in next:
            Speak("Tell Me The Name Of tHE Place ")
            name = takecommand()
            search = f"temperature in {name}"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temperature = data.find("div",class_ = "BNeawe").text
            Speak(f"The Temperature in {name} is {temperature} celcius")

        else:
            Speak("no problem sir")
    
    else:
        Speak("Tell Me The Name Of tHE Place ")
        name = takecommand()
        search = f"temperature in {name}"
        url = f"https://www.google.com/search?q={search}"
        r = requests.get(url)
        data = BeautifulSoup(r.text,"html.parser")
        temperature = data.find("div",class_ = "BNeawe").text
        Speak(f"The Temperature in {name} is {temperature} celcius")