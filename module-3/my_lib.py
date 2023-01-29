def divide_nums(a, b):
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


