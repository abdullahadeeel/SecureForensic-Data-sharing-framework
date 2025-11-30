from tkinter import *

def main_menu(user):
    root = Tk()
    root.title(f"Main Interface - {user[4].capitalize()}")
    root.geometry("800x500")
    root.configure(bg="#E8F5E9")
    root.minsize(800, 500)

    # Menu bar
    menubar = Menu(root)

    # Profile menu
    profile_menu = Menu(menubar, tearoff=0)
    profile_menu.add_command(label="View Profile")
    profile_menu.add_command(label="Change Password")
    profile_menu.add_separator()
    profile_menu.add_command(label="Logout", command=root.destroy)
    menubar.add_cascade(label="Profile", menu=profile_menu)

    role = user[4].lower()
    if role == "sender":
        file_menu = Menu(menubar, tearoff=0)
        file_menu.add_command(label="Upload File")
        file_menu.add_command(label="Sent Files")
        menubar.add_cascade(label="File", menu=file_menu)
    elif role == "receiver":
        file_menu = Menu(menubar, tearoff=0)
        file_menu.add_command(label="Incoming Files")
        menubar.add_cascade(label="File", menu=file_menu)
    elif role == "admin":
        user_menu = Menu(menubar, tearoff=0)
        user_menu.add_command(label="Manage Users")
        menubar.add_cascade(label="Users", menu=user_menu)

    root.config(menu=menubar)

    # Welcome Label
    welcome_lbl = Label(root, text=f"Welcome, {user[1]} ({user[4].capitalize()})", font=("Arial", 18, "bold"), bg="#E8F5E9")
    welcome_lbl.pack(pady=50)

    root.mainloop()



