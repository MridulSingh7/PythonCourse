def infinite_generate():
    count=1
    while True: #infinite yield
        yield f"Refill number: #{count}"
        count+=1

refill = infinite_generate()

for _ in range(10):
    print(next(refill))

    #this is how to write and use infinite generator


