import client
import bank
import plot

import os


def main():
    command = ""
    while command != "10":
        os.system("cls")  # очистка терминала
        print("Доступные действия: ")
        print("1 - посмотреть предложения банка")
        print("2 - оставить отзыв")
        print("3 - информация о счетах")
        print("4 - посмотреть прогноз доходов и расходов")
        print("5 - добавить транзакцию")
        print("6 - график доллара к рублю")
        print("7 - график доллара к биткоину ")
        print("8 - график китайского юаня к доллару ")
        print("9 - [добавить свою функцию] ")
        print("10 - выйти")

        command = input("Выберите действие: ")

        if command == "1":
            bank.suggestions()
        elif command == "2":
            bank.feedback()
        elif command == "3":
            client.show_info()
        elif command == "4":
            client.predict()
        elif command == "5":
            client.make_transaction()
        elif command == "6":
            plot.plot_rub_usd()
        elif command == "7":
            plot.plot_usd_btc()
        elif command == "8":
            plot.plot_cny_usd()
        elif command == "10":
            print("До свидания!")
            break
        else:
            print("Действие не распознано. Попробуйте еще раз.")

        input("Enter чтобы продолжить")


# точка входа
if __name__ == "__main__":
    main()
