import pyttsx3  # pip intall pyttxs3
import datetime
import speech_recognition as sr  # pip install SpeechRecognition
import wikipedia  # pip install wikipedia

engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is")
    speak(Time)


def date():
    speak("The current date is")
    dt = datetime.datetime.today()
    speak(dt.year)
    speak(dt.month)
    speak(dt.day)


def wishme():
    speak("Welcome buddy!!!")
    time()
    date()
    hour = datetime.datetime.now().hour
    if (hour >= 6 and hour < 12):
        speak("Good Moring!!!")
    elif(hour >= 12 and hour < 18):
        speak("Good Afternoon!!!")
    elif (hour >= 18 and hour < 24):
        speak("Good Evening!!!")
    else:
        speak("Good Night")
    speak("How can i help you buddy!!!")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(query)
        return query
    except Exception as e:
        print(e)
        speak("Please repeat it again!!!")


if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()

        if 'time' in query:
            time()
        elif 'date' in query:
            date()
        elif 'wikipedia' in query:
            speak("Searching...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)
        elif 'offline' in query:
            quit()
