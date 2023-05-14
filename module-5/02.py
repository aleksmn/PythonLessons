
class Airplane:
    engines = int(input('Двигатели: '))
    seats = int(input('Посадочные места: '))

    print('Самолет собран!')


plane1 = Airplane()
plane2 = Airplane()
plane3 = Airplane()


print(plane1.engines)
print(plane2.engines)
print(plane3.engines)





























# class Airplane:
#     def __init__(self):
#         '''Конструктор класса'''
#         self.engines = int(input('Двигатели: '))
#         self.seats = int(input('Посадочные места: '))

#         print('Самолет собран!')    


# plane1 = Airplane()
# plane2 = Airplane()
# plane3 = Airplane()


# print(plane1.engines, plane1.seats)
# print(plane2.engines, plane2.seats)
# print(plane3.engines, plane3.seats)








# class Airplane:
#     def __init__(self, engines=1, seats=2):
#         '''Конструктор класса'''
#         self.engines = engines
#         self.seats = seats

#         print('Самолет собран!')    


# plane1 = Airplane(engines=3, seats=5)
# plane2 = Airplane()
# plane3 = Airplane()


# print(plane1.engines, plane1.seats)
# print(plane2.engines, plane2.seats)
# print(plane3.engines, plane3.seats)









# class Car:
#     def __init__(self, color, brand, speed):
#         self.color = color
#         self.brand = brand
#         self.speed = speed
#         print('Автомобиль готов!')





# class Cat:
#     def __init__(self, name, breed, coat_color, character):
#       self.name = name
#       self.breed = breed
#       self.coat_color = coat_color
#       self.character = character
#       print('Котик родился!')
#       print(f'Теперь его зовут {self.name}!')

