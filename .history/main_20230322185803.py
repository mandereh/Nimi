import speech_recognition as sr

listener = sr.Recognizer()

try:
    with sr.Microphone as source:
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        if 'alexa'
        print(command)
except:
    pass