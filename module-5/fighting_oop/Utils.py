import os


class Utils:
    def clear(self):
        return os.system('cls||clear')     # os.system('clear') для Linux и MacOS

    def go_on(self):
        input('Нажмите Enter, чтобы продолжить')
        self.clear()

    def is_valid(self, user_input, data_range=''):
        if len(user_input) == 0:
            print('Ошибка ввода. Вы ввели пустую строку.')
            return False
        elif data_range != '' and (int(user_input) < data_range[0] or int(user_input) > data_range[1]):
            print(f'Ошибка ввода. Введите числа от {data_range[0]} до {data_range[-1]}.')
            return False
        else:
            return True