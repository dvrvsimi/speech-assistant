# speech-assistant
**hello there!**

this project is easy to run and doesn't require APIs, just ensure that all the dependencies in `requirements.txt` are properly installed. To install all dependencies at once, run `pip install -r requirements.txt` on your terminal

the program uses the `speech_recognition` package to recognize audio input and gets a response depending on the input. The `webbrowser` package allows the program get information from the internet and is triggered by certain prompts.

remember that the `gTTS` in `sppech.py` was configured to `lang='en'`, please look up `gTTS` to configure it to your preference.

for now, there are only response triggers for these prompts:
* hello
* what is your name
* what is today's date
* search
* location
* song
* bye

## note:
they are voice prompt so you just have to say them as clearly as possible into your mic or else the program returns an `UnknownValueError`. Ensure to be connected to stable internet to avoid running into `RequestError`.
