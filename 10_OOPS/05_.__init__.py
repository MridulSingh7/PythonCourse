class ChaiOrder:
    def __init__(self,type_,size):
        self.type=type_
        self.size=size  

    def sumary(self):
        return f"{self.size}ml of {self.type} chai"

order = ChaiOrder("Masala",200)#these masala and 200 are called instances of class, i mean properties of class
print(order.sumary())