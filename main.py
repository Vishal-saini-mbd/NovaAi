import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from gtts import gTTS
import pygame
from openai import OpenAI
import os

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()
def speak_old(text):
    tts = gTTS(text)
    tts.save('temp.mp3') 
    # Initialize Pygame mixer
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load('temp.mp3')

    # Play the MP3 file
    pygame.mixer.music.play()

    # Keep the program running until the music stops playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    pygame.mixer.music.unload()
    os.remove("temp.mp3") 
def aiProcess(command):
    client = OpenAI(api_key="OPENAI_API_KEY")

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=[
            {
                "role": "system",
                "content": "You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Assistant. Give short responses."
            },
            {
                "role": "user",
                "content": command
            }
        ]
    )

    return response.output_text


# print(response.output_text)


newsapi = "NEWS_API_KEY"
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
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()
            
            # Extract the articles
            articles = data.get('articles', [])
            
            # Print the headlines
            for article in articles:
                speak(article['title'])
    else:
        #let OpenAi handle the problem
        output = aiProcess(c)
        speak(output)
        pass
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
                    audio = r.listen(source)

                command = r.recognize_google(audio)
                print("command:", command)
                processCommand(command)

        except Exception as e:
            print("Error:", e)