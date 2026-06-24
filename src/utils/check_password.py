from bcrypt import checkpw

# Function for checking password
def check_password(password: str, hashed_password: str) -> bool:
    is_password_correct = checkpw(password=password.encode(), hashed_password=hashed_password.encode())
    return is_password_correct