class InvalidChaiError(Exception): #created a custom error handling class which inherits the Exception class which is for error handling
    pass #we do this so that we get to know konsa error aaya hai, easy to debug



'''
a function bill
has a menu jisme masala hai aur ginger hai with price 20 and 40 each
it takes arguments of flavor and cups, total = flavor[cost]*number of cups

under the try block
agar flavor menu me nahi hai then raise the invalidchaierror ki chai not available
agar cups ka quantity integetr me nahi hai to raise typeError 

then calculate the total cost = menu[flavor]*cups menu[flavor]=price of the item, key-value pair
print the total 


if anything goes wrong, we now go into except block: and we print the error
except Exception as e means we have e instead of Exception

and use finally to end the function by gratitude
this is the bill function
'''

#we pass on bill("masala",4)=> masala tea , 4 cups = 20*4 = 80 rupees




def bill(flavor,cups):
    menu = {"masala":20, "ginger":40} 
    try:
        if flavor not in menu: 
            raise InvalidChaiError("That chai is not available")
        if not isinstance(cups, int):
            raise TypeError("Number of cups must be an integer")
        total = menu[flavor]*cups
        print(f"Your bill for {cups} cups of {flavor} chai: rupees {total}")
    except Exception as e:
        print("Error:",e)
    finally:
        print("Thank you for visiting chaicode")



bill("mint",2)
