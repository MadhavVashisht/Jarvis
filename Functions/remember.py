import pyttsx3
import speech_recognition as sr
import sys
sys.path.append('D://Jaadu')
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

def rem():
    remeberMsg = mainjaadu.query.replace("remember that","")
    remeberMsg = remeberMsg.replace("jadu","")
    Speak("You Tell Me To Remind You That :"+remeberMsg)
    remeber = open('data.txt','w')
    remeber.write(remeberMsg)
    remeber.close()