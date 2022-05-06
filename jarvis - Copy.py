from re import search
from urllib import request
from numpy import take
from pyautogui import click
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import subprocess as sp
from time import sleep


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
#print(voices)
engine.setProperty("voice", voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
       speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("Hello! Riya here!.  How can i help you, syam!")


    
    
    

def openapps():
    
    if "audacity" in query:
        sp.Popen("C:\\Program Files\\Audacity\\Audacity.exe")  
    if "gmail" in query:
        sp.Popen("C:\\Program Files\\Google\Chrome\\Application\\chrome_proxy.exe  --profile-directory=Default --app-id=pjkljhegncpnkpknbcohdijeoejaedia")
    if "youtube" in query:
        sp.Popen("C:\\Program Files\\Google\\Chrome\\Application\chrome_proxy.exe  --profile-directory=Default --app-id=blpcfgokakmgnkcojhhkbfbldkacnbeo")
    if "chrome" in query:
        sp.Popen("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
    if "whatsapp" in query:
        sp.Popen("C:\\Users\\Veda\\AppData\\Local\\WhatsApp\\WhatsApp.exe")  
    if "main page" in query:
        sp.Popen("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
        sleep(10)
        click(x=965, y=672)
        sleep(5)
        click(x=1339, y=490)
        sleep(5)
        click(x=205, y=124)
        sleep(3)
        click(x=125, y=605)
    
        
def OnlineClass(Subject):
    
    if "English" in Subject:
        from OnlineClasses.Links import English
        Link = English()
        
        webbrowser.open(Link)
        speak("please wait sir while i connect you to Google meet!")
        sleep(20)
        click(x=707, y=765)
        sleep(3)
        click(x=611, y=766)
        sleep(2)
        click(x=1122, y=664)
        sleep(1)
        click(x=1349, y=534)
        speak("Waiting for venkataramana sir to admit you sir !")
        
    elif "environment" in Subject:
        from OnlineClasses.Links import Environment
        Link = Environment()
        
        webbrowser.open(Link)
        speak("please wait sir connecting you to Google meet!")
        sleep(20)
        click(x=707, y=765)
        sleep(3)
        click(x=611, y=766)
        sleep(2)
        click(x=1122, y=664)
        sleep(1)
        click(x=1349, y=534)
        speak("Waiting for Maha bala sir to admit you sir !")
        
    
    elif "analytical technique" in Subject:
        from OnlineClasses.Links import ATM
        Link = ATM()
        
        webbrowser.open(Link)
        speak("Please wait sir. Connecting you to Teams!")
        sleep(20)
        click(x=954, y=420)
        sleep(18)
        click (x=568, y=509)
        sleep(2)
        click (x=722, y=506)
        sleep(2)
        click (x=793, y=464)
        speak("Joining the Chandru sir's class!")
    
    elif "organizational" in Subject:
        from OnlineClasses.Links import Organisational
        Link = Organisational()
        
        webbrowser.open(Link)
        speak("Please wait sir. Connecting you to Teams!")
        sleep(20)
        click(x=954, y=420)
        sleep(18)
        click (x=568, y=509)
        sleep(2)
        click (x=722, y=506)
        sleep(2)
        click (x=793, y=464)        
        speak("Joining Manohar sir's class!")
   
    elif "economics" in Subject:
        from OnlineClasses.Links import Economics
        Link = Economics()
        
        webbrowser.open(Link)
        speak("Please wait sir. while i Connect you to Teams!")
        sleep(20)
        click(x=954, y=420)
        sleep(18)
        click (x=568, y=509)
        sleep(2)
        click (x=722, y=506)
        sleep(2)
        click (x=793, y=464)
        
        speak("Joining Vinod sir's class")
    
    elif "accounts" in Subject:
        from OnlineClasses.Links import Tally
        Link = Tally()
        
        webbrowser.open(Link)
        speak("Please wait sir. Connecting you to Teams!")
        sleep(20)
        click(x=954, y=420)
        sleep(18)
        click (x=568, y=509)
        sleep(2)
        click (x=722, y=506)
        sleep(2)
        click (x=793, y=464)
        
        speak("Joining Warden sir's class!.")
    
    elif "second" in Subject:
        from OnlineClasses.Links import Add
        Link = Add()
        
        webbrowser.open(Link)
        speak("Please wait sir. Connecting you to Teams!")
        sleep(20)
        click(x=1225, y=512)
        sleep(18)
        click (x=838, y=680)
        sleep(2)
        click (x=949, y=679)
        sleep(2)
        click (x=1102, y=618)
        speak("Joining additional english class sir!")
        
    
    

def takeCommand():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-ind")
        print(f"You said : {query}\n")

    except Exception as e:
        print(e)
        print("Say that again....")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:        
        query = takeCommand().lower()

          
        if 'wikipedia' in query:
           speak('searching Wikipedia...')
           query = query.replace("wikipedia", "")
           results = wikipedia.summary(query, sentences=2)
           speak("According to Wikipedia")
           print(results)
           speak(results)
                        
        elif 'open instagram' in query:
            speak("Opening instagram, please wait sir!")
            webbrowser.open("instagram.com")
        elif "attendance" in query:
            speak ("opening L.M.S. attendance page!")
            webbrowser.open("https://lms.sssihl.edu.in/mod/attendance/view.php?id=48524")
            sleep(10)
            click(x=1311, y=471)
        elif 'play music' in query:
            speak("hello i am syam sundar")
            music_dir = 'C:\songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S:")
            speak(f"Sir, the time is {strTime}")
        elif "audacity" in query:
            speak("opening audacity please wait sir!")
            openapps()
        elif "whatsapp" in query:
            speak("opening whatsapp. please wait sir!")
            openapps()
        
        elif "gmail" in query:
            speak ("opening gmail")
            openapps()
        elif "youtube" in query:
            speak ("opening youtube! please wait sir.")
            openapps()
        elif "chrome" in query:
            speak ("opening chrome")
            openapps()
        elif "main page" in query:
            speak("opening MDH main page!")
            openapps()
        elif "story" in query:
           click(x=34, y=1048)
           sleep(2)
           click(x=443, y=966)
           sleep(5)
           click(x=1225, y=32)
           sleep(2)
           click(x=443, y=211)
           speak("instagram status!")
        elif "instagram message" in query:
           sleep(1)
           click(x=34, y=1048)
           sleep(3)
           click(x=443, y=966)
           sleep(7)
           click(x=1225, y=32)
           sleep(2)
           click(x=1282, y=76)
           
            
        
           
        elif "online" in query:
            
            from jarvis import OnlineClass
            speak("Tell me the subject name sir!")
            
            Class = takeCommand()
            
            OnlineClass(Class)
           
            

        elif 'break' in query:
            speak("Ok Sir , You can call me anytime !")
            speak('Just say Hello Susan!')
            break
        

        
        
         
        
            



        



