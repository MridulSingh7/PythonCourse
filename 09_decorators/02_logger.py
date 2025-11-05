from functools import wraps

def log_activity(func):
    @wraps(func)
    def wrapper(*args, **kwargs): #we can also pass arguments to the wrapper
        print(f"Calling function :{func.__name__} ")
        result = func(*args,**kwargs)
        print(f"Executed function : {func.__name__}")
        return result
    return wrapper

@log_activity
def logger_function(type):
    print(f"Brewing chai:{type}")

logger_function("Masala Chai")