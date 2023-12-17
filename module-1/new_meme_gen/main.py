from PIL import Image, ImageDraw, ImageFont

# установим библиотеку Pillow
# pip install pillow

print("Генератор мемов запущен!")

text_type = int(input("Сколько добавить текстов, 1 или 2: "))

if text_type == 1:
    top_text = ""
    bottom_text = input("Введите нижний текст: ")
elif text_type == 2:
    top_text = input("Введите верхний текст: ")
    bottom_text = input("Введите нижний текст: ")
else:
    print("Введён неправильный режим. Перезапустите программу.")
    quit()

print(top_text, bottom_text)


# Шаг 2
memes = ["Кот в ресторане.png", "Кот в очках.png"]

print("Выберите картинку для мема:")

for i in range(len(memes)):
    print(i, memes[i])

meme_number = int(input("Введите номер картинки: "))

# Шаг 3. Открываем картинку

image = Image.open(memes[meme_number])
width, height = image.size

print(width, height)

draw = ImageDraw.Draw(image)

font = ImageFont.truetype('arial.ttf', size=70)


draw.text((width / 2, 60), top_text, font=font, fill="black", anchor="mt")

draw.text((width / 2, height - 60), bottom_text, font=font, fill="black", anchor="mb")


image.save("new_meme.jpg")
