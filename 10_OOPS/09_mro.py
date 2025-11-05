class A:
    label = "A: BASE CLASS"

class B:
    label = "B: MASALA BLEND"

class C(A):
    label = "C: HERBAL BLEND"

class D(B,C):
    pass

cup = D()
print(cup.label)