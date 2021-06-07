import speech_recognition as sr
import pyowm
import random
import os
import webbrowser
import pyttsx3
from Keys import OPENWEATHER
from datetime import date, timedelta, datetime
import asyncio

SEARCH_WORDS = {'who': 'who', 'what': 'what', 'when': 'when', 'where': 'where', 'why': 'why', 'how': 'how'}

recognizer = sr.Recognizer()
microphone = sr.Microphone()

engine = pyttsx3.init()
engine.setProperty('volume', 5.0)

WakeWord = 'Jarvis'

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
                s.speak("I am Jarvis. I'm a digital assistant created by Luca D'Ealessandris.")

            elif "open" in command:
                s.open_things(command)


            elif "good morning" in command:
                today = date.today()
                now = datetime.now()
                home = 'New York'
                owm = pyowm.OWM(OPENWEATHER)
                mgr = owm.weather_manager()
                observation = mgr.weather_at_place(home)
                w = observation.weather
                temp = w.temperature('celsius')
                status = w.detailed_status
                s.speak("Good morning Luca, it is currently " + now.strftime("%I") + now.strftime("%M") + now.strftime("%p"))
                s.speak("The temperature outside is currently " + str(int(temp['temp'])) + " degrees celsius and " + status)

            elif "how are you" in command:
                current_feelings = ["I'm okay.", "I'm doing well. Thank you.", "I am doing okay."]
                greeting = random.choice(current_feelings)
                s.speak(greeting)

            elif "time" in command:
                now = datetime.now()
                s.speak("It is currently " + now.strftime("%I") + now.strftime("%M") + now.strftime("%p"))

            elif "weather" in command:
                home = 'New York'
                owm = pyowm.OWM(OPENWEATHER)
                mgr = owm.weather_manager()
                observation = mgr.weather_at_place(home)
                w = observation.weather
                temp = w.temperature('celsius')
                status = w.detailed_status
                s.speak("The temperature outside is currently " + str(int(temp['temp'])) + " degrees celsius and " + status)

            elif "temperature" in command:
                home = 'New York'
                owm = pyowm.OWM(OPENWEATHER)
                mgr = owm.weather_manager()
                observation = mgr.weather_at_place(home)
                w = observation.weather
                temp = w.temperature('celsius')
                status = w.detailed_status
                s.speak("The temperature outside is currently " + str(int(temp['temp'])) + " degrees celsius and " + status)
            
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

s = Jarvis()

while True:
    command = s.listen(recognizer, microphone)
    if command == None:
        return       
    else:
        s.analyze(command)