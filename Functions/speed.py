import pyttsx3
import speech_recognition as sr
import mainjaadu
import speedtest

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

def speed():
        Speak("Checking Speed..........")
        speed = speedtest.Speedtest()
        down = speed.download()
        correctdown = int(down/800000)
        up = speedtest.upload()
        correctup = int(up/800000)

        if 'uploading' in mainjaadu.query:
            Speak(f"The current uploading speed is {correctup} mbps")

        elif 'downloading' in mainjaadu.query:
            Speak(f"The current downloading speed is {correctdown} mbps")

        else:
            Speak(f"The current Downloading speed is {correctdown} mbps")
            Speak(f"The current Uploading speed is {correctup} mbps")