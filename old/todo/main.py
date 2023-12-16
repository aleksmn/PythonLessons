file = 'todo.txt'

def print_todo():
    print("\n*  Твои задачи  *\n")
    with open(file, 'r', encoding='utf-8') as f:
        for num, line in enumerate(f):
            print(num+1, line, end='')
    print("-"*9)



print_todo()

user_choice = input("Добавить новую задачу (1)\nУдалить задачи (2)\nВыйти (3)\n")

if user_choice == "1":
    new_task = input("Напишите задачу:\n")
    with open(file, 'a', encoding='utf-8') as f:
        f.write(new_task.strip() + "\n")


if user_choice == "2":

    while True:
        to_delete = input("Введите номер задачи, чтобы удалить (0 - удалить все, q - выход)\n")

        if to_delete == "q":
            break

        if to_delete == "0":
            with open(file, 'w', encoding='utf-8') as f:
                print("Удаляем задачи...")
                pass
            break

if user_choice == "3":
    print("Всего доброго!")
    quit()

print_todo()

