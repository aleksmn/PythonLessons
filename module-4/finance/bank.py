def suggestions():
    print("Предложения SkysmartBank")

    # Открываем файл для чтения
    # r - read 
    with open("suggestions.txt", "r", encoding="utf-8") as file:
        # прочитаем файл построчно
        for line in file:
            print(line.strip())



def feedback():
    text = input("Пожалуйста, введите свой отзыв: ")

    with open("feedback.txt", "a+", encoding="utf-8") as file:
        file.write(text + "\n")
        # file.seek(0)
        # print(file.read())


# Точка входа в программу
if __name__ == "__main__":
    suggestions()