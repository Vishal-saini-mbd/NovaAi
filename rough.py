import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()
def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)



if __name__ == "__main__":
    r = sr.Recognizer()
    speak("Activating nova")

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source)

            word = r.recognize_google(audio)

            if word.lower() == "nova":
                speak("Yes sir")
                
                with sr.Microphone() as source:
                    print("nova Active...")
                    audio = r.listen(source, timeout=2, phrase_time_limit=1)

                command = r.recognize_google(audio)
                print("command:", command)
                processCommand(command)

        except Exception as e:
            print("Error:", e)
