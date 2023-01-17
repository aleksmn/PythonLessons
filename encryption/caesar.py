print("\n* Шифр Цезаря *\n")

alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

toEncrypt = input("Введите сообщение: ")

toEncrypt = toEncrypt.upper()

shift = int(input("Введите ключ (1-32): "))

encrypted = ""

for char in toEncrypt:
    position = alphabet.find(char)
    newPosition = position + shift
    if char in alphabet:
        encrypted = encrypted + alphabet[newPosition]
    else:
        encrypted = encrypted + char


print("Результат шифровки: ", encrypted)




# # English Version

# alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"

# toEncrypt = input("Enter a message: ")


# toEncrypt = toEncrypt.upper()

# shift = int(input("Enter a key (1-25): "))

# encrypted = ""

# for char in toEncrypt:
#     position = alphabet.find(char)
#     newPosition = position + shift
#     if char in alphabet:
#         encrypted = encrypted + alphabet[newPosition]
#     else:
#         encrypted = encrypted + char


# print("Your encrypted message is", encrypted)
