import speech_recognition as sr 
from translate import Translator
import os 

r = sr.Recognizer()
lg = Translator(from_lang = "english" , to_lang = "german")


text = ''

while text != "close":
    print("\nspeak something\n")
    with sr.Microphone() as source:
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            os.system('cls')
            print(text)
            convert = lg.translate(text)
            print(convert)
        except:
            print("could not recognize")