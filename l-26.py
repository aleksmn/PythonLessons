

def count_letters(word):
    letters = {}

    for l in word:
        if l not in letters:
            letters[l] = 1

        else:
            letters[l] += 1

    return letters 


print(count_letters("Wonderland"))




# Wonderland


# def count_letters(word):
#     letters = {}
#     for char in word:

#         letters[char] = word.count(char)

#     return letters

# print(count_letters("Wonderland"))


# Напиши функцию, которая будет принимать 
# аргументом текст и возвращать словарь, 
# где ключи — это отдельные слова в тексте, 
# а значения — их количество.

# text = "Напиши функцию, которая будет принимать аргументом текст и возвращать словарь, где ключи — это отдельные слова в тексте, а значения — их количество."
