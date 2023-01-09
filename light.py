import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import speech_recognition as sr

eng=pyttsx3.init('nsss')
voice=eng.getProperty('voice')
eng.setProperty('voice',voice)

def speak(audio):
    eng.say(audio)
    eng.runAndWait()
    
def greet():
    hour = int(datetime.datetime.now().hour)
    
    if hour>=0 and hour<=12:
        speak("Good Morning!")
    
    elif hour>12 and hour<=18:
        speak("Good Afternoon!")
    
    else:
        speak("Good Evening!")
    
    speak("Hello, this is Light. What can I do for you?")

    
def command():
    '''
    Collects voice from external microphone as an input 
    Prouduces string as an output
    '''
   
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Light is Listening...")
        speak("light is listening")
        r.adjust_for_ambient_noise(source)
        audio=r.listen(source)
    
    try:
        print("Light is understanding....")
        query=r.recognize_google(audio)
        print("User command: ",query)

    except Exception as e:
        print(e)
        print("Could you repeat that again? ...")
        speak("Could you repeat that again?")
        return "NONE"
    
    return query
        
        
if __name__=="__main__":
    greet()
    while True:
        text=command().lower()
        d = '/Applications'
        apps = list(map(lambda x: x.split('.app')[0], os.listdir(d)))
        if "light exit" in text:
            speak("Thank you for using Light")
            break
        elif "wikipedia" in text:
            speak("Searching in wikipedia...")
            text=text.replace("wikipedia","")
            result=wikipedia.summary(text,sentences=2)
            speak("According to wikipedia source: ")
            print(result)
            speak(result)
            
        elif "open youtube" in text:
            print("Opening Youtube...")
            speak("Opening Youtube")
            webbrowser.open("https://www.youtube.com",new=1)
            
        elif "open google" in text:
            print("Opening Google...")
            speak("Opening Google")
            webbrowser.open("https://www.google.com",new=1)
    
    
        elif "open code" in text:
            print("Opening Visual Studio Code...")
            speak("Opening Visual Studio code")
            app = 'Visual Studio Code'
            os.system('open ' +d+'/%s.app' %app.replace(' ','\ '))
            
        elif "open spotify" in text:
            print("Opening Spotify...")
            speak("Opening Spotify")
            app = 'Spotify'
            os.system('open ' +d+'/%s.app' %app.replace(' ','\ '))
        
        elif "the time" in text:
            print("Displaying current time...")
            speak("Displaying current time...")
            time=datetime.datetime.now().strftime("%H:%M:%S")
            speak(time)
            print(time)