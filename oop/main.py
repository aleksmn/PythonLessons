class Animal:
    def run(self):
        print("I run")

    def sleep(self):
        print("I sleep")



class Cat():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # Магический метод
    def __str__(self) -> str:
        return f"Cat with name {self.name}"

    # Полиморфизм
    def info(self):
        print(
            f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Meow")




class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"Dog with name {self.name}"

    # Полиморфизм
    def info(self):
        print(
            f"I am a dog. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Bark")


cat1 = Cat("Kitty", 2.5)
dog1 = Dog("Fluffy", 4)



print(cat1)
print(dog1)








# for animal in (cat1, dog1):
#     animal.make_sound()
#     animal.info()
#     animal.make_sound()
