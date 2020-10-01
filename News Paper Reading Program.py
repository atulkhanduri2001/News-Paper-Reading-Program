import requests
import json  # {java script object notation}. Used to read javascript variables easly.
# transfer data between a server and a client.
from datetime import datetime
import time
import pygame

# pygame.mixer.init()
# pygame.mixer.music.load('water.mp3')
# pygame.mixer.music.play()

t = 3
time.sleep(t)


def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)


if __name__ == '__main__':

    speak("Hello... Please enter your name:")

    pp = input("Please enter your name:\n")
    t = 1
    time.sleep(t)
    speak(
        f"There is no need to rush.... What is meant for you arrives on time.... Welcome back to Sinister's News Corporation {pp} ......Hope you are having a great day ....... Lets make you updated about whats happening around you......")
    speak("Lets Start with our first news")
    url = "https://newsapi.org/v2/top-headlines?q=trump&apiKey=bf9763caddb74b1da4b8a0c16b53652a"
    news = requests.get(url).text
    news_dict = json.loads(news)
    arts = news_dict['articles']
    for article in arts:
        speak(article['description'])
        print(article['description'])
        t = 1
        time.sleep(t)
        speak("Moving on to the next news...\n")

    speak(f"Thanks for joining us . Have a great day {pp}..\n")
