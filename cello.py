import key_names
import copy
import os.path
import win32com
import speech_recognition as sr

macros = {}

#Load previous macros
if os.path.isfile("macros_stoage"):
    macros = pickle.load("macros_stoage")

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# recognize speech using Google Speech Recognition
try:
    # we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    text = r.recognize_google(audio)
    print("Google Speech Recognition thinks you said " + text)
    print(macros[text])
except sr.UnknownValueError:
    print("Could not understand speech.")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
