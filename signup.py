import sqlite3
import re
from tkinter import *
from tkinter import simpledialog, messagebox
from db import create_db, DB_PATH
from utils import hash_password, generate_otp

create_db()

def is_valid_name(name):
    return name.replace(" ", "").isalpha()

def is_valid_email(email):
    # Email must have at least one digit
    if not re.match(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$", email):
        return False
    return bool(re.search(r"[0-9]", email))

def is_strong_password(pwd):
    return (
        len(pwd) >= 8 and
        re.search(r"[A-Z]", pwd) and
        re.search(r"[a-z]", pwd) and
        re.search(r"[0-9]", pwd) and
        re.search(r"[!@#$%^&*()_+=\-{};:<>?/|~]", pwd)
    )

def is_valid_role(role):
    return role.lower() in ["sender", "receiver", "admin"]

def register_user(name, email, password, role):
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute(
            "INSERT INTO users (name, email, password, role, created_at) VALUES (?, ?, ?, ?, datetime('now'))",
            (name, email, hash_password(password), role.lower())
        )
        conn.commit()
        conn.close()
        print("DB Insert Success!")
        return True
    except sqlite3.IntegrityError:
        print("DB Insert Failed: Email already exists!")
        return False
    except Exception as e:
        print("DB Insert Failed:", e)
        return False

def signup_page():
    root = Tk()
    root.title("SIGN UP")
    root.state("zoomed")
    root.configure(bg="#E3F2FD")

    # Title
    title = Label(root, text="SIGN UP", bg="#E3F2FD", font=("Arial", 32, "bold"))
    title.pack(pady=40)

    # Card frame for form
    card_frame = Frame(root, bg="white", width=800, height=600)
    card_frame.pack(pady=20)
    card_frame.pack_propagate(False)

    labels = ["Full Name", "Email Address", "Password", "Role (sender / receiver / admin)"]
    name_var = StringVar()
    email_var = StringVar()
    pass_var = StringVar()
    role_var = StringVar()

    entries = []
    for i, txt in enumerate(labels):
        Label(card_frame, text=txt, font=("Arial", 16), bg="white").pack(anchor="w", padx=80, pady=(15 if i==0 else 5, 5))
        frame = Frame(card_frame, bg="#FFFFFF", bd=2, relief="groove")
        frame.pack(padx=80, pady=(0, 15), fill="x")
        var = [name_var, email_var, pass_var, role_var][i]
        show = "*" if "Password" in txt else ""
        entry = Entry(frame, textvariable=var, font=("Arial", 14), bd=0, show=show)
        entry.pack(fill="x", padx=5, pady=5)
        entries.append(entry)

    error_msg = Label(card_frame, text="", fg="red", bg="white", font=("Arial", 14))
    error_msg.pack(pady=(0, 20))

    # FOCUS OUT VALIDATION
    def validate_name(event):
        if name_var.get().strip() and not is_valid_name(name_var.get().strip()):
            error_msg.config(text="Only letters (A-Z, a-z) are allowed in name.")
        else:
            error_msg.config(text="")

    def validate_email(event):
        if email_var.get().strip() and not is_valid_email(email_var.get().strip()):
            error_msg.config(text="Invalid email format or missing digit.")
        else:
            error_msg.config(text="")

    def validate_password(event):
        if pass_var.get() and not is_strong_password(pass_var.get()):
            error_msg.config(text="Weak password: requires A-Z, a-z, 0-9, symbol, 8+ chars")
        else:
            error_msg.config(text="")

    def validate_role(event):
        if role_var.get().strip() and not is_valid_role(role_var.get().strip()):
            error_msg.config(text="Role must be sender, receiver, or admin.")
        else:
            error_msg.config(text="")

    name_var.trace_add("write", lambda *args: validate_name(None))
    email_var.trace_add("write", lambda *args: validate_email(None))
    pass_var.trace_add("write", lambda *args: validate_password(None))
    role_var.trace_add("write", lambda *args: validate_role(None))

    # Submit function
    def submit():
        name = name_var.get().strip()
        email = email_var.get().strip()
        pwd = pass_var.get().strip()
        role = role_var.get().strip().lower()

        if not all([name, email, pwd, role]):
            error_msg.config(text="All fields are required.")
            return
        if not is_valid_name(name):
            error_msg.config(text="Only letters (A-Z, a-z) are allowed in name.")
            return
        if not is_valid_email(email):
            error_msg.config(text="Invalid email format or missing digit.")
            return
        if not is_strong_password(pwd):
            error_msg.config(text="Weak password: requires A-Z, a-z, 0-9, symbol, 8+ chars")
            return
        if not is_valid_role(role):
            error_msg.config(text="Role must be sender, receiver, or admin.")
            return

        # Check existing email
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE email=?", (email,))
        existing = c.fetchone()
        conn.close()
        if existing:
            messagebox.showerror("Error", "Email already exists! Signup Failed.")
            return

        # OTP verification
        otp = generate_otp()
        otp_input = simpledialog.askstring("OTP Verification", f"Your OTP is:\n{otp}\n\nCopy and paste OTP below:")

        if otp_input is None:
            messagebox.showerror("Error", "OTP entry cancelled.")
            return

        if otp_input.strip() == otp:
            success = register_user(name, email, pwd, role)
            if success:
                messagebox.showinfo("Success", "Signup Successful! You can now Signin.")
                root.destroy()
            else:
                messagebox.showerror("Error", "Signup Failed! Please try again.")
        else:
            messagebox.showerror("Error", "OTP Incorrect! Signup Failed.")

    submit_btn = Button(card_frame, text="CREATE ACCOUNT", width=25, font=("Arial", 16, "bold"), bg="#87CEEB", fg="white", command=submit)
    submit_btn.pack(pady=25)

    root.mainloop()

if __name__ == "__main__":
    signup_page()

























