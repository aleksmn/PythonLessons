
class Rectangle:
    # Конструктор класса
    def __init__(self, width, height):
        # self - ссылка на сам объект
        self.width = width
        self.height = height
        print(f"Прямоугольник со сторонами {self.width} и {self.height} создан")



rect1 = Rectangle(2, 4)
rect2 = Rectangle(34, 45)
rect3 = Rectangle(23, 56)

# Выводим периметры
print(rect1.width * 2 + rect1.height * 2)
print(rect2.width * 2 + rect2.height * 2)
print(rect3.width * 2 + rect3.height * 2)