print("Программа для расчета площади и периметра прямоугольника")


side1 = int(input("Введите длину:\n"))
side2 = int(input("Введите ширину:\n"))

# Расчет периметра:
p = (side1 + side2) * 2

# Расчет площади
s = side1 * side2

# Вывод

print(f'Прямоугольник со сторонами: {side1} x {side2}')
print(f'Периметр: {p}')
print(f'Площадь: {s}')

# Запись результатов в файл
# a: append - добавить ниже

with open('my-results.txt', 'a', encoding='utf-8') as f:
    f.write(f'Прямоугольник со сторонами: {side1} x {side2}\n')
    f.write(f'Периметр: {p}\n')
    f.write(f'Площадь: {s}\n')
    f.write('---------------------------------------\n')





## Чтение из файла

# with open('my-results.txt', 'r', encoding="UTF-8") as f:
#     for line in f:
#         print(line, end='')


