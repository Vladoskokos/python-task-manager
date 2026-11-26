import json


def save_tasks(task_list):
    json_text = json.dumps(task_list, ensure_ascii=False)
    with open("tasks.json", "w", encoding="utf-8") as tasks_file:
        tasks_file.write(json_text)


def load_tasks():
    try:
        with open("tasks.json", "r", encoding="utf-8") as tasks_file:
            json_text = tasks_file.read()
        loaded_data = json.loads(json_text)
        if not isinstance(loaded_data, list):
            print("В файле должен быть список задач")
            return None
        for task in loaded_data:
            if not isinstance(task, dict):
                print("Каждая задача должна быть словарем")
                return None
            if "title" not in task:
                print("В задачи нет ключа title")
                return None
            if "done" not in task:
                print("В задачи нет ключа done")
                return None
            if not isinstance(task["title"], str):
                print("Название задачи должно быть строкой")
                return None
            if not task["title"].strip():
                print("Название задачи не должно быть пустым")
                return None
            if not isinstance(task["done"], bool):
                print("Статус задачи должен быть логическим значением")
                return None
        return loaded_data
    except json.JSONDecodeError:
        print("Некорректный JSON")
        return None
    except FileNotFoundError:
        return []


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
            return True
        else:
            print("Такого номера задачи нет")
    else:
        print("Введите номер цифрами")
    return False


tasks = load_tasks()
if tasks is None:
    print("Не удалось загрузить задачи. Проверь файл tasks.json")
else:
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
                save_tasks(tasks)
        elif command == "3":
            number_text = input("Номер задачи: ")
            number_text = number_text.strip()
            was_completed = complete_by_number(tasks, number_text)
            if was_completed:
                save_tasks(tasks)
        else:
            print("Неизвестная команда")