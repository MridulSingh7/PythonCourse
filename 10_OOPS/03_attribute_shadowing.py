class Chai:
    temperature = "hot"
    strength= "Strong"

cutting = Chai()
print(cutting.temperature)
cutting.temperature = "Mild"
print("After changing the temperature:",cutting.temperature)
print("After changing the temperature in cutting, Chai class temperature is:",Chai.temperature)
#hence, changing a value in an object doesnt change its value in the Class 

del cutting.temperature
print(cutting.temperature)
#ab waapas default value aajaega if there is no information about the temprature


#But what if you create an attribute in an object, jo class me nahi tha?
cutting.size = "Small"
print(cutting.size)
del cutting.size 
print(cutting.size)

#as you can see it throws an error, this is what attribute shadowing is
'''
you can give custom values to the attributes in the object, jo already pre defined ho in the class
and if you delete the custom given value like you did here, the attribute pre defined in the class, will be the value of the attribute of that object
this is called attribute shadowing
if not defined the attribute of the object, or deleted it
if the attribute is defined in the class, it will be equal to that value of attribute in class

however if not defined that attribute in class, then it throws error
'''