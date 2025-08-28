class TaskNode:
    def __init__(self, subject, description, due_date):
        self.subject = subject
        self.description = description
        self.due_date = due_date
        self.next = None


class TaskList:
    def __init__(self):
        self.head = None 

    def add_task(self, subject, description, due_date):
        new_node = TaskNode(subject, description, due_date)
        if self.head == None:
            new_node.next = self.head
            self.head = new_node
    
    def print_tasks(self):
        current = self.head
        while current:
            print(f"{current.subject}: {current.description} (Due {current.due_date})")
            current = current.next




# main
tasks = TaskList()
tasks.add_task("Maths", "Finish worksheet", "2025-06-20")
tasks.add_task("English", "Read Chapter 5", "2025-06-19")
tasks.add_task("French", "Finish translations", "2025-08-26")
tasks.print_tasks()