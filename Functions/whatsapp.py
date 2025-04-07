from urllib.parse import quote
import pyttsx3
import speech_recognition as sr
import pywhatkit
import keyboard


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

def Taskexe():

    Speak('Tell me the name of the receiver')
    name=takecommand()
    if 'papa' in name:
      Speak('Tell me the message sir')
      msg=takecommand()
      pywhatkit.sendwhatmsg_instantly("+918827541214",msg,20)
      keyboard.press_and_release('enter')
      Speak(f"Sending Whatsapp message to : {name}")
    
    if 'mummy' in name:
      Speak('Tell me the message sir')
      msg=takecommand()
      pywhatkit.sendwhatmsg_instantly("+917898445467",msg,20)
      keyboard.press_and_release('enter')
      Speak(f"Sending Whatsapp message to : {name}")
    
    if 'raghav' in name:
      Speak('Tell me the message sir')
      msg=takecommand()
      pywhatkit.sendwhatmsg_instantly("+919301414955",msg,20)
      keyboard.press_and_release('enter')
      Speak(f"Sending Whatsapp message to : {name}")
    
    if 'riya' in name:
      Speak("tell me the message boss")
      msg=takecommand()
      pywhatkit.sendwhatmsg_instantly("+919953462101",msg,20)
      keyboard.press_and_release('enter')
      Speak(f"Sending Whatsapp message to : {name}")
    
    else:
      Speak('Please Enter The Phone Number')
      num=input()
      ph= '+91' + num
      Speak('Tell me the message sir')
      msg=takecommand()
      Speak('Please, Tell me the time sir')
      Speak('Time in hour!')
      hour=int(takecommand())
      Speak('Time in minutes')
      min=int(takecommand())
      pywhatkit.sendwhatmsg_instantly(ph,msg,20)
      keyboard.press_and_release('enter')
      Speak(f"Sending Whatsapp message to : {name}")
