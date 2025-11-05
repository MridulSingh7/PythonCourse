#we use ternary operators in this one
order_amount = int(input("Enter your order amount : "))
delivery_fee = 0 if order_amount>300 else 30
#if and else inside assigning a value is ternry
print(delivery_fee)