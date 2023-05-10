import qrcode

data = 'Hello World!'

# Простой способ
img = qrcode.make(data)

img.save('test.png')


# с настройками:

qr = qrcode.QRCode(box_size=22, border=8)

qr.add_data(data)

img2 = qr.make_image(fill_color='navy')

img2.save('test2.png')









# links= '''https://ru.wikipedia.org/wiki/Объектно-ориентированное_программирование

# https://ru.wikipedia.org/wiki/Структурное_программирование

# https://ru.wikipedia.org/wiki/Функциональное_программирование
# '''