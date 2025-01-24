import tkinter as tk
from tkinter import messagebox
import hashlib

def add():
    # accepting input from the user
    username = entryName.get()
    # accepting password input from the user
    password = entryPassword.get()

    # so if the user inputs both the username and password
    # it would be put into the text file ( passwords.txt)
    # very secure dont worry
    if username and password:
        with open("passwords.txt", 'a') as f:
            f.write(f"{username} {password}\n")
        messagebox.showinfo("Success", "Password added !!")
    else:
        messagebox.showerror("Error", "Please enter both the fields")


def getlist():
    # creating a dictionary
    passwords = {}

    # adding a try block, this will catch errors such as an empty file or others
    try:
        with open("passwords.txt", 'r') as f:
            for k in f:
                i = k.split(' ')
                passwords[i[0]] = i[1]
    except:
        print("No passwords found!!")

    if passwords:
        mess = "List of passwords:\n"
        for name, password in passwords.items():
            # generating a proper message
            mess += f"Password for {name} is {password}\n"
        # Showing the message
        messagebox.showinfo("Passwords", mess)
    else:
        messagebox.showinfo("Passwords", "Empty List !!")


def encrypt():
    PASSWORD_PATH = "passwords.txt"
    try:
        with open(PASSWORD_PATH) as file:
            record_list = file.readlines()
    except FileNotFoundError:
        messagebox.showinfo(
                "Error", 
                f"{PASSWORD_PATH} file not found"
            )
        return
    
    current_user = entryName.get()
    for record in record_list:
        if record.split()[0] == current_user:
            current_password = record.split()[1]
            res = hashlib.sha256(current_password.encode('utf-8')).hexdigest()
            messagebox.showinfo(
                "Success", 
                f"Hashed version of password for user {current_user} is {res}"
            )
            return
        
    messagebox.showinfo(
        "Failure", 
        f"Username not found"
    )
      

if __name__ == "__main__":
    app = tk.Tk()
    app.geometry("560x270")
    # Change the background color using configure
    app.configure(bg='gray9')
    app.title("KaiPass version 1")

    # Username block
    labelName = tk.Label(app, text="USERNAME:",bg='gray9',fg='MediumPurple1')
    labelName.grid(row=0, column=0, padx=15, pady=15)
    entryName = tk.Entry(app)
    entryName.grid(row=0, column=1, padx=15, pady=15)

    # Password block
    labelPassword = tk.Label(app, text="PASSWORD:",bg='gray9',fg='MediumPurple1')
    labelPassword.grid(row=1, column=0, padx=10, pady=5)
    entryPassword = tk.Entry(app)
    entryPassword.grid(row=1, column=1, padx=10, pady=5)

    # Add button
    buttonAdd = tk.Button(app, text="Add", command=add,bg='thistle1')
    buttonAdd.grid(row=2, column=0, padx=15, pady=8, sticky="we")

   
    # List Button
    buttonList = tk.Button(app, text="List", command=getlist, bg='thistle1')
    buttonList.grid(row=3, column=0, padx=15, pady=8, sticky="we")


    # Encrypt Button
    buttonList = tk.Button(app, text="Encrypt", command=encrypt, bg='thistle1')
    buttonList.grid(row=4, column=0, padx=15, pady=8, sticky="we")

    app.mainloop()