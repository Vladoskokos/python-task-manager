def create_task(title):
    task = {"title": title, "done": False}
    return task


def show_task_status(task_list):
    if not task_list:
        print("Список задач пуст")
        return
    for number, task in enumerate(task_list, 1):
        print(f"{number} {task["title"]}")
        if task["done"]:
            print("Готово")
        else:
            print("Нужно выполнить")


def complete_task(task):
    task["done"] = True


def complete_by_number(task_list, number_text):
    if number_text.isdecimal():
        task_number = int(number_text)
        if task_number >= 1 and task_number <= len(task_list):
            task_index = task_number - 1
            selected_task = task_list[task_index]
            complete_task(selected_task)
            print(f"Задача отмечена выполненной: {selected_task["title"]}")
        else:
            print("Такого номера задачи нет")
    else:
        print("Введите номер цифрами")


tasks = []
initial_task = create_task("Разобрать меню")
tasks.append(initial_task)


while True:
    print("1 - Показать задачи")
    print("2 - Новая задача")
    print("3 - Отметить выполненной")
    print("0 - Выход")
    command = input("Выбери действие: ")
    command = command.strip()
    if command == "0":
        print("До встречи!")
        break
    elif command == "1":
        show_task_status(tasks)
    elif command == "2":
        user_title = input("Новая задача: ")
        user_title = user_title.strip()
        if not user_title:
            print("Название не введено")
        else:
            user_task = create_task(user_title)
            tasks.append(user_task)
    elif command == "3":
        number_text = input("Номер задачи: ")
        number_text = number_text.strip()
        complete_by_number(tasks, number_text)
    else:
        print("Неизвестная команда")