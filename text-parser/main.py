import string
import time

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

def sort_dict(d: dict) -> list:
    """Функция сортирует словарь по значениям"""
    return sorted(d.items(), key=lambda x: x[1], reverse=True)


def filter_words(words):
    stoplist = ''
    try:
        with open('text-parser/stoplist.txt', 'r', encoding='utf-8') as f:
            stoplist = f.read().split()
    except:
        print("Стоплист не найден")
    # print(stoplist)
    return [w for w in words if len(w[0]) > 2 and w[0] not in stoplist]


def output(word_freq):
    title = "Результат частотного анализа\n"
    print(len(title) * "=")
    print(title)

    for word, count in word_freq[:10]:
        h = "#" * (count // 10)
        time.sleep(0.1)
        print(h, count, word)

    print(len(title) * "=")

    


def main():
    url = "https://rvb.ru/pushkin/01text/04onegin/01onegin/0836-full.htm"
    txt = load_page(url)

    word_freq = count_words(txt)
    word_freq = sort_dict(word_freq)
    word_freq = filter_words(word_freq)

    # print(word_freq[:10])  
    output(word_freq)




if __name__ == "__main__":
    main()




