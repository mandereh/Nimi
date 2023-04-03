import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

class Alexa:
    
    def __init__(self) -> None:
            self.listener = sr.Recognizer()
            self.engine = pyttsx3.init()
            self.voices = self.engine.getProperty('voices')
            self.engine.setProperty('voice',self.voices[1].id)
            
            
    def talk(self,text):
        self.engine.say(text)
        self.engine.runAndWait()
        
        
    def take_command(self):
        try:
            with sr.Microphone() as source:
                print('listening....')
                voice = self.listener.listen(source)
                command = self.listener.recognize_google(voice)
                command = command.lower()
                if 'alexa' in command:
                    command = command.replace('alexa','')
                    print(command)
        except:
            command = ''
        return command
    
    def run(self):
        while True:
            command = self.take_command()
            print(command)
            if 'play' in command:
                song = command.replace('play','')
                self.talk('playing'+song)
                pywhatkit.playonyt(song)
            elif 'time' in command:
                time = datetime.datetime.now().strftime('%I:%M %p')
                self.talk('current time is '+ time)
            elif 'who is' in command:
                person = command.replace('who is', '')
                info = wikipedia.summary(person, 1)
                print(info)
                self.talk(info)
            elif 'date' in command:
                date = datetime.date.today().strftime('%Y-%m-%d')
                self.talk(date)
            elif 'are you single' in command:
                self.talk('I am in a relationship with wifi')
            elif 'joke' in command:
                self.talk(pyjokes.get_joke())
            else:
                self.talk('Please say the command again.')
                
if __name__ == "__main__":
    alexa = Alexa()
    alexa.run()
            
        
        
            