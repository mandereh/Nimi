# import speech_recognition as sr
# import pyttsx3
# import pywhatkit
# import time

# listener = sr.Recognizer()
# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)
# def talk(text):
#     engine.say(text)
#     engine.runAndWait()
# def take_command():
#     try:
#         with sr.Microphone as source:
#             voice = listener.listen(source)
#             command = listener.recognize_google(voice)
#             command = command.lower()
#             if 'alexa' in command:
#                 command = command.replace('alexa','')
#                 talk(command)
#     except:
#         pass
#     return command
# def run_alexa():
#     command = take_command()
#     print(command)
#     if 'play' in command:
#         song = command.replace('play','')
#         talk('playing'+song)
#         pywhatkit.playonyt('song')
#     elif 'time' in command:
#         time.datetime.datetime.now().strftime('%I:%M:%p')
#         print('time')
#         talk('Current time is'+time)
        
# run_alexa()


import speech_recognition as sr
import pyttsx3
import pywhatkit
import time

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    command = None
    try:
        with sr.Microphone as source:
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa','')
                talk(command)
    except:
        pass
    if command is not None:
        return command

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play','')
        talk('playing'+song)
        pywhatkit.playonyt('song')
    elif 'time' in command:
        current_time = time.datetime.datetime.now().strftime('%I:%M:%p')
        print(current_time)
        talk('Current time is'+current_time)

run_alexa()
