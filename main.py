import tkinter as tk

from todolist.gui import ToDoApp


def main():
    root = tk.Tk()
    ToDoApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
