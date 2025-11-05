tier = input("Enter your seat type :\n1.Sleeper\n2.General\n3.AC\n :-").lower()

match tier :
    case "sleeper":
        print("Cost for Sleeper is : 500")
    case "general":
        print("Cost for General is : 340")
    case "ac":
        print("Cost for AC is : 880")
    case _:
        print("Unknown seat type")

#switch case aise use karte hain