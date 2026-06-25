from types import FunctionType
from functools import wraps

# Decorator for handling errors
def handle_error(fn: FunctionType) -> FunctionType: 
    
    @wraps(fn)
    def wrapper(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except Exception as exception:
            print(f"Error: {exception}")

    return wrapper