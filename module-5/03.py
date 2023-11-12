
class Cat:
    def __init__(self, name, breed, coat_color, character):
        self.name = name
        self.breed = breed
        self.coat_color = coat_color
        self.character = character
        print('Котик родился!')
        print(f'Теперь его зовут {self.name}!')

    def speak(self, text: str):
        """Метод класса"""
        print(f"Кот по имени {self.name} говорит Мяу! {text.capitalize()}.")



murzik = Cat("Мурзик", "персидский", "рыжий", "веселый")