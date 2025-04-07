import pyttsx3
import speech_recognition as sr
from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import Tk
from tkinter import StringVar
from pytube import YouTube

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

def video_down():
    root = Tk()
    root.geometry('500x300')
    root.resizable(0,0)
    root.title("Youtube Video Downloader")
    Speak("Enter Video Url Here !")
    Label(root,text = "Youtube Video Downloader",font = 'arial 15 bold').pack()
    link = StringVar()
    Label(root,text = "Paste Yt Video URL Here",font = 'arial 15 bold').place(x=160,y=60)
    Entry(root,width = 70,textvariable = link).place(x=32,y=90)

    def VideoDownloader():
        url = YouTube(str(link.get()))
        video = url.streams.first()
        video.download()
        Label(root,text = "Downloaded",font = 'arial 15').place(x= 180,y=210)

    Button(root,text = "Download",font = 'arial 15 bold',bg = 'pale violet red',padx = 2 , command = VideoDownloader).place(x=180,y=150)

    root.mainloop()
    Speak("Video Downloaded")
