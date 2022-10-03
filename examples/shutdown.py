import os

# Через 30 сек на Windows:
# os.system("shutdown /s /t 30")

minutes = input('Через сколько минут выключить компьютер?\n')

# seconds = int(minutes) * 60 


os.system("shutdown " + str(minutes))

# Отменить:
# shutdown / a
