import pyttsx3

engine = pyttsx3.init(driverName='sapi5')
engine.setProperty('rate', 180)
voices = engine.getProperty('voices')

def speak(text):
    engine.say(text)
    engine.runAndWait()
