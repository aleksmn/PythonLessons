# Пример инкапсуляции

# class Kettle:
#     def turn_on(self):
#         print('Чайник включился')
#         self.boil()
#         self.check_t()
#         self.beep()
#         self.turn_off()

#     def boil(self):
#         print('Вода греется...')

#     def check_t(self):
#         print('Проверяется температура')

#     def beep(self):
#         print('Вода нагрелась, дается сигнал')

#     def turn_off(self):
#         print('Чайник выключился')


# chaynik = Kettle()
# chaynik.turn_on()



# Пример инкапсуляции

class Kettle:
    def turn_on(self):
        print('Чайник включился')
        self.__boil()
        self.__check_t()
        self.__beep()
        self._turn_off()

    # Private
    def __boil(self):
        print('Вода греется...')

    def __check_t(self):
        print('Проверяется температура')

    def __beep(self):
        print('Вода нагрелась, дается сигнал')
    # Protected
    def _turn_off(self):
        print('Чайник выключился')


chaynik = Kettle()
chaynik.turn_on()