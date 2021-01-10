import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)



def sendEmail(to ,content):
    server =smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login('rrpatil2701@gmail.com','********')
    server.sendmail('rrpatil2701@gmail.com',to,content)
    server.close()
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Rushi")
    elif hour >=12 and hour <18:
        speak("Good afternoon Rushi")
    else:
        speak("Goood Evening ! Rushi")
    speak(" I am Ritcho sir . Please tell moe how may i help you!")
def hear():
    # it takes the microphone input from the user and returns String output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening ...")
        r.pause_threshold = 1
        audio =r.listen(source)
    try:
        print("Recognizing ...")
        query =r.recognize_google(audio,language='en-in')
        print("user said:{}".format(query))
    except Exception as e:
        print(e)
        print("Say that again please ...")
        return "None"
    return query
if __name__ == "__main__":
    WishMe()
    while True:
        query = hear().lower()
        # Logic for executing  task based query
        if "wikipedia" in query:
            speak("Searching wikipedia")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query,sentences=2)
            speak("Acocording to wikipedia ")
            speak(result)
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "open google" in query:
            webbrowser.open("google.com")
        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")
        elif "play music" in query:
            music_dir = 'C:\\Users\\RUSHIKESH\\Music\\PowerDVD 14\\MusicStore'
            songs =os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif "current time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")  
            speak("The time is {}".format(strTime))
        elif "open code" in query:
            codepath ="C:\\Users\\RUSHIKESH\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        elif "send email" in query:
            try:
                speak("What should I say?")
                content = hear()
                to ="rrpatil853@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                speak("sorry my friend Rushi . I am not able to send Email.")     
