print("Добро пожаловать в магазин одежды!")

age = input("Введите возраст: ")

# Получаем целое число
age = int(age)

print("Вы ввели возраст:", age)


if age == 0:
    print("Вы ввели 0 :)")


# Если возраст меньше 12, то переходим в раздел для детей
# иначе переходим в основной раздел (else)
if age < 12:
    # Блок кода
    print("Переходим в раздел для детей!")

elif age < 18:
    print("Переходим в раздел для подростков!")

else:
    print("Переходим в основной раздел магазина!")


print("Спасибо за использование нашего приложения!")