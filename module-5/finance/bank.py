def suggestions():
    print("Предложения SkysmartBank")
    with open("suggestions.txt", "r", encoding='utf-8') as f:
        text = f.read()

    print(text)


suggestions()