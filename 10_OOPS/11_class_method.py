#static methods cannot initialise but classmethods can
#basically classmethod takes cls class as the argument, and used as alternative constructors
class ChaiOrder:
    def __init__(self, tea_type, sweetness, size):
        self.tea_type = tea_type
        self.sweetness = sweetness
        self.size = size

    # Added __repr__ for readable output
    def __repr__(self):
        return f"ChaiOrder(Type='{self.tea_type}', Sweetness='{self.sweetness}', Size='{self.size}')"

    @classmethod
    def from_dict(cls, order_data):
        return cls(
            order_data["tea_type"], 
            order_data["sweetness"],
            order_data["size"]
        )
    
    @classmethod
    def from_string(cls, order_string):
        tea_type, sweetness, size = order_string.split("-")
        return cls(tea_type, sweetness, size)


class ChaiUtils:
    @staticmethod
    def is_valid_size(size):
        return size in ["Small", "Medium","Large"] 


order1 = ChaiOrder.from_dict({"tea_type": "Masala", "sweetness": "Medium", "size": "Large"})
order2 = ChaiOrder.from_string("Ginger-Low-Medium")
order3 = ChaiOrder("lemon", "Low", "small")

print(order1)
print(order2)
print(order3)



'''
. Use Case of Class Method
The primary use case for a class method (@classmethod) is to provide alternative constructors for a class.

Use Case	Explanation/Code Reference
Alternative Constructors- When data to create an object comes from various sources (e.g., a dictionary, a string, a file).
Instead of cluttering the main __init__ method with complex parsing logic,
class methods handle the input conversion and then use the class reference (cls) to instantiate the object.

Example (from Code)	The method ChaiOrder.from_dict() is an alternative constructor.
It takes a dictionary, extracts the required values, and uses return cls(...) to correctly create a new ChaiOrder instance.





2.Difference Between Class Method and Static Method
The key difference lies in the first argument they receive and their binding to the class or instance.
Feature	Class Method (@classmethod)	Static Method (@staticmethod)
First Argument- Receives the class itself as the first argument, conventionally named cls.	Receives no specific first argument (like cls or self).
Binding/Scope- Bound to the class and can access/modify class state (via cls).	Not bound to the class or instance; acts like a regular function placed within the class namespace.
Initialization- Can create a new instance of the class using cls(...).	Cannot create a new instance as it has no reference to the class or instance.
Use Case-  factory/Alternative Constructors.	Utility functions that logically belong to the class but don't need class or instance data.
Code Reference-   ChaiOrder.from_dict(cls, order_data) uses cls.	ChaiUtils.is_valid_size(size) only uses the provided size.



3. What Does a Class Method Do Exactly?
A class method does two things exactly:
It is implicitly passed the class object itself (cls) when called.
It uses the received cls reference, typically to call the class's constructor, thereby creating and returning a new instance of that class.
Code Example:
In ChaiOrder.from_string(cls, order_string):
The method receives the ChaiOrder class object as cls.
It parses the input string: tea_type, sweetness, size = order_string.split("-").
It then executes return cls(tea_type, sweetness, size). Since cls refers to ChaiOrder, this is equivalent to calling ChaiOrder.__init__(tea_type, sweetness, size),
effectively initializing and returning a new ChaiOrder object.




4. When to Use Class Method vs. Static Method
Use Class Methods When:
You need to perform an operation that returns a class instance, or when you need to access or modify a class-level attribute.
Rule: Use when you need to call the constructor: return cls(...).
Code Reference: ChaiOrder.from_dict is necessary because its purpose is to create (initialize) a new ChaiOrder object from external data.


Use Static Methods When:
The function is a purely utility or helper function that has a strong logical connection to the class but does not need to access the class state (cls) or the instance state (self).
Rule: Use when the method can be defined outside the class but is logically grouped inside it. It neither creates an instance nor uses cls.
Code Reference: ChaiUtils.is_valid_size(size) is a static method because it only checks the input size against a fixed list;
it doesn't need to know anything about the ChaiUtils class or a specific ChaiOrder instance to perform its check.'''