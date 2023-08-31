import speech_recognition as sr

recognizer = sr.Recognizer()


with sr.Microphone() as source:
    print("Слушаю...")
    audio = recognizer.listen(source)
    print("Конец связи")

try:
    text = recognizer.recognize_google(audio, language='ru-RU')
    print(f'Вы сказали: {text}')
except sr.UnknownValueError:
    print("Не понял вас.")
except sr.RequestError as e:
    print(f"Ошибка сервиса распознавания речи: {e}.")