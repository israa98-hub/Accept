import speech_recognition as sr
from pygame import *
import winsound

'''r=sr.Recognizer()
with sr.Microphone() as source:
    print("speeek")
    audio = r.listen(source)
    try:
        text=r.recognize_google(audio)
        mixer.init()
        mixer.music.load(text)
        mixer.music.play()
        while mixer.music.get_busy():
              time.Clock().tick(2)

        print("ok")
    except:
        print("understand!!!!!!!!")


'''
mixer.init()
mixer.music.load("drum.wav")
mixer.music.play()
while mixer.music.get_busy():
   time.Clock().tick(2)
