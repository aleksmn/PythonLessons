print("\n* Шифровщик Цезаря *\n")

alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

# toEncrypt = input("Введите сообщение: ")
shift = int(input("\nВведите ключ (1-32): "))





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

    return encrypted




# Вызываем функцию шифровки
# encrypt(toEncrypt, shift)


file = input("Введите название файла: ")

lines=[]

with open(file, 'r', encoding='utf-8') as f:
    for line in f:
        lines.append(line)

print(lines)


encrypted_lines = []


for l in lines:
    #  encrypt(l, shift)

     encrypted_lines.append(encrypt(l, shift))



print(encrypted_lines)