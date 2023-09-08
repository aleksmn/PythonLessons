# def fib(n):
#     f1, f2 = 0, 1
#     for i in range(n-1):
#         f1, f2 = f2, f1 + f2
#         # print(f2)

#     return f2


def fib_digit(n):
    f1, f2 = 0, 1
    for i in range(n-1):
        f1, f2 = f2%10, (f1 + f2)%10

    return f2



def main():
    n = int(input())
    # print(fib(n))
    print(fib_digit(n))


if __name__ == "__main__":
    main()