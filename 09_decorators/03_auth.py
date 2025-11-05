from functools import wraps

def require_admin(func):
    @wraps(func)
    def wrapper(user_role):
        if user_role != "admin":
            print("Access denied🚫!Admins only")
        else :
            print("Welcome Back😊")
            return func(user_role)
    return wrapper

@require_admin
def access_tea_inventory(user_role):
    print(f"Access granted to the {user_role}")

access_tea_inventory("admin")
print("\n\n\n\n\n")
access_tea_inventory("user")