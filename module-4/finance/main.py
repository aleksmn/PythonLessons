from client import *
from bank import *
from plot import *
import os

if __name__ == "__main__":

    load()

    command = ""
    while command != "10":
        os.system("cls||clear")
        print("Доступные действия: ")
        print("1 - посмотреть предложения банка")
        print("2 - отправить жалобу")
        print("3 - информация о счетах")
        print("4 - посмотреть прогноз доходов и расходов")
        print("5 - добавить транзакцию")
        print("6 - график доллара к рублю")
        print("7 - график доллара к биткоину ")
        print("10 - выйти")

        command = input("Выберите действие: ")

        if command == "1":
            suggestions()
        elif command == "2":
            complain()
        elif command == "3":
            show_info()
        elif command == "4":
            predict()        
        elif command == "5":
            make_transaction()
        elif command == "6":
            plot_rub_usd()
        elif command == "7":
            plot_usd_btc()
        elif command == "10":
            print("Сохранение изменений")
            save()
            print("До свидания!")
            break

        else:
            print("Действие не распознано. Попробуйте еще раз.")

        input("Enter чтобы продолжить")