text = input("Введите текст: ")
text = text.lower()

punctuation = [".", ",", "!", "?"]

for char in punctuation:
    text = text.replace(char, "")

words = text.split()

longest_word = words[0]
shortest_word = words[0]

for word in words:

    # Поиск самого длинного и самого короткого слова
    if len(word) > len(longest_word):
        longest_word = word
    if len(word) < len(shortest_word):
        shortest_word = word


# Частота слов

word_frequency = {} 

for word in words:
    # Если слово есть в словаре, увличиваем значение на 1
    if word in word_frequency:
        word_frequency[word] += 1    
    else:
        word_frequency[word] = 1


# Вывод результата
print("Количество разных слов:", len(set(words)))
print("Самое длинное слово:", longest_word)
print("Самое короткое слово:", shortest_word)

print("Частота слов:")
for w, f in word_frequency.items():
    print(f'{w}: {f}')