from PIL import Image, ImageDraw, ImageFont

# Как установить библиотеку (модуль)
# выполнить в терминале команду
# pip install pillow

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

#  Открываем картинку
image = Image.open(image)

# получим ширину и высоту картинки
width, height = image.size

print(width, height)

draw = ImageDraw.Draw(image)

font = ImageFont.truetype('arial.ttf', size=70)
# для MacOS
# font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", size=70)

# Добавим текст на картинку
# верхний текст
draw.text(xy=(width//2, 60), text=top_text, font=font, fill="black", anchor="mt")
# нижний текст
draw.text(xy=(width//2, height - 60), text=bottom_text, font=font, fill="black", anchor="mb")

# Сохраняем картинку
image.save("new_meme.png")
print("Картинка сохранена!")