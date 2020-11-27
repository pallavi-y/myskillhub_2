import pyttsx3

def Say(text):

    engine = pyttsx3.init()
    engine.setProperty("rate", 130)
    engine.say(text)
    engine.runAndWait()