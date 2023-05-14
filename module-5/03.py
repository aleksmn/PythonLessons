
class Cat:
    def __init__(self, name, color, character):
      self.name = name
      self.color = color
      self.character = character
      print('Котик родился!')
      print(f'Теперь его зовут {self.name}!')


    def say(self):
       print(f'{self.character.capitalize()} {self.color} котенок {self.name} говорит Мяу!')



kitty = Cat('Вася', 'рыжий', 'веселый')


kitty.say()