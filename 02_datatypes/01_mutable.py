#always check mutability by the object id and not by the values
spice_mix = set()
print(f"initial spice mix: {spice_mix}")
print(f"initial spice mix id: {id(spice_mix)}")
spice_mix.add('ginger')
spice_mix.add('cardamom')
print(f"after spice mix: {spice_mix}")
print(f"after spice mix id: {id(spice_mix)}")

#set is mutable, its id doesnt change even after knowing that the values can change



#references (varaible names) are immutable
value = 2
value = 12
#you might think that the value variable is changed from 2 to 12, but actually value is a reference, pehle it pointed to 2, now it points to 12
print(f"id of 2: {id(2)}")
print(f"id of 12:{id(12)}")