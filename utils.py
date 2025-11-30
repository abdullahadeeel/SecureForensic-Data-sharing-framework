import hashlib
import random

# Hash password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Generate OTP
def generate_otp(length=6):
    return str(random.randint(10**(length-1), 10**length-1))





