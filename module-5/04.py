# Наследование

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sleep(self):
        print("Сплю...")

    def run(self):
        print("Бегаю!")


class Cat(Animal):
    def __init__(self, name, age):
        # Вызываем конструктор родительского класса
        Animal.__init__(self, name, age)

    def speak(self):
        print(f"Кошка по имени {self.name} говорит Мяу!")



class Dog(Animal):
    def __init__(self, name, age, toy):
        # Вызываем конструктор родительского класса
        Animal.__init__(self, name, age)

        self.toy = toy

    def play(self):
        print(f"Играю с любимой игрушкой: {self.toy}")

    # Полиморфизм - название метода одинаковое, но разные действия
    def speak(self):
        print(f"Собака по имени {self.name} говорит Гав!")


# Создадим объекты
cat1 = Cat("Мурка", 2)
cat1.speak()  
cat1.sleep()  
cat1.run()  



dog1 = Dog("Шарик", 4, "мяч")
dog1.speak()
dog1.sleep()
dog1.run()