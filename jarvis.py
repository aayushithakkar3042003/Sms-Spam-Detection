import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests
recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "46883fd8472f40f9b85cf1a1a667fa5e"

def speak(text):
    engine.say(text)
    engine.runAndWait()
def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(' ')[1]
        link = musiclibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey")
        
        
        
    
if __name__ =='__main__':
    speak("Initializing Jarvis....")
    while True:
        # listen the word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()
        
        print("recognizing....")
        try:       
            with sr.Microphone() as source:
                print("Listening ...")
                audio = r.listen(source,timeout= 2,phrase_time_limit= 1)
            word  = r.recognize_google(audio)
            print(word)
            if(word.lower()=="jarvis"):
                speak("Ya")
                 # listen the command
                with sr.Microphone() as source:
                    print("Jarvis active...")
                    audio = r.listen(source,timeout=2,phrase_time_limit=1)
                    command = r.recognize_google(audio)
                    processCommand(command)
                
                 
            print(command)
        except Exception as e:
         print("Error {0}".format(e))
        # except sr.RequestError as e:
        #     print("google error : {0}".format(e))
        # 9:45 minutes
    