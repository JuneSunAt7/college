
class ToDoList:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

        print("***Command Line ToDo List***")
        while True:
            print("Menu:")
            print("1. Create task")
            print("2. View tasks")
            print("3. Delete task")
            print("4. Exit")
            try:
                self.option = int(input("> "))
                self.choose_option(self.option)
                if self.option == 4:  # exit
                    break
            except ValueError:
                print("Invalid option")

    def choose_option(self, num_option):
        if num_option == 1:
            self.create_task()
        elif num_option == 2:
            self.view_tasks()
        elif num_option == 3:
            self.delete_task()
        elif num_option == 4:
            print("Exit...")
            return

    def create_task(self):
        descr = input("Description: ")
        self.add_task_to_local_storage(descr)
        print("Task is added")

    def view_tasks(self):
        if not self.tasks:  # check if empty list tasks
            print("List of tasks is empty")
            return
        print("Tasks: ")
        for task in self.tasks:
            print(f" {task['id']}. {task['description']}")

    def delete_task(self):
        try:
            id_task = int(input("Input id for delete: "))
            task_to_delete = next((task for task in self.tasks if task['id'] == id_task), None)
            if task_to_delete:
                self.tasks.remove(task_to_delete)
                print(f"Task {id_task} is removed")
            else:
                print(f"Task with id {id_task} not found")
        except ValueError:
            print("Invalid input. Please enter a valid ID.")

    def add_task_to_local_storage(self, description):
        if not description.strip(): # check if empty
            print("Description is empty")
            return
        task = { # create as map structure
            "id": self.next_id,
            "description": description
        }
        self.tasks.append(task)
        self.next_id += 1

if __name__ == '__main__':
    local_todo = ToDoList()     # class instance











