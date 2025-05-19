# Пример инкапсуляции

class Kettle:
    def __init__(self):
         self.brand = "Скайсмарт"

    def turn_on(self):
        print(f'Чайник {self.brand} включился')
        self.boil()
        self.check_t()
        self.beep()
        self.turn_off()

    def boil(self):
        print('Вода греется...')

    def check_t(self):
        print('Проверяется температура')

    def beep(self):
        print('Вода нагрелась, дается сигнал')

    def turn_off(self):
        print('Чайник выключился')


chaynik = Kettle()
chaynik.turn_on()







# class Kettle:
#     def __init__(self):
#          self.__brand = "Скайсмарт"

#     def turn_on(self):
#         print(f'Чайник {self.__brand} включился')
#         self.__boil()
#         self.__check_t()
#         self.__beep()
#         self.__turn_off()

#     # Private - скрытый метод
#     def __boil(self):
#         print('Вода греется...')

#     def __check_t(self):
#         print('Проверяется температура')

#     def __beep(self):
#         print('Вода нагрелась, дается сигнал')

#     def __turn_off(self):
#         print('Чайник выключился')


# chaynik = Kettle()
# chaynik.turn_on()





