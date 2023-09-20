import speech_recognition as sr

def get_speech():
    text = ''
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

    finally:
        return text


if __name__ == "__main__":
    speech = get_speech()

    if 'привет' in speech.lower():
        print("И тебе привет!")