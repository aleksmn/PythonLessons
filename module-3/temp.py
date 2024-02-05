def convert_C_to_F(tempC):
    return tempC * (9/5) + 32

def convert_F_to_C(tempF):
    return (tempF - 32) * 5/9

def convert_temp(temp_string):
    # 32f -> 0.0c
    if temp_string[-1] == "f":
        t = convert_F_to_C(int(temp_string[:-1]))
        return str(t) + "c"

    elif temp_string[-1] == "c":
        t = convert_C_to_F(int(temp_string[:-1]))
        return str(t) + "f"
    
    else:
        print("Ошибка ввода")


print(convert_temp("32f"))
print(convert_temp("0c"))