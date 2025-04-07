import pyttsx3
import speech_recognition as sr
import pyautogui
import os

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



def screenshot():
        Speak("Ok boss, tell me what should I name it?")
        path=takecommand()
        path1name=path+".png"
        path1="D:\\ScreenShots\\"+path1name
        kk=pyautogui.screenshot()
        kk.save(path1)
        os.startfile("D:\\ScreenShots\\"+path1name)
        Speak("Here is your Screen-shot BOSS!")
