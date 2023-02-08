import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import requests
import json


engine=pyttsx3.init('sapi5')   #code to set the voice of AI david or Zyra
voice=engine.getProperty('voices')
engine.setProperty('voice',voice[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def Wishuser():
    hour=int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good Morning User,I am your Laptop Assistant,How may I help you")
    elif hour>=12 and hour<18:
        speak("Good Afternoon User,I am your Laptop Assistant,How may I help you")
    elif hour>=18:
        speak("Good Evening User,I am your Laptop Assistant,How may I help you")


def takecommand():

    #this function takes voice input from microphone and generates its string output
    cmd=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        cmd.pause_threshold=1
        audio=cmd.listen(source)
    try:
        print("Recognizing...")
        query=cmd.recognize_google(audio,language='en-in')
        print(f"User said:{query}\n")

    except Exception as e:

        print("I can't get you at this moment,Please say it again...")
        return "None"
    return query


if __name__ == '__main__':
    counter=1
    Wishuser()
    while True:

        query=takecommand().lower()


        if ' according to wikipedia' in query:
            speak("Searching Wikipedia")
            query=query.replace("who is","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)


        elif 'open youtube' in query:
            speak("opeining Youtube")
            webbrowser.open("youtube.com")



        elif 'open google' in query:
            speak("Opening google")
            webbrowser.open("google.com")

        elif 'open spotify' in query:
            speak("Opening spotify")
            webbrowser.open("spotify.com")

        elif 'time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak("The time is")
            print("The time is",strTime)
            speak(strTime)

        elif 'open mail' in query:
            webbrowser.open("www.gmail.com")

        elif 'open whatsapp' in query:
            webbrowser.open("www.whatsapp.com")

        elif 'open geekforgeeks' in query:
            webbrowser.open("www.geekforgeeks.com")

        elif 'open hackerrank' in query:
            webbrowser.open("www.hackerrank.com")

        elif 'do you love me' in query:
            speak("I am an AI machine and its typical to love you back!")

        elif 'open flipkart' in query:
            webbrowser.open("www.flipkart.com")

        elif 'open amazon' in query:
            webbrowser.open("www.amazon.com")

        elif 'thank you' in query:
            speak("your welcome")

        elif 'open wikipedia' in query:
            speak("opening wikipedia")
            webbrowser.open("https://en.wikipedia.org//wiki//Main_Page")


        elif 'news' in  query:
            speak("News for Today")
            url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=432409f8f81c466ba1cb176cba422130"
            news = requests.get(url).text
            newsdict = json.loads(news)
            art = newsdict["articles"]
            for articles in art:
                if counter<=2:
                    speak(articles["title"])
                    counter=counter+1
                    speak("Next news is")
                else:
                    speak("Thankyou...")
                    break




        elif 'quit' in query:
            speak("Thankyou,have a nice day")
            break




