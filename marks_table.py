import tkinter as tk
from tkinter import ttk

def create_simple_table():
    # Sample student data
    student_data = [
        ("Rama", 85, 92,90),
        ("Bhima", 72, 65,60),
        ("Soma", 95, 90,85),
        ("Reema",80,70,65)
    ]

    root = tk.Tk()
    root.title("Student Marks")

    # Create a Treeview widget, a versatile table-like widget in Tkinter
    tree = ttk.Treeview(root, columns=("Name", "Math", "Science","English"), show="headings") # Set column headings

    # Define column headings
    tree.heading("Name", text="Name")
    tree.heading("Math", text="Math")
    tree.heading("Science", text="Science")
    tree.heading("English", text="English")

    # Insert data into the Treeview
    for name, math_mark, science_mark ,english_mark in student_data:
        tree.insert("", "end", values=(name, math_mark, science_mark,english_mark))

    tree.pack(padx=10, pady=10) # Place the table in the window

    root.mainloop()

if __name__ == "__main__":
    create_simple_table()
