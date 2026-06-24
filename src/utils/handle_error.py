# Decorator for handling errors
def handle_error(fn): 
    
    def wrapper(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except Exception as exception:
            print(f"Error: {exception}")

    return wrapper