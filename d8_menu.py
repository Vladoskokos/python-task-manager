tasks = ["Повторить Python", "Решить задачу", "Погулять"]
while True:
    print("1 - Показать задачи")
    print("2 - Добавить задачу")
    print("3 - Удалить выполненную задачу")
    print("0 - Выход")

    command = input("Выбери действие: ").strip()

    if command == "0":
        print("До встречи!")
        break
    elif command == "1":
        for task in tasks:
            print(task)
        print(f"Всего задач: {len(tasks)}")
    elif command == "2":
        new_task = input("Новая задача? ")
        new_task = new_task.strip()

        if not new_task:
            print("Задача не введена")
        else:
            tasks.append(new_task)
            print("Задача добавлена")
    elif command == "3":
        done_task = input("Какую задачу выполнил? ")
        done_task = done_task.strip()

        if not done_task:
            print("Задача не введена")
        elif done_task in tasks:
            tasks.remove(done_task)
            print("Задача выполнена")
        else:
            print("Такой задачи нет")

    else:
        print("Неизвестная команда")