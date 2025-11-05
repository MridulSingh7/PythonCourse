chai = "ginger chai"

def prepare_chai(order):
    print("preparing", order)

prepare_chai(chai)


def make_chai(tea,milk,sugar):
    print(tea,milk,sugar)

make_chai("darjeeling", "yes", "yes")#positional args dalna, when you know konsa position pe konsa parameter hai uske hisab se args bhej rahe ho,
#but aisa b ho sakta hai you dont know ki konse position pe konsa arg hai, ex tea ke jagah sugar ka arg daldiye etc
make_chai(tea="darjeeling", sugar="medium",milk="yes")
#this is called keyword mapped args


def special_chai(*ingredients,**extras):
    print("Ingridients:", ingredients)
    print("Extras:", extras)

special_chai("Cardamon","Cinammon", sweetner="Honey", foam="Yes")
#anything without a key (cardamon and cinammon) will automatically be treated as
#the parameter with * single , ingredients tuple me save hojaega
#arguments with keywords are mapped to ** wala parameter


#to make sure that you set the default value to be none follow this
def chai_order(order=None):
    if order is None:
        order=[]

chai_order() #ab jabtak () me koi arg nahi pass karoge tabtak iska default value [] empty set hoga
#instead of doing def chai_order(order=[]) do this , more secure and ensures ki hamesha default zero set ho  