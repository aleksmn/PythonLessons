def receipt():
    summa = 0
    with open('receipt.txt', 'r', encoding='utf-8') as f:
        for line in f:
            print(line.strip())


def restaurant_data():
    restaurant = {"details": []}
    with open("receipt.txt", 'r', encoding='utf-8') as f:
        for item in f.read().split('***\n'):
            item_list = item.split('\n')

            restaurant['details'].append({
                "administrator":item_list[0],
                "workers":item_list[1].split(", "),
                "turnover":item_list[2],
                "revenue":item_list[3],
                "tips":item_list[4],
            })

    # Вывод словаря
    return restaurant



if __name__ == "__main__":
    receipt()

    # print(restaurant_data()) 