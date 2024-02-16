import pyttsx3 as pt
import speech_recognition as sr

def speak(query):
    engine=pt.init('sapi5')
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.say(query)
    engine.runAndWait()


def micro():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold=1
        r.energy_threshold=300
        audio=r.listen(source)


    try:
        print("Recog...")
        query=r.recognize_google(audio,language="en-in")
        print(f"You said: {query}\n")

    except Exception as e:
        print("Say that again....")
        return "NONE"
    return query



def greetings():
    pass
    




