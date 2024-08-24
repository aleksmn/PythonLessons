from PIL import Image, ImageDraw, ImageFont

# Как установить библиотеку (модуль)
# выполнить в терминале команду
# pip install pillow


print("Генератор мемов запущен!")

text_type = input("Сколько добавить текстов, 1 или 2: ")

if text_type == "1":
    top_text = ""
    bottom_text = input("Введите текст: ")

elif text_type == "2":
    top_text = input("Введите верхний текст: ")
    bottom_text = input("Введите нижний текст: ")

else:
    print("Введён неправильный режим. Перезапустите программу.")
    # Выход из программы
    quit()

print("Выберите картинку для мема:")

print("1. Кот в ресторане")
print("2. Кот в очках")


meme_number = input("Введите номер картинки: ")

if meme_number == "1":
    meme = "Кот в ресторане.png"
elif meme_number == "2":
    meme = "Кот в очках.png"
else:
    print("Введён неправильный номер картинки. Перезапустите программу.")
    # Выход из программы
    quit()


#  Открываем картинку
image = Image.open(meme)

width, height = image.size

print(width, height)

draw = ImageDraw.Draw(image)

font = ImageFont.truetype('arial.ttf', size=70)


# Добавим верхний текст на картинку

draw.text(xy=(width // 2, 60), text=top_text, font=font, fill="black", anchor="mt")

draw.text(xy=(width // 2, height - 60), text=bottom_text, font=font, fill="black", anchor="mb")

# Сохраняем картинку
image.save("new_meme.png")
print("Картинка сохранена!")