import tkinter as tk
from tkinter import *

root = tk.Tk()
root.title("Secure Forensic Data Sharing Framework")
root.geometry("950x600")
root.configure(bg="#d6ecff")


# ---------------- OPEN NEW WINDOWS ----------------
def open_sender_window():
    win = tk.Toplevel(root)
    win.title("Sender Dashboard")
    win.state('zoomed')  # Full screen / maximize
    win.configure(bg="#e6f2ff")

    Label(win, text="Sender Dashboard", font=("Segoe UI", 22, "bold"),
          bg="#e6f2ff", fg="#004a7c").pack(pady=20)

    btns = [
        "Upload File",
        "Encrypt File",
        "Select Transfer Method",
        "Send File",
        "Sent Files History"
    ]

    for text in btns:
        Button(win, text=text, font=("Segoe UI", 14), width=25,
               bg="#4da9ff", fg="white", bd=0, height=2).pack(pady=20)

    # Back button
    Button(win, text="Back", font=("Segoe UI", 14, "bold"),
           bg="#3399ff", fg="white", width=12, height=1,
           command=win.destroy).pack(pady=15)


def open_receiver_window():
    win = tk.Toplevel(root)
    win.title("Receiver Dashboard")
    win.state('zoomed')
    win.configure(bg="#e6f2ff")

    Label(win, text="Receiver Dashboard", font=("Segoe UI", 22, "bold"),
          bg="#e6f2ff", fg="#004a7c").pack(pady=20)

    btns = [
        "View Incoming Files",
        "Enter Decryption Key",
        "Decrypt File",
        "Verify File Integrity",
        "Received Files History"
    ]

    for text in btns:
        Button(win, text=text, font=("Segoe UI", 14), width=25,
               bg="#4da9ff", fg="white", bd=0, height=2).pack(pady=20)

    Button(win, text="Back", font=("Segoe UI", 14, "bold"),
           bg="#3399ff", fg="white", width=12, height=1,
           command=win.destroy).pack(pady=15)


def open_admin_window():
    win = tk.Toplevel(root)
    win.title("Admin Dashboard")
    win.state('zoomed')
    win.configure(bg="#e6f2ff")

    Label(win, text="Admin Dashboard", font=("Segoe UI", 22, "bold"),
          bg="#e6f2ff", fg="#004a7c").pack(pady=20)

    btns = [
        "Manage Users",
        "View Forensic Logs",
        "AI Monitoring Alerts",
        "System Settings",
        "Statistics Dashboard"
    ]

    for text in btns:
        Button(win, text=text, font=("Segoe UI", 14), width=25,
               bg="#4da9ff", fg="white", bd=0, height=2).pack(pady=20)

    Button(win, text="Back", font=("Segoe UI", 14, "bold"),
           bg="#3399ff", fg="white", width=12, height=1,
           command=win.destroy).pack(pady=15)


# ---------------- MAIN TITLE ----------------
Label(root, text="Secure Forensic Data Sharing Framework",
      font=("Segoe UI", 24, "bold"),
      bg="#d6ecff", fg="#003d66").pack(pady=20)

Label(root, text="Select Your Role",
      font=("Segoe UI", 18, "bold"),
      bg="#d6ecff", fg="#005b94").pack(pady=10)


# ---------------- BOX STYLE ----------------
def role_box(parent, title, command):
    box = Frame(parent, bg="white", width=230, height=200,
                highlightbackground="#0074b8", highlightthickness=3)
    box.pack_propagate(False)

    Label(box, text=title, font=("Segoe UI", 16, "bold"),
          bg="white", fg="#004a7c").pack(pady=30)

    Button(box, text="Open", font=("Segoe UI", 13, "bold"),
           bg="#4da9ff", fg="white", bd=0, width=12, height=1,
           activebackground="#1c83e8",
           command=command).pack()

    return box


# ---------------- 3 BOXES IN ONE HORIZONTAL ROW ----------------
row = Frame(root, bg="#d6ecff")
row.pack(pady=40)

sender_box = role_box(row, "Sender", open_sender_window)
sender_box.grid(row=0, column=0, padx=25)

receiver_box = role_box(row, "Receiver", open_receiver_window)
receiver_box.grid(row=0, column=1, padx=25)

admin_box = role_box(row, "Admin", open_admin_window)
admin_box.grid(row=0, column=2, padx=25)


root.mainloop()
