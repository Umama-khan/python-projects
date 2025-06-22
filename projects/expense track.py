import tkinter as tk
from tkinter import ttk, messagebox
import csv
from datetime import datetime
import os

FILENAME = "expenses.csv"

class ExpenseTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Expense Tracker")
        self.root.geometry("600x400")

        # Entry fields
        self.desc_entry = tk.Entry(root, width=25)
        self.desc_entry.grid(row=0, column=1, padx=10, pady=5)
        tk.Label(root, text="Description:").grid(row=0, column=0)

        self.amount_entry = tk.Entry(root, width=25)
        self.amount_entry.grid(row=1, column=1, padx=10, pady=5)
        tk.Label(root, text="Amount (Rs):").grid(row=1, column=0)

        self.category_entry = tk.Entry(root, width=25)
        self.category_entry.grid(row=2, column=1, padx=10, pady=5)
        tk.Label(root, text="Category:").grid(row=2, column=0)

        self.date_entry = tk.Entry(root, width=25)
        self.date_entry.grid(row=3, column=1, padx=10, pady=5)
        tk.Label(root, text="Date (YYYY-MM-DD):").grid(row=3, column=0)

        self.add_btn = tk.Button(root, text="Add Expense", command=self.add_expense)
        self.add_btn.grid(row=4, column=1, pady=10)

        # Treeview (table)
        self.tree = ttk.Treeview(root, columns=("Desc", "Amount", "Category", "Date"), show="headings")
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)
        self.tree.grid(row=5, column=0, columnspan=3, padx=10, pady=10)

        self.total_label = tk.Label(root, text="Total: Rs 0", font=("Arial", 12, "bold"))
        self.total_label.grid(row=6, column=1)

        self.load_expenses()

    def add_expense(self):
        desc = self.desc_entry.get()
        amount = self.amount_entry.get()
        category = self.category_entry.get()
        date = self.date_entry.get()

        if not desc or not amount or not category or not date:
            messagebox.showerror("Input Error", "Please fill in all fields.")
            return

        try:
            amount = float(amount)
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Format Error", "Amount must be a number and date in YYYY-MM-DD format.")
            return

        # Insert into table
        self.tree.insert("", "end", values=(desc, f"{amount:.2f}", category, date))

        # Save to CSV
        with open(FILENAME, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([desc, amount, category, date])

        self.update_total()
        self.clear_fields()

    def load_expenses(self):
        if os.path.exists(FILENAME):
            with open(FILENAME, "r") as f:
                reader = csv.reader(f)
                for row in reader:
                    if len(row) == 4:
                        self.tree.insert("", "end", values=(row[0], row[1], row[2], row[3]))
        self.update_total()

    def update_total(self):
        total = 0
        for child in self.tree.get_children():
            total += float(self.tree.item(child)['values'][1])
        self.total_label.config(text=f"Total: Rs {total:.2f}")

    def clear_fields(self):
        self.desc_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)
        self.category_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTracker(root)
    root.mainloop()
