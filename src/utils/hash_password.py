from bcrypt import gensalt, hashpw

# Function for hashing password
def hash_password(password: str) -> str: 
    
    salt = gensalt()
    hashed_password = hashpw(password=password.encode(), salt=salt)

    return hashed_password.decode("utf-8")