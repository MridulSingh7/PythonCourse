device_status = input("Is your thermostat on: ").lower()
if device_status == "yes" :
    temperature = input("what is the temperature: ")
    temp = int(temperature)
    if temp>35:
        print("WARNING!!! High Temperature")
    else :
        print(f"The temperature is normal : {temp}C")
else :
    print("The device is OFF, run the code again and type YES to activate the thermostat")