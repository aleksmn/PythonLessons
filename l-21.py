def convertTemp(temp, scale="c"):
    # print("Переводим температуру", temp)
    # print("из шкалы", scale)

    if scale == "c":
        new_temp = temp * 1.8 + 32
    elif scale == "f":
        new_temp = (temp - 32) / 1.8
    else:
        new_temp = None

    return new_temp


print(convertTemp(0, "f"))
