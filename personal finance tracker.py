import tkinter as tk
from tkinter import messagebox, ttk
import csv
from datetime import datetime

# Initialize main window
root = tk.Tk()
root.title("Personal Finance Tracker")
root.geometry("500x600")

# List to store expenses
expenses = []

# Function to add an expense
def add_expense():
    amount = entry_amount.get()
    category = combo_category.get()
    date = entry_date.get()

    if not amount or not category or not date:
        messagebox.showerror("Input Error", "All fields are required.")
        return

    try:
        float(amount)
    except ValueError:
        messagebox.showerror("Input Error", "Amount must be a number.")
        return

    expenses.append([amount, category, date])
    tree.insert("", "end", values=(amount, category, date))
    entry_amount.delete(0, tk.END)
    combo_category.set("")
    entry_date.delete(0, tk.END)

# Function to export expenses to CSV
def export_csv():
    with open("expenses.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Amount", "Category", "Date"])
        writer.writerows(expenses)
    messagebox.showinfo("Export", "Expenses exported to expenses.csv")

# Function to summarize expenses
def show_summary():
    summary = {}
    for expense in expenses:
        category = expense[1]
        amount = float(expense[0])
        summary[category] = summary.get(category, 0) + amount

    summary_text = "\n".join([f"{cat}: ${amt:.2f}" for cat, amt in summary.items()])
    messagebox.showinfo("Summary", summary_text)

# Labels and Inputs
label_title = tk.Label(root, text="Add Expense", font=("Helvetica", 16))
label_title.pack(pady=10)

entry_amount = tk.Entry(root, width=30)
entry_amount.pack(pady=5)
entry_amount.insert(0, "Amount")

combo_category = ttk.Combobox(root, values=["Food", "Transport", "Utilities", "Entertainment", "Other"], width=27)
combo_category.pack(pady=5)
combo_category.set("Select Category")

entry_date = tk.Entry(root, width=30)
entry_date.pack(pady=5)
entry_date.insert(0, datetime.now().strftime("%Y-%m-%d"))

btn_add = tk.Button(root, text="Add Expense", command=add_expense)
btn_add.pack(pady=10)

# Treeview for displaying expenses
columns = ("Amount", "Category", "Date")
tree = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
tree.pack(pady=20)

# Buttons
btn_summary = tk.Button(root, text="Show Summary", command=show_summary)
btn_summary.pack(pady=5)

btn_export = tk.Button(root, text="Export to CSV", command=export_csv)
btn_export.pack(pady=5)

# Run app
root.mainloop()