import time
import os


timer = int(input("Введите кол-во секунд   "))

print(f"Таймер на {timer} сек.")
for x in range(timer):
    print(x)
    time.sleep(1)
    # os.system("cls")
    os.system('clear')
