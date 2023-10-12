import tkinter as tk
import random
import string

def generate_password():
    length = int(length_entry.get())
    complexity = complexity_var.get()
    
    if complexity == "Low":
        characters = string.ascii_letters + string.digits
    elif complexity == "Medium":
        characters = string.ascii_letters + string.digits + string.punctuation
    elif complexity == "High":
        characters = string.ascii_letters + string.digits + string.punctuation + string.whitespace
    else:
        result_label.config(text="Invalid complexity level")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    result_label.config(text="Generated Password: " + password)

# Create the main window
root = tk.Tk()
root.geometry("400x300")
root.title(" Task3 for codesoft-Password Generator")

# Create and pack widgets
length_label = tk.Label(root, text="Password Length:")
length_label.pack()
length_entry = tk.Entry(root)
length_entry.pack()

complexity_label = tk.Label(root, text="Password Complexity:")
complexity_label.pack()

complexity_var = tk.StringVar()
complexity_var.set("Low")

complexity_low = tk.Radiobutton(root, text="Low", variable=complexity_var, value="Low")
complexity_medium = tk.Radiobutton(root, text="Medium", variable=complexity_var, value="Medium")
complexity_high = tk.Radiobutton(root, text="High", variable=complexity_var, value="High")

complexity_low.pack()
complexity_medium.pack()
complexity_high.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
