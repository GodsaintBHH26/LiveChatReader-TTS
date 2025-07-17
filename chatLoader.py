import pytchat
import re
from chatSpeaker import speak
import time
import threading

link = re.compile(r'https?://\S+|www\.\S+')

def chatReader(vid_id):
    chat=pytchat.create(video_id=vid_id)
    while chat.is_alive():
        for msg in chat.get().sync_items():
            
            text, emoji = parse_message(msg)
            emoji_count = len(emoji)
            
            if emoji_count == 0:
                cText=f"{msg.author.name} says: {text}"
            elif emoji_count > 2 :
                cText = f"{msg.author.name} sent {emoji_count} emojies and said {text}"
            print(cText)
            
            #voice chat
            thread=threading.Thread(
                target=speak(cText),
                daemon=True
            )
            thread.start()
            

def parse_message(messageEx):
     emoji = []
     Message = []
     
     if not hasattr(messageEx, 'messageEx'):
        return messageEx.message, emoji
            
     for part in messageEx.messageEx:
            if isinstance(part, dict) and part.get('type') == 'text':
                if part.get('type')== 'text':
                    Message.append(part.get('text', ''))
                elif 'emoji' in part:
                    emoji.append(part['emojiText'])
            elif isinstance(part, str):
                Message.append(part)

    
     return ' '.join(Message), emoji