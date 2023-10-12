from tkinter import *
from tkinter import messagebox


def newExp():
    exp = my_entry.get()
    if exp != "":
        lb.insert(END, exp)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("warning", "Please Enter Adding Element In List ")


def deleteExp():
    lb.delete(ANCHOR)
   

ws = Tk()
ws.geometry('500x450+500+200')
ws.title('Task 1 for codesoft')
ws.config(bg='skyblue')
ws.resizable(width=False, height=False)

frame = Frame(ws)
frame.pack(pady=10)

lb = Listbox(
    frame,
    width=25,
    height=8,
    font=('Times', 18),
    bd=0,
    fg='#464646',
    highlightthickness=0,
    selectbackground='black',
    activestyle="none",

)
lb.pack(side=LEFT, fill=BOTH)

exp_list = [
    'DAA',
    'DM',
    'OS',
    'SE',
    'TOC',
    'CAO',
    'BC',
    'NM'
]

for item in exp_list:
    lb.insert(END, item)

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

my_entry = Entry(
    ws,
    font=('times', 24)
)

my_entry.pack(pady=20)

button_frame = Frame(ws)
button_frame.pack(pady=20)

addExp_btn = Button(
    button_frame,
    text='Add Exp',
    font=('times 14'),
    bg='red',
    padx=20,
    pady=10,
    command=newExp
)
addExp_btn.pack(fill=BOTH, expand=True, side=LEFT)

delExp_btn = Button(
    button_frame,
    text='Delete Exp',
    font=('times 16'),
    bg='PINK',
    padx=20,
    pady=10,
    command=deleteExp
)
delExp_btn.pack(fill=BOTH, expand=True, side=LEFT)

ws.mainloop()