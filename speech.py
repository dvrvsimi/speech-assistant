import speech_recognition as sr 
import webbrowser
import time
import playsound
import os
import random
from gtts import gTTS
from time import ctime

r = sr.Recognizer()

def record(ask = False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            print('sorry, i didn\'t get that')
        except sr.RequestError:
            print('sorry, my server is down')
        return voice_data

def respond(voice_data):
    if 'hello' in voice_data:
        print('hi there, human')
    if 'what is your name' in voice_data:
        print('my name is luna')
    if "what is today's date" in voice_data:
        print(ctime())
    if 'search' in voice_data:
        search = record('what do you want to search for?')
        webbrowser.get().open(url='https://google.com/search?q=' + search)
        print('here\'s what i could find on ' + search)
    if 'location' in voice_data:
        location = record('where do you want to search for?')
        webbrowser.get().open(url='https://google.nl/maps/place/' + location + '&amp;')
        print('here\'s your search on ' + location)
    if 'bye luna' in voice_data:
        print('bye human!')
        exit()


time.sleep(1)
print('how can i help you?')
while 1:
    voice_data = record()
    respond(voice_data)
