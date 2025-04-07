import pyttsx3
import speech_recognition as sr


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

def Dict():
        Speak('Activated Dictionary!')
        Speak('Tell me the problem sir!')
        problem=takecommand()
        if 'meaning' in problem:
             problem=problem.replace("What is the meaning","")
             problem=problem.replace("of","")
             problem=problem.replace("jadu","")
             result=dict.meaning(problem)
             Speak(f"the meaning of {problem} is {result}")
