from PIL import Image

# Install:
# pip install pillow

image = Image.open('dog.jpg')

w, h = image.size

# Во сколько раз уменьшить изображение
try:
    factor = int(input("Во сколько раз уменьшить изображение: "))
except:
    factor = 10

new_w, new_h = w/factor, h/factor

new_w = int(new_w)
new_h = int(new_h)

resized_image = image.resize((new_w, new_h))

print(w, h, new_w, new_h)

resized_image.save('dog-mini.jpeg')
