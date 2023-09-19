from bs4 import BeautifulSoup
import requests


def load_file(path: str) -> str:
    """
    Функция возвращает текст из файла
    """
    with open(path, 'r', encoding="utf-8") as f:
        text = f.read()
    
    return text



def load_page(url: str) -> str:
    """ 
    Функция возвращает весь текст веб-страницы
    """

    text = ''

    response = requests.get(url)
    doc = BeautifulSoup(response.content, "html.parser")
    # Выводим каждую строку из тега body
    for string in doc.body.strings:
        text += string

    # Удаление лишних пробелов
    # text = text.translate(str.maketrans('', '', '\n\n'))
    # text = ' '.join(text.split())
    
    return text

if __name__ == "__main__":
    user_url = input("Введите URL: ")
    url = user_url if user_url else "https://rvb.ru/pushkin/01text/04onegin/01onegin/0836-full.htm"
    
    print(load_page(url))