from functools import wraps
def my_decorator(func):#defining the name of wrapper
    @wraps(func) #make sure the use this, so that your function name isnt changed
    def wrapper(): #creating the wrapper
        print("Before function runs") 
        func() #calling the function jisko wrap karna hai
        print("After function runs")
    return wrapper #return the wrapper not the function

@my_decorator #@wrapperFunction - iske next line me jo function ayega wo wrapper me chala jaega
def greet(): 
    print("Hello from decorators class from chaicode")
#function greet is wrapped inside the my_decorator wrapper because its defined just after @my_decorator.

greet()
print(greet.__name__)#normally greet.__name__ wrapper dikhaega, but since we used functools ka wraps, we use wraps to make sure the name is written correctly





def my_decorator2(func):
    @wraps(func)
    def wrapper():
        print("First line of the wrapper")
        func()
        print("second line of the wrapper")
    return wrapper

@my_decorator2
def greetAgain():
    print("This function GreetAgain is defined below the @mydecorator part")

greetAgain()
print(greetAgain.__name__)