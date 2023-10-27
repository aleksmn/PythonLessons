import requests
from pprint import pprint
from datetime import datetime

from config import open_weather_token


# WEATHER_TOKEN = getenv("open_weather_token")
WEATHER_TOKEN = open_weather_token

def get_weather(city):


    r = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_TOKEN}&units=metric&lang=ru")
    data = r.json()

    # pprint(data)

    # Валидация полученных данных
    if data['cod'] == '404':
        return "Город с таким названием не найден"
    if data['cod'] == 401:
        return "Возника ошибка: " + data['message']


    city = data["name"]
    temp = data["main"]["temp"]
    description = data["weather"][0]["description"]
    humidity = data["main"]["humidity"]
    wind = data["wind"]["speed"]
    sunrise = datetime.fromtimestamp(data["sys"]["sunrise"])
    sunset = datetime.fromtimestamp(data["sys"]["sunset"])
    day_length = sunset - sunrise

    # print(city, temp, humidity, wind)
    # print(sunrise, sunset)

    weather_output = (
        f"--- {datetime.now().strftime('%Y-%m-%d %H:%M')} ---\n"
        f"Погода в городе {city}\nТемпература: {temp}С\nОписание: {description}\nВлажность: {humidity}%"
        f"\nСкорость ветра: {wind} м/с\nВосход: {sunrise}\nЗакат: {sunset}\nДолгота дня: {day_length}"
    )

    return weather_output




def main():
    city = input("Введите город: ")
    weather = get_weather(city)
    print(weather)


if __name__ == '__main__':
    main()
