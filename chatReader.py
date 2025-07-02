import pyttsx3
import pytchat
import time
import threading

engine = pyttsx3.init()
engine.setProperty('rate', 180)
voices = engine.getProperty('voices')

for index, voice in enumerate(voices):
    print("------")
engine.setProperty('voices', voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def chatReader(vid_id):
    chat=pytchat.create(video_id=vid_id)
    while chat.is_alive():
        for msg in chat.get().sync_items():
            cText=f"{msg.author.name} says: {msg.message}"
            print(cText)
            
            #voice chat
            thread=threading.Thread(
                target=speak(cText),
                daemon=True
            )
            thread.start()

if __name__ == '__main__':
    print("Youtube Live Chat reader:")
    live_id = input("Enter the live stream ID: ").strip()
    chatReader(live_id)