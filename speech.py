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

def luna_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 100000000)
    audio = 'audio.' + str(r) + '.mp3'
    tts.save(audio)
    playsound.playsound(audio)
   # print(audio_string)
    os.remove(audio)
name = record('what is your name? ')
print('hello ' + name)
def respond(voice_data):
    if 'hello' in voice_data:
        print('hi there, ' + 'name')
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
        print('here\'s a map showing ' + location)
    if 'song' in voice_data:
        song = record('what song would you like to listen to?')
        webbrowser.get().open(url='https://streamsquid.com/#/search/' + song + '&amp;')
        print('here\'s a streaming platform playing ' + song)
    if 'bye' in voice_data:
        print('bye human!')
        exit()


time.sleep(1)
print('how can i help you?')
while 1:
    voice_data = record()
    respond(voice_data)
