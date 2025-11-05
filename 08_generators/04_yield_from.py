def menu1():
    yield "Masala Tea"
    yield "Pepper Tea"

def menu2():
    yield "Oolong Tea"
    yield "Matcha Tea"

def full_menu():
    yield from menu1() # alag alag generator functions ke yield ko combine kar sakte ho ek naye generator function me using this
    yield from menu2()

for chai in full_menu():
    print(chai)
#to close a generator function, use method .close(), also beneficiary for memory cleanup