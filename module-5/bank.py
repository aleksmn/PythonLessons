class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def set_balance(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def add(self, amount):
        self.__balance += amount

    def remove(self, value):
        if value > self.__balance:
            print("Ошибка: на счете недостаточно средств")
        else:
            self.__balance -= value


if __name__ == "__main__":
    
    account = BankAccount(1000)

    print(account.get_balance()) # 1000

    account.remove(500)
    print(account.get_balance()) # 500

    account.add(1000)
    print(account.get_balance()) # 1500

    account.set_balance(5000)
    print(account.get_balance()) # 5000