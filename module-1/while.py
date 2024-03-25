# Цикл WHILE (пока)


x = 1

while x**2 < 1000:

    if x**2 % 100 == 0:
        print("Число пропущено")
        x += 1
        continue

    
    print(x**2)

    if x**2 == 676:
        print("Число найдено!")
        break
    
    x += 1



print("Цикл закончен")
