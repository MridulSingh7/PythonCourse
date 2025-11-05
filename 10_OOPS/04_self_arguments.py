class Chaicup:
    size = 150 #ml
    #we describe methods like this in the class itself
    def describe(self): #self is the reference to all the attributes in the class 
        return f"size is {self.size}ml" #this is how to use self
    

cup = Chaicup()
print(cup.describe())  
print(Chaicup.describe(cup))#method directly class pe laga diya, with object as argumetn

cup_two = Chaicup()
cup_two.size=100
print(Chaicup.describe(cup_two)) #references to the cup two ka describe in class 