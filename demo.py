from vosk import Model, KaldiRecognizer
import pyttsx3
import datetime
import pyaudio
import os
import msvcrt as m
import random





def wait():
    m.getch()


APRIL = pyttsx3.init('sapi5')
voice = APRIL.getProperty('voices')
assistant_voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_enUS_EvaM'
rate = APRIL.getProperty('rate')
APRIL.setProperty('rate', 170)
voices = APRIL.getProperty('voices')
APRIL.setProperty('voice', assistant_voice_id)


def speak(audio):
    print('APRIL: ' + audio)
    APRIL.say(audio)
    APRIL.runAndWait()


k1 = ["loading data, this may take some time", "loading models, this usualy take some time"]
rand = random.choice(k1)
speak(rand)

model = Model(r"C:\Users\dutta\PycharmProjects\happy\vosk-model-small-en-in-0.4")
recognizer = KaldiRecognizer(model, 16000)
cap = pyaudio.PyAudio()
stream = cap.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()
a = 0


def command():
    print("")
    print("Listening...")
    print("")

    while True:

        data = stream.read(4000, exception_on_overflow=False)

        if recognizer.AcceptWaveform(data):
            text = recognizer.Result()
            p = text[14:-3]
            print(f"You Said : {p}")
            if len(p) > 0:
                return p

            else:
                print('Sorry, I did\'t get that. :( Try typing the command, (tips: type 10 instead of "ten") ')
                query = str(input('your favor is: '))
                return query


def asmit():
    while True:

        query = command().lower()
        a5 = ["hi"]

        if query in a5:
            print("hi")


        elif "time" in query:
            Time = datetime.datetime.now().strftime('%I %M %p')
            speak('It is')
            speak(Time)
asmit()