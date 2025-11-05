#mathematics wala set, venn diagram wala
essential_spices = {"cardamon", "ginger", "cinammon"}
optional_spices = {"cloves", "ginger", "black pepper"}

all_spices = essential_spices | optional_spices #logically this is UNION (|) operator for sets
print(all_spices)
common_spices = essential_spices & optional_spices #logically this is INTERSECTION (&)
print(common_spices)
only_in_essential_spices = essential_spices - optional_spices #logically strictly A i.e A-B 
print(only_in_essential_spices)

print(f"is clove in essential spices ? : {"clove" in essential_spices}") #to check if any element is in the list
print(f"is black pepper in optional spices ? : {"clove" in optional_spices}")

#there is also a datatype called frozenset 
