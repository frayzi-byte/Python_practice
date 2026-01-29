class Task:
    def __init__(self, name: str, task_id: int):
        self.name = name
        self.completed = False
        self.id = task_id


tasks = []


def add_task():
    while True:
        add = input("Would you like to add a new task? (yes/no):\n").lower()

        match add:
            case "yes":
                name = input("Enter task name:\n")
                task_id = len(tasks) + 1
                new_task = Task(name, task_id)
                tasks.append(new_task)
                print(f"Task '{name}' added with id {task_id}")
            case "no":
                break
            case _:
                print("Please type yes or no")


add_task()