#pure function are normal
def pure_func():
    return "HEY"

#impure functions involve global variables
counter = 0
def impure_func():
    global counter
    counter = counter+1
    return counter
#global variable counter change kardiya

def factorial(n):
    if n==1 or n==0:#base case for recursive functions
        return 1
    return n*factorial(n-1)
#recursive function




#lambda functions, one liner, often passed as arguments to use in another function
def square_list(nums):
    return list(map(lambda x: x**2, nums))
