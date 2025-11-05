'''Create an infinite generator function called token_dispenser(start=1).

On each call to next(), it should yield the current token number and increment it.

If a value is passed to the generator using send(), the generator should reset the token number to that new value.

The generator should handle the .close() method gracefully and print "Dispenser closed." when it is closed.
'''

def token_dispenser(start=1):
    token = start #initialised token as 1
    try:
        while True: #infinite generator
            reset_value = yield token #agar yield kiye token to 
            if reset_value is not None:
                token = reset_value #agar kuch send kiye ho to token ka reset value hojaega
            else:
                token += 1 #if no input then token keeps on increasing
            print(f"Order number:{token}")
    except GeneratorExit:
        print("Dispenser closed.")


'''

reset_value = yield token	

This is the core of the generator:
1. yield token: Pauses the function, returns the current value of token to the caller, and saves its internal state.
2. reset_value = ...: When the generator is resumed (either by next() or send()), the function receives a value. 
If resumed by next(), this value is None.
 If resumed by send(value), this value is the one sent, and it's assigned to reset_value.
 '''