import speech_recognition as sr
import pyowm
import random
import os
import webbrowser
import pyttsx3
from datetime import datetime
import json

SEARCH_WORDS = {'who': 'who', 'what': 'what', 'when': 'when', 'where': 'where', 'why': 'why', 'how': 'how'}

recognizer = sr.Recognizer()
microphone = sr.Microphone()

engine = pyttsx3.init()
engine.setProperty('volume', 5.0)

with open('settings.json') as f:
    settings = json.load(f)

username = settings["username"]
city = settings["city"]
startup = settings["startup"]
botname = settings["botname"]

WakeWord = botname

class Jarvis:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

    def speak(self, text):
        engine.say(text)
        engine.runAndWait()

    def listen(self, recognizer, microphone):
            try:
                with microphone as source:
                    recognizer.adjust_for_ambient_noise(source)
                    recognizer.dynamic_energy_threshold = 3000
                    audio = recognizer.listen(source, timeout=100000)
                    response = recognizer.recognize_google(audio)

                    if WakeWord in response:
                        return response.lower()

                    else:
                        pass
            except sr.WaitTimeoutError:
                pass
            except sr.UnknownValueError:
                pass
            except sr.RequestError:
                print("Network error.")

    def analyze(self, command):
        try:
            print(command)
            if "introduce yourself" in command:
                s.speak(f"I am {botname}. I'm a digital assistant created by Luca D'Ealessandris.")

            elif "open" in command:
                s.open_things(command)

            elif "good morning" in command:
                now = datetime.now()
                home = city
                owm = pyowm.OWM(os.environ['OPENWEATHER'])
                mgr = owm.weather_manager()
                observation = mgr.weather_at_place(home)
                w = observation.weather
                temp = w.temperature('celsius')
                status = w.detailed_status
                s.speak(f"Good morning {username}, it is currently " + now.strftime("%I") + now.strftime("%M") + now.strftime("%p"))
                s.speak("The temperature outside is currently " + str(int(temp['temp'])) + " degrees celsius and " + status)

            elif "how are you" in command:
                current_feelings = ["I'm okay.", "I'm doing well. Thank you.", "I am doing okay."]
                greeting = random.choice(current_feelings)
                s.speak(greeting)

            elif "time" in command:
                now = datetime.now()
                s.speak("It is currently " + now.strftime("%I") + now.strftime("%M") + now.strftime("%p"))

            elif "weather" in command:
                home = city
                owm = pyowm.OWM(os.environ['OPENWEATHER'])
                mgr = owm.weather_manager()
                observation = mgr.weather_at_place(home)
                w = observation.weather
                temp = w.temperature('celsius')
                status = w.detailed_status
                s.speak("The temperature outside is currently " + str(int(temp['temp'])) + " degrees celsius and " + status)

            elif "temperature" in command:
                home = city
                owm = pyowm.OWM(os.environ['OPENWEATHER'])
                mgr = owm.weather_manager()
                observation = mgr.weather_at_place(home)
                w = observation.weather
                temp = w.temperature('celsius')
                status = w.detailed_status
                s.speak("The temperature outside is currently " + str(int(temp['temp'])) + " degrees celsius and " + status)
            
            # keep in end
            elif SEARCH_WORDS.get(command.split(' ')[1]) in command:
                s.speak("Here's what I found.")
                webbrowser.open("https://www.google.com/search?q={}".format(command[7:]))

            else:
                s.speak("I don't know how to do that yet.")

        except TypeError:
            s.speak("I don't know how to do that yet")
            print("Warning: You're getting a TypeError somewhere.")
            pass
        except AttributeError:
            print("Warning: You're getting an Attribute Error somewhere.")
            pass

    def open_things(self, command):
        if "youtube" in command:
            s.speak("Opening YouTube.")
            webbrowser.open("https://www.youtube.com/")
            pass

        elif "pronote" in command:
            s.speak("Opening Pronote.")
            webbrowser.open("https://4040004j.index-education.net/pronote/eleve.html")
            pass

        elif "gmail" in command:
            s.speak("Opening gmail.")
            webbrowser.open("https://mail.google.com/mail/u/1/#inbox")
            pass

        elif "calendar" in command:
            s.speak("Opening calendar.")
            webbrowser.open("https://calendar.google.com/calendar/u/1/r/day?pli=1")
            pass

        elif "discord" in command:
            s.speak("Opening discord.")
            webbrowser.open("https://discord.com/channels/@me/")
            pass

        elif "classroom" in command:
            s.speak("Opening classroom.")
            webbrowser.open("https://classroom.google.com/u/1/h")
            pass

        elif "minecraft" in command:
            s.speak("Opening minecraft.")
            os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Minecraft Launcher\Minecraft Launcher.lnk")
            pass

        elif "steam" in command:
            s.speak("Opening Steam.")
            os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Steam\Steam.lnk")
            pass

        elif "google" in command:
            s.speak("Opening google chrome.")
            os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome.lnk")
            pass

        else:
            webbrowser.open("https://www.google.com/search?q={}".format(command[12:]))
            pass
            
    def run():
      command = s.listen(recognizer, microphone)
          
      if command == None:
        s.run()
      else:
        if startup == "True":
          def setup():
            settings["startup"] = "False"
            
            s.speak("Hi there! I'm your new assistant. What is your name?")
            response = s.listen(recognizer, microphone)
            settings["username"] = response
            
            s.speak(f"Hi {response}! In what city do you live in?")
            response = s.listen(recognizer, microphone)
            settings["city"] = response
            
            s.speak("Great! Finally, what would you like to call me?")
            response = s.listen(recognizer, microphone)
            settings["botname"] = response

            botname = settings["botname"]
            username = settings["username"]
            city = settings["city"]

            s.speak(f"From now on you will call me {botname}, I will call you {username} and you live in {city}, is everything right? Answer with yes or no.")
            response = s.listen(recognizer, microphone)
            
            if response == "Yes":
              s.speak("Great! I will now restart and you will be able to use me afterwards!")
              quit()
            
            else:
              s.setup()
        
        else:
          s.analyze(command)
          s.run()

s = Jarvis()
s.run()