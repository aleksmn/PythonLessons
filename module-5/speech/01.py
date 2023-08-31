import speech_recognition as sr

# pip install SpeechRecognition


recognizer = sr.Recognizer()


with sr.Microphone() as source:
    print("Слушаю...")
    audio = recognizer.listen(source)
    print("Конец связи")

text = recognizer.recognize_google(audio, language='ru-RU')

print(f'Вы сказали: {text}')