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



murzik = Cat("Мурзик", "персидский", "рыжий", "веселый")

murzik.speak("всем привет")