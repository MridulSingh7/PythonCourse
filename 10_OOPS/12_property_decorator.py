class TeaLeaf:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age + 2
    
    @age.setter
    def age(self, age):
        if 1 <= age <= 5:
            self._age = age
        else:
            raise ValueError("Tea leaf age must be between 1 and 5 years")
        
leaf = TeaLeaf(2)
print(leaf.age)
leaf.age = 3
print(leaf.age)



'''
The @property decorator allows you to access a method (the getter) as if it were a simple attribute,
eliminating the need for parentheses (leaf.age instead of leaf.age()).

What it enables:
Access Value: It provides the mechanism for reading the attribute's value.
Dynamic Calculation: It allows the retrieved value to be calculated on the fly (e.g., return self._age + 2),
which is essential for hiding the internal representation.'''

'''
The setter method is called automatically when you assign a new value to the property (e.g., when you execute leaf.age=3).
What it enables:
Validation: It allows you to validate or review the value supplied by the user before it is stored internally.
Storage: If the value passes validation, the setter's primary job is to store that value into the private internal attribute (e.g., self._age=3).


The Clarification Point
The setter does not review the value assigned by the getter.
The Getter gives you the calculated value out.
The Setter takes the user's input value in and validates it before storing it.
They are two separate operations on the same managed attribute.
'''