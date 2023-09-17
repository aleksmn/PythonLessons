import string
import time
import os

os.system('clear || cls')

with open("mytext.txt", 'r', encoding="utf-8") as f:
    text = f.read()

# print(len(text))
# print(text.count(' '))

def count_words(text):
    d = {}

    # Убираем заглавные буквы
    text = text.lower()

    # Избавляемся от знаков припинания (пунктуации)
    text = text.translate(text.maketrans('', '', string.punctuation))

    for word in text.split():
        d[word] = d.get(word, 0) + 1

    # Составляем рейтинг слов

    word_chart = []

    for key, val in d.items():
        word_chart.append((val, key))

    word_chart = sorted(word_chart, reverse=True)

    return word_chart


res = count_words(text)[:5]

# Фильтруем результат с использованием стоп листа

with open('stoplist.txt', 'r', encoding='utf-8') as f:
    stoplist = f.read().split()


# print(stoplist)

# Вносим поправки в стоплист

my_stop = 'иль ним пред меж сей свой моей'

stoplist = stoplist + my_stop.split()

chart = count_words(text)

filtered_chart = [w for w in chart if len(w[1]) > 2 and w[1] not in stoplist]


title = "Результат частотного анализа\n"
print(len(title) * "=")
print(title)

for count, word in filtered_chart[:10]:
    h = "#" * (count // 10)
    time.sleep(0.1)
    print(h, count, word)


print(len(title) * "=")