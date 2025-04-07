import keyboard
import pyttsx3
import speech_recognition as sr
import webbrowser
import pywhatkit
import wikipedia
import os
import pyautogui
import psutil
import pyjokes
import sys
import requests
from bs4 import BeautifulSoup
from Functions import whatsapp
from Functions import speed
from Functions import reader
from Functions import temp
from Functions import takehindi
from Functions import opencloseapps
from Functions import ytubeauto
from Functions import browserauto
from Functions import Dictionary
from Functions import screenshot
from Functions import alarm
from Functions import videodownload
from Functions import remember
from Functions import howto
from Functions import private
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

def TaskExe():
    
    while True:

        query = takecommand()

        if 'hello' in query:
            Speak("Hello Sir , I Am Jadoo .")
            Speak("Your Personal AI Assistant!")
            Speak("How May I Help You?")

        elif 'how are you' in query:
            Speak("I Am Fine Sir!")
            Speak("Whats About YOU?")

        elif 'sleep' in query:
            Speak("Ok Sir , I am going to sleep now")
            Speak("You Can Call Me Anytime !")
            Speak("Just Say Wake Up Jadoo!")
            break


        elif 'youtube search' in query:
            Speak('Ok Sir , This is what i found for your search')
            query= query.replace("jadoo","")
            query= query.replace("youtube search","")
            web = 'https://www.youtube.com/results?search_query='+ query
            Speak('Done Sir')
        
        elif 'google search' in query:
            import wikipedia as googleScrap
            query = query.replace("jadu","")
            query = query.replace("google search","")
            query = query.replace("google","")
            Speak("This Is What I Found On The Web!")
            pywhatkit.search(query)

            try:
                result = googleScrap.summary(query,2)
                Speak(result)

            except:
                Speak("No Speakable Data Available!")

        elif 'website' in query:
            Speak("Ok sir , Launching.....")
            query=query.replace("jadoo","")
            query=query.replace("website","")
            query=query.replace(" ","")
            query=query.replace("jadoo","")
            web1 = query.replace("open","")
            web2 = 'www.'+web1+''
            Speak("Launched Boss!")

        elif 'launch' in query:
            Speak("Tell me the nameof website!")
            name=takecommand()
            web = 'www.' + name + '.com'
            webbrowser.open(web)
            Speak("Done Sir")

        elif 'play music' in query:
          Speak('Please tell the name of the song you wanna listen')
          song=takecommand()
          pywhatkit.playonyt(song)

        elif 'wikipedia' in query:
            Speak('Sir, What to search on wikipedia')
            search=takecommand()
            wiki=wikipedia.summary(search,2)
            Speak(f"According to wikipedia : {wiki}")

        elif 'whatsapp' in query:
            whatsapp.Taskexe()

        elif 'screenshot' in query:
            screenshot.screenshot()

        elif 'open code' in query:
            app=query.replace("open","")
            opencloseapps.openapps(app)
        
        elif 'open minecraft' in query:
            app=query.replace("open","")
            opencloseapps.openapps(app)
        
        elif 'open browser' in query:
            app=query.replace("open","")
            opencloseapps.openapps(app)
        
        elif 'close code' in query:
            app=query.replace("close","")
            opencloseapps.closeapps(app)
        
        elif 'close browser' in query:
            app=query.replace("close","")
            opencloseapps.closeapps(app)
        
        elif 'close minecraft' in query:
            app=query.replace("close","")
            opencloseapps.closeapps(app)

        elif 'controll youtube' in query:
            ytubeauto.YoutubeAuto()

        elif 'control browser' in query:
            browserauto.ChromeAuto()

        elif 'joke' in query:
            get = pyjokes.get_joke()
            Speak(get)

        elif 'repeat my word' in query:
            Speak("Speak Sir!")
            jj = takecommand()
            Speak(f"You Said : {jj}")

        elif 'my location' in query:
            Speak('Ok Sir, Wait a second')
            webbrowser.open('https://www.google.com/maps/@25.4257806,77.6530642,20.58z')

        elif 'dictionary' in query:
            Dictionary.Dict()

        elif 'alarm' in query:
            alarm.alarm()

        elif 'video download' in query:
            videodownload.video_down()

        elif 'translator' in query:
            takehindi.Tran()

        elif 'remember that' in query:
            remember.rem()

        elif 'what do you remember' in query:
            remeber = open('D:\\Jaadu\\Functionsdata.txt','r')
            Speak("You Tell Me That" + remeber.read())

        elif 'read book' in query:
            reader.Reader()

        elif 'downloading speed' in query:
            speed.speed()

        elif 'uploading speed' in query:
            speed.speed()

        elif 'internet speed' in query:
            speed.speed()
        
        elif 'how to' in query:
            howto.how()

        elif 'temp ' in query:
            temp.temp()

        elif 'shout down the system' in query:
            os.system("shutdown /s /t 5")
        
        elif 'restart the system' in query:
            os.system("shutdown /r /t 5")
        
        elif 'sleep the system' in query:
            os.system("roundll32.exe powrprof.dll,SetSuspendState 0,1,0")
        
        elif 'make the folder private' in query:
            private.private()
        
        elif 'make the folder public' in query:
            private.public()

        else:
            Speak("Sorry Sir, I can't do this yet please upgrade me for this")

if __name__ == "__main__":
    while True:
        permission = takecommand()
        if "wake up jadu" in permission:
            Speak("Hello Madhav.")
            Speak("How may i help you?")
            search = "temperature at your location"
            url = f"https://www.google.com/search?q=weather today"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temperature = data.find("div",class_ = "BNeawe").text
            Speak(f"The Temperature Outside Is {temperature} ")

            TaskExe()
        
        elif "wake up jack" in permission:
            Speak("Hello Arindam.")
            Speak("How may i help you?")
            search = "temperature at your location"
            url = f"https://www.google.com/search?q=weather today"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temperature = data.find("div",class_ = "BNeawe").text
            Speak(f"The Temperature Outside Is {temperature} ")

            TaskExe()

        elif "goodbye" in permission:
            sys.exit()