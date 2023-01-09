from tkinter import *
from tkinter import messagebox
import random

def pass_gen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = "".join(password_list)
    pass_input.insert(0, password)



def save():
    w = website_input.get()
    e = email_input.get()
    p = pass_input.get()
    if w == "" or p == "" or e == "":
        messagebox.askokcancel(title=w, message=f"Don't leave any fields empty!")

    else:
         is_ok = messagebox.askokcancel(title=w, message=f"These are the details entered: \nEmail:{e} \nPassword:{p}\nis it ok to save?")

         if is_ok:
            with open(file="data.txt", mode="a") as info:
                 info.write(w + "|" + e + "|" + p + "\n")
                 website_input.delete(0, END)
                 pass_input.delete(0, END)




window = Tk()
window.title("PASSWORD MANAGER")
window.minsize(height=200, width=200)
window.config(pady=50, padx=50)

canvas = Canvas()
myimg = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=myimg, anchor="center")
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_input = Entry(width=38)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

email_label = Label(text="Email/User_Name:")
email_label.grid(column=0, row=2)

email_input = Entry(width=38)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "ash92199@gmail.com")

pass_label = Label(text="Password:")
pass_label.grid(column=0, row=3)

pass_input = Entry()
pass_input.grid(column=1, row=3)

generate_pass = Button(text="Generate Password", command=pass_gen)
generate_pass.grid(row=3, column=2)

add = Button(text="Add", width=36, command=save)
add.grid(column=1, row=4, columnspan=2)








window.mainloop()