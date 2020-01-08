import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS

def speek(text):
    tts=gTTS(text=text,lang="en")
    filename="voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)
speek("princess")

