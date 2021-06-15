import datetime
import os
import time
import subprocess
import pyjokes as pyjokes
import pyautogui
import sys
import speech_recognition as sr
import pyttsx3
import pyaudio
import wikipedia
import webbrowser
from tkinter import *

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voices',voices[1].id)

def speak(audio):
        engine.say(audio)
        engine.runAndWait()
def wishme():
        hour =int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            print("good morning sir")
            speak("good morning sir")
        elif hour >= 12 and hour<18:
            print("good afternoon sir")
            speak("good afternoon sir")
        else:
            print("good evening sir")
            speak("good evening sir")

        print("i am  your assistant ! how can i help you")
        speak(" i am  your assistant ! how can i help you")
def takeCommand():
    # it take microphone input from the user and return string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening..........")
        r.pause_threshold= 1
        #r.energy_threshold=200
        audio = r.listen(source)
    try:
        print("recognizing........")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said : {query}\n")
    except Exception as e:
        print("say that again pls......")
        speak("say that again pls.....")
        return "none"
    return query




if __name__ =="__main__":
    wishme()
    while True:
      query=takeCommand().lower()
      if 'wikipedia' in query:
          speak("searching wikipedia....")
          query=query.replace("wikipedia", "")
          results= wikipedia.summary(query,sentences=2)
          print("according to wikipedia")
          speak("according to wikipedia")
          print(results)
          speak(results)



      elif "open youtube" in query:
          webbrowser.open("youtube.com")

      elif "open gmail" in query:
          webbrowser.open("www.gmail.com")

      elif "open stackoverflow" in query:
          webbrowser.open("stackoverflow.com")

      elif "open github" in query:
          webbrowser.open("github.com")

      elif "open drive" in query:
          webbrowser.open("drive.com")

      elif "open classroom" in query:
          webbrowser.open("classroom.com")

      elif "open google" in query:
          webbrowser.open("google.com")

      elif 'covid-19 tracker' in query:
          webbrowser.open(
              "https://news.google.com/covid19/map?hl=en-IN&gl=IN&ceid=IN%3Aen"
          )
          speak("covid-19 tracker is open now")
          time.sleep(5)

      elif 'top engineering colleges in india' in query or 'indian engineering college' in query or 'engineering college' in query:
          webbrowser.open_new_tab(
              "https://www.shiksha.com/b-tech/ranking/top-engineering-colleges-in-india/44-2-0-0-0"
          )
          speak("Colleges as per NIRF Ranking are open on Shiksha website!")
          time.sleep(2)

      elif 'top medical colleges in india' in query or 'medical colleges in india' in query or 'medical college' in query:
          speak('Here are some top Medical Colleges in India')
          webbrowser.open_new_tab(
              "https://medicine.careers360.com/colleges/ranking")
          speak("Colleges as per NIRF rankings are opened!")
          time.sleep(2)

      #elif "camera" in query or "take a photo" in query:
          #ec.capture(0, "robo camera", "img.jpg")

      elif 'search' in query:
          query = query.replace("search", "")
          webbrowser.open_new_tab(query)
          time.sleep(5)

      elif 'play music' in query:
          music_dir = 'D:\\favsong\\muc'
          songs = os.listdir(music_dir)
          print(songs)
          os.startfile(os.path.join(music_dir,songs[0]))



      elif 'cmd' in query or 'command prompt' in query or 'terminal' in query:
          os.system("start cmd")

      elif 'volume up' in query or 'increase volume' in query:
          pyautogui.press('volumeup')

      elif 'volume down' in query or 'decrease volume' in query or 'lower the volume' in query:
          pyautogui.press('volumedown')

      elif 'volume mute' in query or 'turn off the volume' in query or 'mute' in query:
          pyautogui.press('volumemute')

      elif 'jokes' in query or 'joke' in query:
          joke = pyjokes.get_joke('en', 'all')
          print(joke)
          speak(joke)

      elif "notepad" in query:
          speak("Opening Notepad")
          os.system("start Notepad")

      elif "outlook" in query:
          speak("Opening Microsoft Outlook")
          os.system("start outlook")

      elif "word" in query:
          speak("Opening Word")
          os.system("start winword")

      elif "paint" in query:
          speak("Opening Paint")
          os.system("start mspaint")

      elif "excel" in query:
          speak("Opening Excel")
          os.system("start excel")

      elif "open chrome" in query:
          speak("Opening Google Chrome")
          os.system("start chrome")

      elif "calculator" in query:
          speak("Opening Calculator")
          os.system("start calc")

      elif "log off" in query or "sign out" in query or "shut down" in query:
          speak(
              "Ok , your pc will log off in 10 sec make sure you exit from all applications"
          )
          print("Ok , your pc will log off in 10 sec make sure you exit from all applications ")
          subprocess.call(["shutdown", "/l"])
          time.sleep(3)

      elif 'exit' in query:
          sys.exit("exit")
          speak("Ok sir, Take Care.")

