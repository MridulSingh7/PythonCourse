# This function will be tested automatically.
# Do not change the function name or parameters.
 
loyalty_points = 0  # global variable
 
def process_transactions(transactions: list[int]) -> int:
    # Write your code below this line
    def apply_bonus():
        nonlocal total #nonlocal total means just is scope ke bahar wale scope ke liye
        if total > 1000:
            total += 50  # bonus for high spenders
 
    total = 0
 
    for amount in transactions:
        total += amount
 
    apply_bonus()
 
    # update global loyalty_points
    global loyalty_points #accessing the global varaible from inside the box, using global+variable name,
    loyalty_points += total // 100  # earn 1 point per ₹100
 
    return total



'''
In Python, a global keyword allows a function to modify a variable defined in the global scope (outside any function),
while the nonlocal keyword allows a nested function to modify a variable defined in an enclosing (but not global) scope.
The main difference is the location of the variable being targeted: global refers to the outermost scope, 
whereas nonlocal refers to an intermediate scope between the nested function and the global scope.
'''