# Подсчитать количество гласных букв в строке

def get_vowels(string):
    vowels = "aeiouAEIOU"
    count = 0
    for letter in string:
        if letter in vowels:
            count += 1
    print(count)





get_vowels("Hello, World!")