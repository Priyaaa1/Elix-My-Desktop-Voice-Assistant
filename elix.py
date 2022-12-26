import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id) 



def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
    
    
def greeting():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning")
    elif hour>=12 and hour<18:
        speak("Good afternoon")
    else:
        speak("Good evening")
    
    speak("Hope you are good. My name is Elix, I am a voice assistant developed by Pritam Singh. Please tell me How may I help you ?")
    


def inputcommand(): #It will take input or listen from the user's microphone and return string output
    
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..... Please say something")
        r.pause_threshold    # seconds of non-speaking audio before a phrase is considered complete
        audio=r.listen(source)
    
    try:
        print("Recognizing ..... Hold on")
        query=r.recognize_google(audio, language='en-in')
        print(f'You said : {query}\n')  #use of f-string
    
    except Exception as e:
        #print(e)
        print("It was not you, it was me..... Please say that again.")
        return "None"
    
    return query
        
if __name__=="__main__":
    greeting()
    
    while True:
        query = inputcommand().lower()  
    
    #logics for executing the different tasks
        if 'wikipedia' in query:
            speak('Searching wikipedia.......')
            query=query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            speak(results)
            
        elif 'open google' in query:
            webbrowser.open("google.com")
            
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
    