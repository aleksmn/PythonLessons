class Cat:
    def __init__(self, name, breed, coat_color, character):
        self.name = name
        self.breed = breed
        self.coat_color = coat_color
        self.character = character
        print('Котик родился!')
        print(f'Теперь его зовут {self.name}!')

    # Метод (функция)
    def speak(self, text):
        print(f"Кот по имени {self.name} говорит: Мяу! {text.capitalize()}. Мяу-мяу!")


    # def __str__(self):
    #     return f"Объект класса Cat. Имя: {self.name}"



# murzik = Cat("Мурзик", "персидский", "рыжий", "веселый")

# murzik.speak("всем привет")

# print(murzik)














class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # метод класса
    def get_perimeter(self):
        return (self.width + self.height) * 2
    


rect_1 = Rectangle(23, 54)
print(rect_1.get_perimeter())