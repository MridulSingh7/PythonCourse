def idle_chaiwala():
    pass
print(idle_chaiwala()) #abhi iska return type is none
def idle_chaiwala1():
    return None
print(idle_chaiwala1()) #abhi iska return type is none
def idle_chaiwala2():
    return 120
print(idle_chaiwala2()) #120 is returned and its printed



def chai_status(cups_left):
    if cups_left==0:
        return "Sorry, Chai over"
    return "Wait up, here's your chai"

print(chai_status(4))




#printing multiple return values

def chai_report():
    return 120,20 #sold and remaining

sold,remaining = chai_report()
#destructuring jaise, sold will get the first return value, remaining will get the second return value
print(sold)
print(remaining)