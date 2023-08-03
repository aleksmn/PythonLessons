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

print("Количество разных слов:", len(set(words)))
print("Самое длинное слово:", longest_word)
print("Самое короткое слово:", shortest_word)