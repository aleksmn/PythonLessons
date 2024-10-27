print("Генератор мемов запущен!")


top_text = input("Введите верхний текст: ")
bottom_text = input("Введите нижний текст: ")

print(top_text, bottom_text)

print("Список картинок:")
print("1. Кот в ресторане")
print("2. Кот в очках")

image_number = int(input("Введите номер картинки: "))

if image_number == 1:
    image = "Кот в ресторане.png"
elif image_number == 2:
    image = "Кот в очках.png"
else:
    print("Введён неправильный номер картинки. Перезапустите программу.")
    # Выход из программы
    quit()

print(image)