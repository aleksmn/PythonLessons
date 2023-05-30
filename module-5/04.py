# class Cat():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self) -> str:
#         return f"Кошка по имени {self.name}. Возраст: {self.age}."

#     def speak(self):
#         print("Мяу-мяу!")



# class Dog():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self) -> str:
#         return f"Собака по имени {self.name}. Возраст: {self.age}."

#     # Полиморфизм: название метода одинаковое - разные действия
#     def speak(self):
#         print("Гав-гав!")





# my_cat = Cat("Мурка", 2.5)

# print(my_cat.sleep())



# my_dog = Dog("Барбос", 4)

# print(my_cat)
# my_cat.speak()


# print(my_dog)
# my_dog.speak()















# class Animal:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def run(self):
#         print("Бегаю!!!")

#     def sleep(self):
#         print("Сплю...")



# class Cat(Animal):

#     def __init__(self, name, age):
#         Animal.__init__(self, name, age)


#     def __str__(self) -> str:
#         return f"Кошка по имени {self.name}. Возраст: {self.age}."

#     def speak(self):
#         print("Мяу-мяу!")


# class Dog(Animal):
#     def __init__(self, name, age):
#         Animal.__init__(self, name, age)

#     def __str__(self) -> str:
#         return f"Собака по имени {self.name}. Возраст: {self.age}."

#     # Полиморфизм: один метод - разные действия
#     def speak(self):
#         print("Гав-гав!")




# my_cat = Cat("Мурка", 2.5)
# my_dog = Dog("Барбос", 4)

# print(my_cat)
# my_cat.speak()
# my_cat.sleep()

# print(my_dog)
# my_dog.speak()
# my_dog.sleep()



# for animal in (my_cat, my_dog):
#     print(animal)
#     animal.speak()