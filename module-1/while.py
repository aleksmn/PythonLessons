# Цикл WHILE (пока)

x = 1

while x**2 < 1000:
    print(x, x**2)

    if x**2 == 400:
        print("Число найдено!")
        # Выход из цикла
        break

    elif x % 2 == 0:
        print("Четное число!")


    x += 1



print("Цикл закончен")