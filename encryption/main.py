print("\n* Шифровщик Цезаря *\n")

alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

toEncrypt = input("Введите сообщение: ")
shift = int(input("Введите ключ (1-32): "))


def encrypt(toEncrypt, shift):
    encrypted = ""
    toEncrypt = toEncrypt.upper()
    for char in toEncrypt:
        position = alphabet.find(char)
        newPosition = position + shift
        if char in alphabet:
            encrypted = encrypted + alphabet[newPosition]
        else:
            encrypted = encrypted + char

    print(encrypted)




# Вызываем функцию шифровки
encrypt(toEncrypt, shift)
