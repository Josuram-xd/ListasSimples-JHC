import tkinter as tk
from tkinter import messagebox

from todolist.todo_list import ToDoList


class ToDoApp:
    """Tkinter GUI that drives a ToDoList."""

    def __init__(self, root):
        self.todo_list = ToDoList()
        self.root = root

        self._configure_window()
        self._build_form()
        self._build_list()
        self._build_actions()

        self.refresh_list()

    def _configure_window(self):
        self.root.title("ToDo List")
        self.root.geometry("420x420")
        self.root.resizable(False, False)

    def _build_form(self):
        form_frame = tk.Frame(self.root, padx=10, pady=10)
        form_frame.pack(fill="x")

        tk.Label(form_frame, text="Title:").grid(row=0, column=0, sticky="w")
        self.title_entry = tk.Entry(form_frame, width=35)
        self.title_entry.grid(row=0, column=1, pady=2)

        tk.Label(form_frame, text="Description:").grid(row=1, column=0, sticky="w")
        self.description_entry = tk.Entry(form_frame, width=35)
        self.description_entry.grid(row=1, column=1, pady=2)

        tk.Button(form_frame, text="Add task", command=self.add_task).grid(
            row=2, column=0, columnspan=2, pady=8
        )

    def _build_list(self):
        list_frame = tk.Frame(self.root, padx=10)
        list_frame.pack(fill="both", expand=True)

        self.listbox = tk.Listbox(list_frame, height=12)
        self.listbox.pack(side="left", fill="both", expand=True)

        scrollbar = tk.Scrollbar(list_frame, command=self.listbox.yview)
        scrollbar.pack(side="right", fill="y")
        self.listbox.config(yscrollcommand=scrollbar.set)

    def _build_actions(self):
        button_frame = tk.Frame(self.root, padx=10, pady=10)
        button_frame.pack(fill="x")

        tk.Button(button_frame, text="Complete", command=self.complete_task).pack(
            side="left", expand=True, fill="x", padx=2
        )
        tk.Button(button_frame, text="Remove", command=self.remove_task).pack(
            side="left", expand=True, fill="x", padx=2
        )

    def refresh_list(self):
        self.listbox.delete(0, tk.END)
        for task in self.todo_list:
            pointer = hex(id(task))
            next_pointer = hex(id(task.next)) if task.next is not None else "None"
            self.listbox.insert(
                tk.END, f"{task} | ptr={pointer} -> next={next_pointer}"
            )

    def get_selected_index(self):
        selection = self.listbox.curselection()
        if not selection:
            messagebox.showwarning("No selection", "Select a task first.")
            return None
        return selection[0]

    def add_task(self):
        title = self.title_entry.get().strip()
        description = self.description_entry.get().strip()

        if not title:
            messagebox.showwarning("Missing title", "The task title is required.")
            return

        self.todo_list.add_task(title, description)
        self.title_entry.delete(0, tk.END)
        self.description_entry.delete(0, tk.END)
        self.refresh_list()

    def complete_task(self):
        index = self.get_selected_index()
        if index is None:
            return
        self.todo_list.complete_task(index)
        self.refresh_list()

    def remove_task(self):
        index = self.get_selected_index()
        if index is None:
            return
        self.todo_list.remove_task(index)
        self.refresh_list()
