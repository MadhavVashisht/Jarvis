import pyttsx3
import speech_recognition as sr
import playsound
from gtts import gTTS
from googletrans import Translator
import os
import PyPDF2


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

def Reader():
         Speak("Tell Me The Name Of The Book!")

         name = takecommand()

         if 'india' in name:

             os.startfile('')
             book = open('')
             pdfreader = PyPDF2.PdfFileReader(book)
             pages = pdfreader.getNumPages()
             Speak(f"Number Of Pages In This Books Are {pages}")
             Speak("From Which Page I Have To Start Reading ?")
             numPage = int(input("Enter The Page Number :"))
             page = pdfreader.getPage(numPage)
             text = page.extractText()
             Speak("In Which Language , I Have To Read ?")
             lang = takecommand()

             if 'hindi' in lang:
                 transl = Translator()
                 textHin = transl.translate(text,'hi')
                 textm = textHin.text
                 speech = gTTS(text = textm )
                 try:
                     speech.save('book.mp3')
                     playsound('book.mp3')

                 except:
                     playsound('book.mp3')

             else:
                 Speak(text)

         elif 'europe' in name:
             os.startfile('')
             book = open('','')
             pdfreader = PyPDF2.PdfFileReader(book)
             pages = pdfreader.getNumPages()
             Speak(f"Number Of Pages In This Books Are {pages}")
             Speak("From Which Page I Have To Start Reading ?")
             numPage = int(input())
             page = pdfreader.getPage(numPage)
             text = page.extractText()
             Speak("In Which Language , I Have To Read ?")
             lang = takecommand()

             if 'hindi' in lang:
                 transl = Translator()
                 textHin = transl.translate(text,'hi')
                 textm = textHin.text
                 speech = gTTS(text = textm )
                 try:

                     speech.save('book.mp3')
                     playsound('book.mp3')

                 except:
                     playsound('book.mp3')

             else:
                 Speak(text)
