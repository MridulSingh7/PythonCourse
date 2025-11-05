class Chai: #defining the class
    pass

print(type(Chai))
ginger_tea = Chai() #creating the object based on class
print(type(ginger_tea))
print(ginger_tea is Chai) #ginger tea, the object , is not the class Chai
print(type(ginger_tea) is Chai) #true, type of object and class is same, objects are also the same type as of Class