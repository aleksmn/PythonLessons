# Вот тебе код для экспериментов
class Kettle:
    def turn_on(self):
        print('Чайник включился')
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
