import speech_recognition as sr

listener = sr.Recorgnizer()

try:
    with sr.Microphone as source:
        voice = listener.listen
except:
    pass