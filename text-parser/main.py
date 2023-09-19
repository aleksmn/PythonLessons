import string
from load import load_file, load_page


def count_words(text):
    """ 
    Делаем частотный анализ слов в тексте
    Функция возвращает словарь, в котором ключи это слова,
    а значения - это число, сколько раз слово встречается в тексте
    """

    word_freq = {}
    text = text.lower()

    # Избавляемся от знаков припинания (пунктуации)
    text = text.translate(str.maketrans('', '', string.punctuation))

    for word in text.split():
        word_freq[word] = word_freq.get(word, 0) + 1

    return word_freq

def sort_dict(d:dict, reverse=True) -> list:
    """Функция сортирует словарь по значениям"""
    return sorted(d.items(), key=lambda w: w[1], reverse=reverse)

def filter_words(words):
    return [w for w in words if len(w[0]) > 2]

def main():

    # user_url = input("Введите URL: ")
    url = "https://rvb.ru/pushkin/01text/04onegin/01onegin/0836-full.htm"

    txt = load_page(url)
    word_freq = count_words(txt)
    word_freq = sort_dict(word_freq)
    word_freq = filter_words(word_freq)
    print(word_freq[:10])

    # print(max(word_freq.items(), key=lambda w: w[1]))




if __name__ == "__main__":
    main()




