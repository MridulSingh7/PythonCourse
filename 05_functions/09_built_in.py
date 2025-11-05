#dunder functions __name__ , call it dundername function , ex __doc__ dunderdoc

#learn about them by finding out in the docs in built in functions of python
#jaise jaise jo chiz ka use aaye uss hisaab se dhundho built in function


#common practise : function define karne time pehla line function kya karta hai wo likho
def generate_bill(chai=0,samosa=0):
    '''
    calculate total bill for chai and samosa, initially chai and samosa are zero.
    param1:chai, param2:samosa 
    the return value is total bill amount 
    to view docs about the function : print(generate_bill.__doc__)
    '''
    total = chai*10 + samosa*8
    return total 

print("Total amount :",generate_bill(2,4))
print(generate_bill.__doc__)