from bs4 import BeautifulSoup
import requests



def load_page(url):

    response = requests.get(url)
    
    doc = BeautifulSoup(response.content, "html.parser")
    
    # Получаем содержимое тега body
    tag = doc.body
    
    # Выводим каждую строку
    for string in tag.strings:
        print(string.strip())


if __name__ == "__main__":
    url = "https://rvb.ru/pushkin/01text/04onegin/01onegin/0836-full.htm"
    load_page(url)