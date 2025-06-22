import tkinter as tk
from tkinter import messagebox
import os

FILE_NAME = "tasks.txt"

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("500x500")

        self.task_listbox = tk.Listbox(root, width=40, height=15, font=("Arial", 12))
        self.task_listbox.pack(pady=20)

        self.task_entry = tk.Entry(root, font=("Arial", 12), width=30)
        self.task_entry.pack(pady=5)

        self.add_btn = tk.Button(root, text="Add Task", width=15, command=self.add_task)
        self.add_btn.pack(pady=2)

        self.remove_btn = tk.Button(root, text="Remove Task", width=15, command=self.remove_task)
        self.remove_btn.pack(pady=2)

        self.clear_btn = tk.Button(root, text="Clear All Tasks", width=15, command=self.clear_tasks)
        self.clear_btn.pack(pady=2)

        self.load_tasks()

    def add_task(self):
        task = self.task_entry.get().strip()
        if task == "":
            messagebox.showwarning("Input Error", "Task cannot be empty")
            return
        self.task_listbox.insert(tk.END, task)
        self.task_entry.delete(0, tk.END)
        self.save_tasks()

    def remove_task(self):
        selected = self.task_listbox.curselection()
        if not selected:
            messagebox.showinfo("Select Task", "No task selected")
            return
        self.task_listbox.delete(selected[0])
        self.save_tasks()

    def clear_tasks(self):
        self.task_listbox.delete(0, tk.END)
        self.save_tasks()

    def save_tasks(self):
        tasks = self.task_listbox.get(0, tk.END)
        with open(FILE_NAME, "w") as file:
            for task in tasks:
                file.write(task + "\n")

    def load_tasks(self):
        if os.path.exists(FILE_NAME):
            with open(FILE_NAME, "r") as file:
                for line in file:
                    self.task_listbox.insert(tk.END, line.strip())


# ----------------- Main -----------------
if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
