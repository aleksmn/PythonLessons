


def load_text(path):
    """
    Загружаем текст из файла
    """
    with open(path, 'r', encoding="utf-8") as f:
        text = f.read()
    
    return text



def count_words(text):
    """ 
    Делаем частотный анализ слов в тексте
    Функция возвращает словарь, в котором ключи это слова,
    а значения - это число, сколько раз слово встречается в тексте
    """

    word_freq = {}

    # Твой код

    return word_freq




if __name__ == "__main__":
    # Тестируем
    txt = load_text("text-parser/mytext.txt")
    print(count_words(txt))









# load_text("text-parser/mytext.txt") 



