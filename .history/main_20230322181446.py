import speech_recognition as sr

listener = sr.Recorgnizer()

try:
    with sr.Microphone as source:
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        print(command)
except:
    pass