print("\n**\n")

name = input("Как тебя зовут?  ")

print("Привет, " + name + "!")

year = int(input("Введите год рождения: "))

age = 2022 - year

print("Ваш возраст:", age)


if age < 13:
    print("Переходим в товары для детей...")

elif age < 18:
    print("Переходим к товарам для подростков")

else:
    print("Переходим к основному разделу")
