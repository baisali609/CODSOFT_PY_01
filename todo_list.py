
class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({'task': task, 'completed': False})

    def view_tasks(self):
        for index, task in enumerate(self.tasks, start=1):
            status = '✓' if task['completed'] else 'X'
            print(f"{index}. {task['task']} [{status}]")

    def mark_task_completed(self, task_number):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1]['completed'] = True

    def delete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            self.tasks.pop(task_number - 1)


def main():
    todo_list = ToDoList()
    
    while True:
        print("\nTo-Do List Application")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            todo_list.view_tasks()
        elif choice == '2':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '3':
            task_number = int(input("Enter the task number to mark as completed: "))
            todo_list.mark_task_completed(task_number)
        elif choice == '4':
            task_number = int(input("Enter the task number to delete: "))
            todo_list.delete_task(task_number)
        elif choice == '5':
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
