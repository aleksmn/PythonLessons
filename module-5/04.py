class Animal:
    def run(self):
        print("Бегаю!!!")

    def sleep(self):
        print("Сплю...")



class Cat():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"Кошка по имени {self.name}. Возраст: {self.age}."

    def speak(self):
        print("Мяу-мяу!")


class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"Собака по имени {self.name}. Возраст: {self.age}."

    # Полиморфизм: один метод - разные действия
    def speak(self):
        print("Гав-гав!")




my_cat = Cat("Мурка", 2.5)
my_dog = Dog("Барбос", 4)

print(my_cat)
my_cat.speak()


print(my_dog)
my_dog.speak()





# for animal in (my_cat, my_dog):
#     print(animal)
#     animal.speak()


