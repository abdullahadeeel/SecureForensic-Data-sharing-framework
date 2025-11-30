import sqlite3
import re
from tkinter import *
from tkinter import messagebox, simpledialog
from db import DB_PATH
from utils import hash_password, generate_otp
import main_interface

# Email validation function
def is_valid_email(email):
    return re.match(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$", email)

def signin_page():
    root = Tk()
    root.title("SIGN IN")
    root.state("zoomed")
    root.configure(bg="#87CEEB")  # Sky Blue background

    # Center frame (login card)
    card = Frame(root, bg="white", bd=2, relief="groove")
    card.place(relx=0.5, rely=0.5, anchor=CENTER, width=700, height=550)  # Height increased

    # Title
    title = Label(card, text="SIGN IN", bg="white", font=("Arial", 34, "bold"))
    title.pack(pady=(30, 40))

    email_var = StringVar()
    pass_var = StringVar()

    # Email label and entry
    Label(card, text="Email", bg="white", font=("Arial", 16)).pack(anchor="w", padx=50)
    email_entry_frame = Frame(card, bg="#FFFFFF", bd=2, relief="groove")
    email_entry_frame.pack(pady=(5, 25), padx=50, fill="x")
    email_entry = Entry(email_entry_frame, textvariable=email_var, font=("Arial", 14), bd=0)
    email_entry.pack(fill="x", padx=5, pady=5)

    # Password label and entry
    Label(card, text="Password", bg="white", font=("Arial", 16)).pack(anchor="w", padx=50)
    pass_entry_frame = Frame(card, bg="#FFFFFF", bd=2, relief="groove")
    pass_entry_frame.pack(pady=(5, 40), padx=50, fill="x")
    pass_entry = Entry(pass_entry_frame, textvariable=pass_var, font=("Arial", 14), bd=0, show="*")
    pass_entry.pack(fill="x", padx=5, pady=5)

    # Error message
    error_msg = Label(card, text="", fg="red", bg="white", font=("Arial", 14))
    error_msg.pack(pady=(0, 20))

    # Real-time email validation on focus out
    def validate_email(event=None):
        email = email_var.get().strip()
        if email and not is_valid_email(email):
            error_msg.config(text="Invalid email format. Example: user123@example.com")
            return False
        else:
            error_msg.config(text="")
            return True

    email_entry.bind("<FocusOut>", validate_email)

    # Submit function
    def submit():
        email = email_var.get().strip()
        pwd = pass_var.get().strip()

        if not email or not pwd:
            error_msg.config(text="All fields are required.")
            return

        # Check if email format is valid
        if not validate_email():
            return  # Red flag already shown

        # DB check for email + password combination
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE email=? AND password=?", (email, hash_password(pwd)))
        user = c.fetchone()
        conn.close()

        if user:
            otp = generate_otp()
            otp_input = simpledialog.askstring("OTP Verification", f"Your OTP is:\n{otp}\n\nEnter OTP:")
            if otp_input is None:
                messagebox.showerror("Error", "OTP entry cancelled.")
                return
            if otp_input.strip() == otp:
                messagebox.showinfo("Success", f"Login Successful! Welcome {user[1]}")
                root.destroy()
                main_interface.main_menu(user)
            else:
                messagebox.showerror("Error", "OTP Incorrect! Login Failed.")
        else:
            error_msg.config(text="Invalid email or password!")  # Red flag for invalid combination

    # Sign in button
    submit_btn = Button(card, text="SIGN IN", width=25, font=("Arial", 16, "bold"),
                        bg="#87CEEB", fg="white", command=submit)
    submit_btn.pack(pady=(0, 30))

    root.mainloop()

if __name__ == "__main__":
    signin_page()



























