Python 3.8.10 (tags/v3.8.10:3d8993a, May  3 2021, 11:48:03) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import googletrans
import speech_recognition as sr
import gtts
import playsound
recognizer = sr.Recognizer()
translator = googletrans.Translator()
input_lang = 'fr-FR'
output_lang = 'en'
try:
 with sr.Microphone() as source:
 print('Speak Now')
 voice = recognizer.listen(source)
 text = recognizer.recognize_google(voice, language=input_lang)
 print(text)
except:
 pass
translated = translator.translate(text, dest=output_lang)
print(translated.text)
converted_audio = gtts.gTTS(translated.text, lang=output_lang)
converted_audio.save('romantic.mp3')
playsound.playsound('romantic.mp3')
# print(googletrans.LANGUAGES)