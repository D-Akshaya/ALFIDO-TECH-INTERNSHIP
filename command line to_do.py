class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self):
        task = input("Enter a task: ")
        self.tasks.append(task)
        print(f"Task '{task}' added.")

    def remove_task(self):
        if self.tasks:
            self.view_tasks()
            try:
                task_number = int(input("Enter the task number to remove: "))
                if task_number > 0 and task_number <= len(self.tasks):
                    task = self.tasks.pop(task_number - 1)
                    print(f"Task '{task}' removed.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Invalid task number.")
        else:
            print("No tasks.")

    def view_tasks(self):
        if self.tasks:
            print("Your tasks:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")
        else:
            print("No tasks.")

def main():
    todo = ToDoList()

    while True:
        print("\nTo-Do List App")
        print("1. Add task")
        print("2. Remove task")
        print("3. View tasks")
        print("4. Quit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            todo.add_task()
        elif choice == "2":
            todo.remove_task()
        elif choice == "3":
            todo.view_tasks()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


