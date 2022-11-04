import string


with open("mytext.txt", 'r', encoding="utf-8") as f:
    text = f.read()

# print(len(text))
# print(text.count(' '))

test = 'Напиши функцию, ,,. /которая будет принимать аргументом текст напиши и возвращать словарь, где ключи — это отдельные слова в тексте, а значения — их количество.'

# def count_words(text):
#     d = {}

#     # Убираем заглавные буквы
#     text = text.lower()

#     # Избавляемся от знаков припинания (пунктуации)
#     text = text.translate(text.maketrans('', '', string.punctuation))

#     for word in text.split():
#         d[word] = d.get(word, 0) + 1

#     return d


# print(count_words(text))


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

# print(res)

# for k, v in res:
#     print(k, v)


#### Фильтруем слова - оставляем только те, где 3+ букв


# chart = count_words(text)[:100]


# filtered_chart = []

# for w in chart:
#     # print(w[1])
#     if len(w[1]) > 2:
#         filtered_chart.append(w)



# Более удобный способ (Генератор списков)
# filtered_chart = [w for w in chart if len(w[1]) > 2]

# print(filtered_chart)


# for k, v in filtered_chart:
#     print(k, v)



## Фильтруем результат с использованием стоп листа

with open('stoplist.txt', 'r') as f:
    stoplist = f.read().split()


# print(stoplist)

# Вносим поправки в стоплист

my_stop = 'иль ним пред меж сей свой'


stoplist = stoplist + my_stop.split()

chart = count_words(text)

filtered_chart = [w for w in chart if len(w[1]) > 2 and w[1] not in stoplist ]

for k, v in filtered_chart[:40]:
    print(k, v)

