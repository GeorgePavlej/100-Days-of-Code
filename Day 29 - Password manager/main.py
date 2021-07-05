from tkinter import *
from tkinter import messagebox
import random
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1  ', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    entry_pass_label.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    website = entry_web_label.get()
    email = entry_email_label.get()
    password = entry_pass_label.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                #Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            #Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                #Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            entry_web_label.delete(0, END)
            entry_pass_label.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    website = entry_web_label.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data file found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"Sorry, the website {website} is not saved!")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
pass_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pass_image)
canvas.grid(row=0, column=1)

# Labels

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

pass_label = Label(text="Password:")
pass_label.grid(row=3, column=0)

# Entry

entry_web_label = Entry(width=35)
entry_web_label.focus()
entry_web_label.grid(row=1, column=1, columnspan=2, sticky="EW")

entry_email_label = Entry(width=35)
entry_email_label.insert(0, "georgepavlej@gmail.com")
entry_email_label.grid(row=2, column=1, columnspan=2, sticky="EW")

entry_pass_label = Entry(width=21)
entry_pass_label.grid(row=3, column=1, sticky="EW")

# Buttons

gen_pass_button = Button(text="Generate Password", command=generate_password)
gen_pass_button.grid(row=3, column=2)

search_button = Button(text="Search", command=find_password)
search_button.grid(row=1, column=2, columnspan=2, sticky="EW")

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")



window.mainloop()
