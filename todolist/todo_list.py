from todolist.task import Task


class ToDoList:
    """Singly linked list of Task nodes."""

    def __init__(self):
        self.first_node = None
        self.last_node = None

    def add_task(self, title, description):
        task = Task(title, description)
        if self.first_node is None:
            self.first_node = task
            self.last_node = task
        else:
            self.last_node.next = task
            self.last_node = task
        return task

    def remove_task(self, index):
        if self.first_node is None:
            return False

        if index == 0:
            self.first_node = self.first_node.next
            if self.first_node is None:
                self.last_node = None
            return True

        previous_node = self.first_node
        current_node = self.first_node.next
        current_index = 1
        while current_node is not None:
            if current_index == index:
                previous_node.next = current_node.next
                if current_node == self.last_node:
                    self.last_node = previous_node
                return True
            previous_node = current_node
            current_node = current_node.next
            current_index += 1

        return False

    def get_task(self, index):
        current_node = self.first_node
        current_index = 0
        while current_node is not None:
            if current_index == index:
                return current_node
            current_node = current_node.next
            current_index += 1
        return None

    def complete_task(self, index):
        task = self.get_task(index)
        if task is not None:
            task.mark_completed()
            return True
        return False

    def __iter__(self):
        current_node = self.first_node
        while current_node is not None:
            yield current_node
            current_node = current_node.next

    def __len__(self):
        return sum(1 for _ in self)
