#using the zip to iterate throguh two loops parallely in a for loop
names = ["Hitesh", "Meera", "Ali", "Sam"]
price = [100,122,130,170]

for name, amount in zip(names,price):
    print(f"The order is for {name}, the price is : {amount}")

#aise use case  for iterator1,iterator2 in zip(list1,list2)