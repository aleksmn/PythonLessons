import os
import speech_recognition as sr

# Установка:
# pip install SpeechRecognition
# pip install pyaudio

class Utils:
    def clear(self):
        return os.system('cls||clear')     # os.system('clear') для Linux и MacOS

    def go_on(self):
        input('Нажмите Enter, чтобы продолжить')
        self.clear()

    def is_valid(self, user_input, data_range=''):
        if len(user_input) == 0:
            print('Ошибка ввода. Вы ввели пустую строку.')
            return False
        elif data_range and not user_input.isdecimal():
            print(f'Ошибка ввода. Нужно ввести число')
            return False
        elif data_range and (int(user_input) < data_range[0] or int(user_input) > data_range[1]):            
            print(f'Ошибка ввода. Введите числа от {data_range[0]} до {data_range[-1]}.')
            return False
        else:
            return True


    def speech_recognition(self) -> str:
        recognizer = sr.Recognizer()

        text = ""

        with sr.Microphone() as source:
            print("Слушаю...")

            while not text:
                audio = recognizer.listen(source)
            
                try:
                    text = recognizer.recognize_google(audio, language='ru-RU').capitalize()
                    print(f'Вы сказали: {text}')
                    return text
                except sr.UnknownValueError:
                    print("Не понял вас.")
                except sr.RequestError as e:
                    print(f"Ошибка сервиса распознавания речи: {e}.")



if __name__ == "__main__":
    # Проверка функций
    Utils = Utils()
    Utils.speech_recognition()