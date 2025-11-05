class Chai:
    def __init__(self,type_,strength):
        self.type = type_
        self.strength= strength


#code duplication way to acccessing the base class
class GingerChai(Chai):
    def __init__(self, type_, strength, spice_level):
        self.type = type_
        self.strength = strength
        self.spice_level = spice_level


#another way to do that : Explicit call
#Chai wale ka init constructor run kara diye blackchai wale init ke andar, and jo bacha spice_level wo khudse kardiye 
class BlackChai(Chai):
    def __init__(self, type_, strength, spice_level):
        Chai.__init__(self,spice_level)
        self.spice_level = spice_level
         
#using super().__init
class LemonChai(Chai):
    def __init__(self, type_, strength,spice_level):
        super().__init__(type_, strength)
        #the above code means, base class wala constructor ko use karo aur uska wala initialisation kardo, same as the explicit call , but here we dont class
        self.spice_level = spice_level
        #however extra attributes khudse hi dalne padege


#in all, the base class is the class which is passed on as argument in the Class