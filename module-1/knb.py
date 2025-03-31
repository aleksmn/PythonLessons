import random

print("1 - камень, 2 - ножницы, 3 - бумага")
# Выбор игрока
human = input("Введите выбор: ")


# Выбор компьютера
robot = str(random.randint(1, 3))


if human == "1" and robot == "1":
    print("Компьютер выбрал камень: ничья")

elif human == "1" and robot == "2":
    print("Компьютер выбрал ножницы: ваша победа")

elif human == "1" and robot == "3":
    print("Компьютер выбрал бумагу: компьютер победил")

elif human == "2" and robot == "1":
    print("Компьютер выбрал камень: компьютер победил")

elif human == "2" and robot == "2":
    print("Компьютер выбрал ножницы: ничья")

elif human == "2" and robot == "3":
    print("Компьютер выбрал бумагу: ваша победа")


elif human == "3" and robot == "1":
    ...