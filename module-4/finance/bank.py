def suggestions():
    print("Предложения SkysmartBank")
    with open("suggestions.txt", "r", encoding='utf-8') as file:
        for line in file:  
            print(line.strip())


def complain():
    text = input("Введите текст жалобы: ")
    # "a" - дописать
    with open("complains.txt", 'a', encoding="utf-8") as file:
        file.write(text + "\n")

    print("Ваша жалоба будет рассмотрена в скором времени.")





if __name__ == "__main__":

    complain()
