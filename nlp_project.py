!pip install SpeechRecognition
!pip install gTTS
!pip install transformers 
!pip install tensorflow
!pip install pipwin
!pipwin install pyaudio

import speech_recognition as sr
from gtts import gTTS
import transformers
import os
import datetime
import numpy as np

class ChatBot():
    def __init__(self, name):
        print("--- starting up", name, "---")
        self.name = name
    def speechToText(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as mic:
            print("Listening!!")
            audio = recognizer.listen(mic)
        try:
            self.text = recognizer.recognize_google(audio)
            print("Me -> ", self.text)
        except:
            print("Me ->  ERROR")
    @staticmethod
    def TextToSpeech(text):
        print("AI -> ", text)
        speaker = gTTS(text=text, lang="en", slow=False)
        speaker.save("res.mp3")
        os.system("afplay res.mp3")  #mac->afplay | windows->start
        os.remove("res.mp3")
    def wake_up(self, text):
        return True if self.name in text.lower() else False
    @staticmethod
    def action_time():
        return datetime.datetime.now().time().strftime('%H:%M')

if __name__ == "__main__":
    AI = ChatBot(name="jay")
    nlp = transformers.pipeline("conversational", model="microsoft/DialoGPT-medium")
    os.environ["TOKENIZERS_PARALLELISM"] = "true"
    while True:
        AI.speechToText()
        if AI.wake_up(AI.text) is True:
            res = "Hello I am Meghana! What can I do for you?"
        elif "time" in AI.text:
            res = AI.action_time()
        elif any(i in AI.text for i in ["thank you","thanks"]):
            res = np.random.choice(["you're welcome!","anytime!","no problem!","It's Okay", cool!","I'm here if you need me!"])
        else:   
            chat = nlp(transformers.Conversation(ai.text), pad_token_id=50256)
            res = str(chat)
            res = res[res.find("bot >> ")+6:].strip()
        AI.TextToSpeech(res)
