import tkinter as tk
from tkinter import messagebox

def login():
    username = entry_username.get()
    password = entry_password.get()

    # Here you can add your own authentication logic
    if username == "admin" and password == "password":
        messagebox.showinfo("Login Info", "Welcome Admin")
    else:
        messagebox.showerror("Login Error", "Incorrect Username or Password")

# Create the main window
root = tk.Tk()
root.title("Login Form")
root.geometry("300x200")

# Username label and text entry box
label_username = tk.Label(root, text="Username")
label_username.pack(pady=10)
entry_username = tk.Entry(root)
entry_username.pack(pady=5)

# Password label and password entry box
label_password = tk.Label(root, text="Password")
label_password.pack(pady=10)
entry_password = tk.Entry(root, show='*')
entry_password.pack(pady=5)

# Login button
login_button = tk.Button(root, text="Login", command=login)
login_button.pack(pady=20)

# Run the application
root.mainloop()
