orders = ["Hitesh", "Aman", "Becky", "Carlos"]

for name in orders :
    print(f"Order ready for Mr.{name}")

#when needed numbered order, pehle naya list me convert karo enumerate karke then
menu = ["Green", "lemon", "Spice", "Mint"]

for idx, item in enumerate(menu,start=1): #enumerate aise use karo for for loops, isme numbered list kardega, use start=1 if needed from 1 to n
    print(f"{idx}:{item}")