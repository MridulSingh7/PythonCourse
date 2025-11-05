cup_size = input("choose your cup size : ").lower()
if cup_size == "s":
    print("price for that is 10Rupees")
elif cup_size == 'm':
    print("price for that is 15Rupees")
elif cup_size == 'l':
    print("price for that is 20Rupees")
elif cup_size == 'xl':
    print("price for that is 25Rupees")
else :
    print("Unknown cup size")