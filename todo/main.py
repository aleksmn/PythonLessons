
print("\n* Список задач *\n")

def print_todo(file):
    print("\n*  Твои задачи  *\n")
    with open(file, 'r', encoding='utf-8') as f:
        for num, line in enumerate(f):
            print(num+1, line, end='')

    print("-"*9)



my_todo = 'todo.txt'

print_todo(my_todo)



user_choice = input("Добавить новую задачу (1)\nУдалить задачи (2)\nВыйти (3)\n")

if user_choice == "1":
    new_task = input("Напишите задачу:\n")
    with open(my_todo, 'a') as f:
        f.write(new_task + "\n")


if user_choice == "2":
    while True:
        to_delete = input("Введите номер задачи, чтобы удалить (0 - удалить все, q - выход)\n")

        if to_delete == "q":
            break

        if to_delete == "0":
            with open(my_todo, 'w') as f:
                print("Удаляем задачи...")
                pass
            break




print_todo(my_todo)