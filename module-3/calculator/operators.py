def divide_nums(a: float, b: float) -> float:
    result = 0
    try:
        result = float(a) / float(b)
    except ZeroDivisionError:
        print('На ноль делить нельзя')
    except ValueError:
        print('Функция работает только с числами')
    except Exception as e:
        print(e)
    finally:
        return result


def sum_nums(a: float, b: float) -> float:
    result = 0
    try:
        result = float(a) + float(b)
    except ValueError:
        print('Функция работает только с числами')
    except Exception as e:
        print(e)
    finally:
        return result
    

def sub_nums(a: float, b: float) -> float:
    result = 0
    try:
        result = float(a) - float(b)
    except ValueError:
        print('Функция работает только с числами')
    except Exception as e:
        print(e)
    finally:
        return result
    

def multiply_nums(a: float, b: float) -> float:
    result = 0
    try:
        result = float(a) * float(b)
    except ValueError:
        print('Функция работает только с числами')
    except Exception as e:
        print(e)
    finally:
        return result



if __name__ == "__main__":

    print("Тестим функции")

    # Тестируем функции
    print(sum_nums(4, 6))
    print(sub_nums(4, 't'))
    print(multiply_nums(4, 't'))
