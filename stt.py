import speech_recognition as sr
from googletrans import Translator

#print(googletrans.LANGUAGES)
#mytext = 'hallo'
#translation = Translator().translate(mytext)
#print(translation.text)



r = sr.Recognizer()

with sr.Microphone() as source:
    print("Say Something")
    audio = r.listen(source)
    print("Thank you")
    
try:
#    print("Text: "+r.recognize_google(audio, language="ur-PK"))
    myText = r.recognize_google(audio, language="ur-PK")
    print("Speak Text:  ",myText)
    detect_lang = Translator().detect(myText)
    print("Detected Language:  ",detect_lang)
    translate_lang = Translator().translate(myText)
    print(translate_lang.text)
except:
    pass

