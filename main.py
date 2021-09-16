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

city = settings["city"]
startup = settings["startup"]
botname = settings["botname"]

WakeWord = botname

class Friday:
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
                bot.speak(f"I am {botname}. I'm a digital assistant created by DefaultModels.")

            elif "open" in command:
                bot.open_things(command)

            elif "good morning" in command:
                now = datetime.now()
                home = city
                owm = pyowm.OWM(os.environ['OPENWEATHER'])
                mgr = owm.weather_manager()
                observation = mgr.weather_at_place(home)
                w = observation.weather
                temp = w.temperature('celsius')
                status = w.detailed_status
                bot.speak(f"Good morning, it is currently " + now.strftime("%I") + now.strftime("%M") + now.strftime("%p"))
                bot.speak("The temperature outside is currently " + str(int(temp['temp'])) + " degrees celsius and " + status)

            elif "how are you" in command:
                current_feelings = ["I'm okay.", "I'm doing well. Thank you.", "I am doing okay."]
                greeting = random.choice(current_feelings)
                bot.speak(greeting)

            elif "time" in command:
                now = datetime.now()
                bot.speak("It is currently " + now.strftime("%I") + now.strftime("%M") + now.strftime("%p"))

            elif "weather" in command:
                home = city
                owm = pyowm.OWM(os.environ['OPENWEATHER'])
                mgr = owm.weather_manager()
                observation = mgr.weather_at_place(home)
                w = observation.weather
                temp = w.temperature('celsius')
                status = w.detailed_status
                bot.speak("The temperature outside is currently " + str(int(temp['temp'])) + " degrees celsius and " + status)

            elif "temperature" in command:
                home = city
                owm = pyowm.OWM(os.environ['OPENWEATHER'])
                mgr = owm.weather_manager()
                observation = mgr.weather_at_place(home)
                w = observation.weather
                temp = w.temperature('celsius')
                status = w.detailed_status
                bot.speak("The temperature outside is currently " + str(int(temp['temp'])) + " degrees celsius and " + status)
            
            # keep in end
            elif SEARCH_WORDS.get(command.split(' ')[1]) in command:
                bot.speak("Here's what I found.")
                webbrowser.open("https://www.google.com/search?q={}".format(command[7:]))

            else:
                bot.speak("I don't know how to do that yet.")

        except TypeError:
            bot.speak("I don't know how to do that yet")
            print("Warning: You're getting a TypeError somewhere.")
            pass
        except AttributeError:
            print("Warning: You're getting an Attribute Error somewhere.")
            pass

    def open_things(self, command):
        if "youtube" in command:
            bot.speak("Opening YouTube.")
            webbrowser.open("https://www.youtube.com/")
            pass

        elif "pronote" in command:
            bot.speak("Opening Pronote.")
            webbrowser.open("https://4040004j.index-education.net/pronote/eleve.html")
            pass

        elif "gmail" in command:
            bot.speak("Opening gmail.")
            webbrowser.open("https://mail.google.com/mail/u/1/#inbox")
            pass

        elif "calendar" in command:
            bot.speak("Opening calendar.")
            webbrowser.open("https://calendar.google.com/calendar/u/1/r/day?pli=1")
            pass

        elif "discord" in command:
            bot.speak("Opening discord.")
            webbrowser.open("https://discord.com/channels/@me/")
            pass

        elif "classroom" in command:
            bot.speak("Opening classroom.")
            webbrowser.open("https://classroom.google.com/u/1/h")
            pass

        elif "minecraft" in command:
            bot.speak("Opening minecraft.")
            os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Minecraft Launcher\Minecraft Launcher.lnk")
            pass

        elif "steam" in command:
            bot.speak("Opening Steam.")
            os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Steam\Steam.lnk")
            pass

        elif "google" in command:
            bot.speak("Opening google chrome.")
            os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome.lnk")
            pass

        else:
            webbrowser.open("https://www.google.com/search?q={}".format(command[12:]))
            pass
            
    def run():
      command = bot.listen(recognizer, microphone)
          
      if command == None:
        bot.run()
      else:
        if startup == "True":
          def setup():
            settings["startup"] = "False"
            
            bot.speak("Hi there! I'm your new assistant. What would you like to call me?")
            response = bot.listen(recognizer, microphone)
            settings["botname"] = response

            bot.speak(f"Great! In what city do you live in?")
            response = bot.listen(recognizer, microphone)
            settings["city"] = response

            botname = settings["botname"]
            city = settings["city"]

            bot.speak(f"From now on you will call me {botname} and you live in {city}, is everything right? Answer with yes or no.")
            response = bot.listen(recognizer, microphone)
            
            if response == "Yes":
              bot.speak("Great! I will now restart and you will be able to use me afterwards!")
              quit()
            
            else:
              bot.setup()
        
        else:
          bot.analyze(command)
          bot.run()

bot = Friday()
bot.run()