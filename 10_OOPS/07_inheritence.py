class BaseChai:
    def __init__(self, type_):
        # FIX 1: The attribute is called 'type'
        self.type = type_

    def prepare(self):
        # FIX 1: Correctly use self.type
        print(f"Preparing {self.type} chai...")

class MasalaChai(BaseChai):
    # FIX 2: Call the parent's constructor to initialize self.type
    def __init__(self, type_):
        super().__init__(type_) 

    def add_spices(self):
        print("Adding cardamom, ginger, cloves...")


# Another way to achieve polymorphism/composition
class ChaiShop:
    # Class attribute referencing the BaseChai class
    chai_cls = BaseChai #when we dont want to inherit but need a reference to the class
    
    def __init__(self):
        # Instantiate the class referenced by chai_cls. 
        # For ChaiShop, this runs: self.chai = BaseChai("Regular")
        self.chai = self.chai_cls("Regular")

    def serve(self):
        # FIX 3: Get the type from the instantiated object self.chai
        print(f"Serving {self.chai.type} chai in the shop") 
        self.chai.prepare()

class FancyChaiShop(ChaiShop):
    # Override the class attribute to use MasalaChai instead of BaseChai
    chai_cls = MasalaChai
    # The __init__ of ChaiShop runs, effectively doing: self.chai = MasalaChai("Regular")


shop = ChaiShop()
fancy = FancyChaiShop()

print("--- Regular Shop ---")
shop.serve()

print("\n--- Fancy Shop ---")
fancy.serve()
# Since fancy.chai is an instance of MasalaChai, we can call its unique method.
# We access the *instance* to call the method.
# Note: The original call used fancy.chai_cls.add_spices() which works 
# because add_spices does not require instance data, but calling it on the 
# instantiated object is typically cleaner/safer. Let's stick to the instance:
fancy.chai.add_spices()




'''
classical inheritance vs compositional inheritance
classical inheritance me the class is passed as an argument to the new class

compositional inheritance me we keep reference to the older class and use it as we need it
more flexible, highly reusable, more like pointers rakhe hain'''









'''
trategy Execution (self.chai_cls(...))

self.chai_cls: This is a variable that holds a reference to a class, not an instance.

For ChaiShop, this reference points to the BaseChai class.

For FancyChaiShop, this reference points to the MasalaChai class (due to overriding).

The Execution: By placing parentheses (...) after the class reference, the code is commanding Python to call the class's constructor (__init__). The arguments (e.g., "Regular") are passed to that constructor.

Result: Python creates a new, independent object instance (either a BaseChai or a MasalaChai object).

2. Composition (The "Has-A" Relationship)

self.chai = ...: The newly created object instance (the BaseChai or MasalaChai object) is assigned to an instance attribute named self.chai on the shop object.

The Meaning: This establishes the "has-a" relationship: "The ChaiShop has a chai object." The shop is now composed of (built using) this inner chai object.

3. Strategy Implementation (Flexibility)

The Benefit: Because the shop's logic doesn't say self.chai = BaseChai("Regular"), but instead uses the dynamic attribute self.chai_cls, the type of object created is flexible.

How it Works: A subclass (FancyChaiShop) can change its strategy simply by overriding the chai_cls class attribute. The base class's __init__ method (which is inherited) automatically executes the new strategy when the subclass is instantiated, creating a MasalaChai object instead of a BaseChai object, all without needing to rewrite the shop's core logic.

In short, this line is where the ChaiShop decides what kind of chai it will work with and stores that decision as an internal component. The rest of the shop's methods (like serve) simply delegate tasks to this component (e.g., self.chai.prepare()).'''