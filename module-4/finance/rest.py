def receipt():
    summa = 0
    with open('receipt.txt', 'r', encoding='utf-8') as f:
        for line in f:
            price = line.strip().split()[1]
            summa = summa + int(price)
    print('Итого:', summa)

def show_food():
    food = []
    with open('receipt.txt', 'r', encoding='utf-8') as f:    
        # Вывод построчно
        for line in f:
            # print(line.split())
            food.append(line.split()[0])

    print(food) 

def restaurant_data():
    restaurant = {"details": []}
    # Открываем файл для чтения
    with open("restaurant.txt", "r", encoding="utf-8") as file:
        for item in file.read().split("***"):
            item_list = item.strip().split("\n")

            restaurant['details'].append({
                "administrator": item_list[0],
                "workers": item_list[1].split(', '),
                "turnover": int(item_list[2]),
                "revenue": int(item_list[3]),
                "tips": int(item_list[4])
            })
    
    return restaurant



if __name__ == "__main__":
    # receipt()
    # show_food()
    print(restaurant_data())