import requests
import urllib

from config import USERNAME, PASSWORD

# Установка модулей
# pip install requests

# Ссылка на API
# https://api.imgflip.com/get_memes


images = requests.get(
    'https://api.imgflip.com/get_memes').json()['data']['memes']


print('Список доступных мемов')
count = 1

for img in images:
    print(count, img['name'], img['url'])
    count += 1


# # Добавляем текст на картинку

id = int(input('Введите номер картинки: '))

text0 = input('Введите первый текст: ')
text1 = input('Введите второй текст: ')


URL = 'https://api.imgflip.com/caption_image'

params = {
    'username': USERNAME,
    'password': PASSWORD,
    'template_id': images[id-1]['id'],
    'text0': text0,
    'text1': text1
}

response = requests.request('POST', URL, params=params).json()

# print(response)


if response['success']:
    image_url = response['data']['url']
    image_name = images[id-1]['name']+'.jpg'
    print('Готово! Картинка доступна по ссылке:')
    print(image_url)

else:
    print('Что-то пошло не так...')
    quit()



# # Сохранение картинки

user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"

opener = urllib.request.URLopener()

opener.addheader('User-Agent', user_agent)

opener.retrieve(image_url, image_name)
