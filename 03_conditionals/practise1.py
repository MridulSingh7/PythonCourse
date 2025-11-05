'''
Delivery Charge Calculator
Youre building a delivery system for an e-commerce platform. Depending on the distance of the customers address, different delivery charges apply.

Tasks:

Take input from the user for delivery distance in Kilometers and store it in a variable named distance.

If the distance is 2 km or less, return the string: "Delivery charge: 0"

If the distance is greater than 2 km but not more than 5 km, return the string: "Delivery charge: 30"

If the distance is greater than 5 km but not more than 10 km, return the string: "Delivery charge: 50"

If the distance is more than 10 km, return the string: "Delivery not available for your location."
'''

distance = input("enter the distance of your home from us: ")
x = int(distance)
if x <= 2:
    print("YAY! Free delivery for you")
elif x>2 and x<5:
    print("Delivery charge: 30")
else :
    print("Delivery not available on your location")
