from PIL import Image, ImageDraw, ImageFont

# установим библиотеку Pillow
# pip install pillow

print("Генератор мемов запущен!")

text_type = input("Сколько добавить текстов, 1 или 2: ")

if text_type == "1":
    top_text = ""
    bottom_text = input("Введите нижний текст: ")
elif text_type == "2":
    top_text = input("Введите верхний текст: ")
    bottom_text = input("Введите нижний текст: ")
else:
    print("Введён неправильный режим. Перезапустите программу.")
    # Выход из программы
    quit()

print(top_text, bottom_text)

# Шаг 2
# Список картинок
memes = ["Кот в ресторане.png", "Кот в очках.png"]

print("Выберите картинку для мема:")

count = 1
for m in memes:
    print(count, m)
    count += 1


meme_number = int(input("Введите номер картинки: "))

# Шаг 3. Открываем картинку

image = Image.open(memes[meme_number - 1])
width, height = image.size

print(width, height)

draw = ImageDraw.Draw(image)

#for macOS:  "Keyboard.ttf"

font = ImageFont.truetype('arial.ttf', size=70)

# Добавим текст на картинку
# верхний текст
draw.text(xy=(width / 2, 60), 
          text=top_text, 
          font=font, 
          fill="black", 
          anchor="mt")

# нижний текст
draw.text(xy=(width / 2, height - 60), 
          text=bottom_text, 
          font=font, 
          fill="black", 
          anchor="mb")


image.save("new_meme.png")
print("Картинка сохранена!")
