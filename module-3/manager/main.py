from tkinter import *


def move_task(event, source_list, target_list):
    # Получение выбранной задачи
    task = source_list.get(source_list.curselection())

    # Перемещение задачи из одной доски в другую
    source_list.delete(source_list.curselection())
    target_list.insert(END, task)

def create_task(event):
    # Добавление новой задачи в список "To Do"
    task = entry.get()
    if task:
        todo_list.insert(END, task)
        entry.delete(0, END)

# Создание главного окна
root = Tk()
root.title("Kanban Board")

# Создание списков задач
todo_list = Listbox(root, height=10, width=30)
in_progress_list = Listbox(root, height=10, width=30)
done_list = Listbox(root, height=10, width=30)

# Расположение списков на доске
todo_list.grid(row=0, column=0, padx=10, pady=10)
in_progress_list.grid(row=0, column=1, padx=10, pady=10)
done_list.grid(row=0, column=2, padx=10, pady=10)

# Создание виджетов интерфейса
add_label = Label(root, text="Add Task:")
add_label.grid(row=1, column=0, pady=5)

entry = Entry(root, width=30)
entry.grid(row=1, column=1, pady=5)

add_button = Button(root, text="Add", width=10)
add_button.grid(row=1, column=2, pady=5)
add_button.bind("<Button-1>", create_task)

# Привязка событий перемещения задачи между списками
todo_list.bind("<Button-1>", lambda e: move_task(e, todo_list, in_progress_list))
in_progress_list.bind("<Button-1>", lambda e: move_task(e, in_progress_list, done_list))
done_list.bind("<Button-1>", lambda e: move_task(e, done_list, todo_list))

# Запуск главного цикла событий
root.mainloop()
