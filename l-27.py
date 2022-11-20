# Объект
class Cat:
    
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name + ' говорит мяу!')



murka = Cat("Мурка")

murka.speak()

print(dir(murka))











murz = Cat('Мурзик')

murz.speak()