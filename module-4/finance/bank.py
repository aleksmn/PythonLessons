def suggestions():
    print("Предложения SkysmartBank")
    with open("suggestions.txt", "r", encoding='utf-8') as f:
        text = f.read()

    print(text)

def complain():
    text = input("Введите текст жалобы: ")

    with open("complains.txt", 'a', encoding="utf-8") as file:
        file.write("\n" + text)

    print("Ваша жалоба будет рассмотрена в скором времени.")








if __name__ == "__main__":

    # suggestions()
    complain()