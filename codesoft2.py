import tkinter as tk

def on_button_click(event):
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = str(eval(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

root = tk.Tk()
root.geometry("400x600")
root.title(" Task2 for Codesoft-Calculator")

entry = tk.Entry(root, font="Helvetica 24", justify=tk.RIGHT)
entry.pack(fill=tk.BOTH, ipadx=8, padx=10, pady=10, expand=True)

button_frame = tk.Frame(root)
button_frame.pack(expand=True, fill=tk.BOTH)

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+",
    "C"
]

row, col = 1, 0

for button_text in buttons:
    button = tk.Button(button_frame, text=button_text, font="Helvetica 18", width=5, height=2)
    button.grid(row=row, column=col, padx=5, pady=5)
    button.bind("<Button-1>", on_button_click)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
