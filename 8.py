import tkinter as tk

def calculate():
    try:
        result = eval(entry.get())
        label.config(text=f"Result: {result}")
    except:
        label.config(text="Error")

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, width=20, font=("Arial", 16))
entry.pack(pady=10)

btn = tk.Button(root, text="Calculate", command=calculate)
btn.pack(pady=5)

label = tk.Label(root, text="Result:", font=("Arial", 14))
label.pack()

root.mainloop()
