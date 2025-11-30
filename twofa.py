from utils import generate_otp
from tkinter import simpledialog, messagebox

def offline_otp():
    otp = generate_otp()
    user_input = simpledialog.askstring("OTP Verification", f"Your OTP is:\n{otp}\n\nCopy and paste OTP below:")
    if user_input is None:
        messagebox.showerror("Error", "OTP entry cancelled.")
        return False
    if user_input.strip() == otp:
        messagebox.showinfo("Success", "OTP Verified!")
        return True
    else:
        messagebox.showerror("Error", "OTP Incorrect!")
        return False

def online_otp(email):
    # For temporary testing, same as offline
    return offline_otp()










