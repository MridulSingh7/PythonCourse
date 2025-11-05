def serve_chai():
    yield "Cup 1 : Masala Chai"
    yield "Cup 2 : Adrak Chai"
    yield "Cup 3 : Kaali Chai"

chai = serve_chai()
print(next(chai))#pehla yield
print(next(chai))#dusra yield
print(next(chai))#tisra yield   