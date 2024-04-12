
class Rectangle:
    # Конструктор класса
    def __init__(self, width, height):
        # self - ссылка на сам объект
        self.width = width
        self.height = height
        print(f"Прямоугольник со сторонами {self.width} и {self.height} создан")

    # метод для нахождения периметра
    def get_perimeter(self):
        return self.width * 2 + self.height * 2

    # метод для нахождения площади
    def get_area(self):
        return self.width * self.height




rect1 = Rectangle(2, 4)
rect2 = Rectangle(34, 45)
rect3 = Rectangle(23, 56)


print(rect1.get_perimeter())
print(rect2.get_perimeter())
print(rect3.get_perimeter())