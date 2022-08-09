side = input("Введите сторону квадрата:\n")
side = float(side)

p = side * 4
p = round(p, 2)
s = side ** 2
s = round(s, 2)
print('Периметр квадрата:', p)
print('Площадь квадрата:', s)


with open('my-file.txt', 'a') as f:
    f.write('--------------------' + "\n")
    f.write('Сторона квадрата: ' + str(side) + "\n")
    f.write('Периметр квадрата: ' + str(p) + "\n")
    f.write('Площадь квадрата: ' + str(s) + "\n")


# with open('my-file.txt', 'r') as f:
#     for line in f:
#         print(line, end='')


# https://www.youtube.com/watch?v=Uh2ebFW8OYM
