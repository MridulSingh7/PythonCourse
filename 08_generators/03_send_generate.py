def chai_customer():
    print("Welcome! What chai would you like?")
    order = yield
    while True:
        print(f"Order: {order} is being prepared")
        order = yield

stall = chai_customer()
next(stall)
stall.send("Masala Tea")
stall.send("Ginger tea")
'''
kya horha hai?line 2 tak to normal hai
line 3, order= yield, yield me jab value send karenge humlog from line 10 (stall.send("value"))
to ye jake order variable me store hojaega
and then infinite loop me jake print hoga
again line 6 me order = yield, agar dusri bar send karenge, like we do in line 11, to same process, order me yield me jo value bheje hai wo store hojagea
and then again the true loop will run and print hojaege, then before the while loop runs again, you need to send to yield using the .send() function
'''