class Task:
    """A single to-do item, doubling as a node of the ToDoList linked list."""

    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False
        self.next = None

    def mark_completed(self):
        self.completed = True

    @property
    def status(self):
        return "Done" if self.completed else "Pending"

    def __str__(self):
        return f"{self.title} - {self.description} ({self.status})"
