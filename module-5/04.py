class Cat():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Кошка по имени {self.name}. Возраст: {self.age}."

    def speak(self):
        print("Мяу-мяу!")



class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Собака по имени {self.name}. Возраст: {self.age}."

    # Полиморфизм: название метода одинаковое - разные действия
    def speak(self):
        print("Гав-гав!")





my_cat = Cat("Мурка", 2.5)

print(my_cat.sleep())



my_dog = Dog("Барбос", 4)

print(my_cat)
my_cat.speak()


print(my_dog)
my_dog.speak()



class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print("Бегаю!!!")

    def sleep(self):
        print("Сплю...")



class Cat(Animal):

    def __init__(self, name, age):
        super().__init__(name, age)


    def __str__(self):
        return f"Кошка по имени {self.name}. Возраст: {self.age}."

    def speak(self):
        print("Мяу-мяу!")

    def scratch(self):
        print("Точу когти!")


class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def __str__(self):
        return f"Собака по имени {self.name}. Возраст: {self.age}."

    # Полиморфизм: один метод - разные действия
    def speak(self):
        print("Гав-гав!")



class Tiger(Cat):
    def __init__(self, name, age):
        super().__init__(name, age)


my_cat = Cat("Мурка", 2.5)
my_dog = Dog("Барбос", 4)

print(my_cat)
my_cat.speak()
my_cat.sleep()

print(my_dog)
my_dog.speak()
my_dog.sleep()


tiger_1 = Tiger("Тигра", 8)
print(tiger_1)
tiger_1.scratch()


for animal in (my_cat, my_dog):
    print(animal)
    animal.speak()