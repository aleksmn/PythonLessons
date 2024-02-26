def suggestions():
    print("Предложения SkysmartBank")
    with open("suggestions.txt", "r", encoding='utf-8') as file:
        for line in file:
            # .strip убирает все пробелы по краям и переходы на новую строку
            print(line.strip())        



def complain():
    text = input("Введите текст жалобы: ")
    with open("complains.txt", 'a', encoding="utf-8") as file:
        file.write("\n" + text)

    print("Ваша жалоба будет рассмотрена в скором времени.")





if __name__ == "__main__":

    complain()
