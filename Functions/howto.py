import pyttsx3
import speech_recognition as sr
import sys
sys.path.append('D://Jaadu')
import mainjaadu
from pywikihow import search_wikihow

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

def how():
    Speak("Getting data from the internet")
    op = mainjaadu.query
    max_result = 1
    how_to_func=search_wikihow(op,max_result)
    assert len(how_to_func) == 1
    how_to_func[0].print()
    Speak(how_to_func[0].summary)
