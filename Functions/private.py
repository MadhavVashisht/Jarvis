import pyttsx3
import speech_recognition as sr
import os
import sys
sys.path.append("D://Jaadu")
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
def private():
    Speak("Enter the path of the file or folder")
    p=input("Path:")
    os.system("attrib +h /s /d "+ p )
    Speak("Boss, all the files in the folder are done private")

def public():
    Speak("Enter the path of the file or folder")
    p=input("Path:")
    os.system("attrib -h /s /d "+ p )
    Speak("Boss, all the files in the folder are done public")

