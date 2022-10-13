side = input("Введите сторону квадрата:\n")
side = float(side)

p = side * 4
p = round(p, 2)
s = side ** 2
s = round(s, 2)
print('Периметр квадрата:', p)
print('Площадь квадрата:', s)


with open('my-file.txt', 'a', encoding="UTF-8") as f:
    f.write('Сторона квадрата: ' + str(side) + "\n")
    f.write('Периметр квадрата: ' + str(p) + "\n")
    f.write('Площадь квадрата: ' + str(s) + "\n")
    f.write('--------------------' + "\n")


with open('my-file.txt', 'r', encoding="UTF-8") as f:
    for line in f:
        print(line, end='')


