import pyttsx3 
from datetime import date
from threading import current_thread
from ui import Ui_Jaadu_Ui
from PyQt5 import QtCore , QtGui , QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt , QTimer , QTime , QDate
import speech_recognition as sr
import os
import sys
sys.path.append('F://Jaadu')

gui=Ui_Jaadu_Ui()

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
class MainThread(QThread):

    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        gui

startExe = MainThread() 

class Gui_Start(QMainWindow):
    
    def __init__(self):
        super().__init__()

        self.gui = Ui_Jaadu_Ui()
        self.gui.setupUi(self)

        self.gui.Start.clicked.connect(self.startTask)
        self.gui.Quit.clicked.connect(self.close)
        
    def startTask(self):
        
        self.gui.label1 = QtGui.QMovie("F:\\Jaadu\\Gui\\Gui Material\\Gif_1.gif")
        self.gui.Gif_1.setMovie(self.gui.label1)
        self.gui.label1.start()
        
        self.gui.label2 = QtGui.QMovie("F:\\Jaadu\\Gui\\Gui Material\\Gif_2.gif")
        self.gui.Gif_2.setMovie(self.gui.label2)
        self.gui.label2.start()
        
        self.gui.label3 = QtGui.QMovie("F:\\Jaadu\\Gui\\Gui Material\\Gif_3.gif")
        self.gui.Gif_3.setMovie(self.gui.label3)
        self.gui.label3.start()
        
        self.gui.label4 = QtGui.QMovie("F:\\Jaadu\\Gui\\Gui Material\\Gif_4.gif")
        self.gui.Gif_4.setMovie(self.gui.label4)
        self.gui.label4.start()
        
        self.gui.label5 = QtGui.QMovie("F:\\Jaadu\\Gui\\Gui Material\\Gif_5.gif")
        self.gui.Gif_5.setMovie(self.gui.label5)
        self.gui.label5.start()
        
        self.gui.label6 = QtGui.QMovie("F:\\Jaadu\\Gui\\Gui Material\\Gif_6.gif")
        self.gui.Gif_6.setMovie(self.gui.label6)
        self.gui.label6.start()
        
        self.gui.label7 = QtGui.QMovie("F:\\Jaadu\\Gui\\Gui Material\\Gif_7.gif")
        self.gui.Gif_7.setMovie(self.gui.label7)
        self.gui.label7.start()
        
        self.gui.label8 = QtGui.QMovie("F:\\Jaadu\\Gui\\Gui Material\\Gif_8.gif")
        self.gui.Gif_8.setMovie(self.gui.label8)
        self.gui.label8.start()
        
        self.gui.label9 = QtGui.QMovie("F:\\Jaadu\\Gui\\Gui Material\\Gif_9.gif")
        self.gui.Gif_9.setMovie(self.gui.label9)
        self.gui.label9.start()
        
        timer=QTimer(self)
        timer.timeout.connect(self.showTimeLive)
        timer.start(999)

        startExe.start()
        import mainjaadu
        mainjaadu.TaskExe()

    def showTimeLive(self):
        t_ime = QTime.currentTime()
        time = t_ime.toString()
        d_ate = QDate.currentDate()
        date = d_ate.toString()
        
        label_Time = "Time :" + time
        label_Date = "Date :" + date


        self.gui.Text_Time.setText(label_Time)
        self.gui.Text_Date.setText(label_Date)

GuiApp = QApplication(sys.argv)
jaadu_gui = Gui_Start()
jaadu_gui.show()
exit(GuiApp.exec_())
