def suggestions():
    print("Предложения SkysmartBank")
    with open("suggestions.txt", "r", encoding='utf-8') as f:
        text = f.read()

    print(text)

def complain():
    print("Оставить жалобу")





if __name__ == "__main__":

    suggestions()