import speech_recognition as sr
import sounddevice as sd
from scipy.io.wavfile import write
from playsound import playsound
def funcVoice():

    fs = 44100  # Sample rate
    seconds = 3  # Duration of recording
    print("seeey")
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()  # Wait until recording is finished
    file="x.wav"
    write(file, fs, myrecording)  # Save as WAV file
    playsound(file)


funcVoice()