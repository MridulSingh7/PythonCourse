#lists are mutable, you can change the same list
ingredients = ["water", "tea leaves", "milk"]
print(ingredients)
ingredients.append("sugar") #insert at back
ingredients.insert(2,"spices") #insert at the given index
print(ingredients)
spices = ["cardamon", "elaichi", "ginger"]
ingredients.extend(spices) #ingridients wale list me spices ke sare elements add kardegi last me
print(ingredients)

last_added = ingredients.pop()
print(last_added)
ingredients.reverse(); #will reverse the list
print(ingredients)
ingredients.sort()
print(ingredients)

sugar_levels = [1,2,3,4,5]
print(f"max sugar level is : {max(sugar_levels)}") #finding maximum element in the list




#operator overloading 
base_liqiud = ["milk", "water"]
extra_flavour = ["ginger"]
full_liquid_mix = base_liqiud + extra_flavour #operator overloading, using + to append
strong_brew = ["Black tea"]*3 #operator overloading, using * to multiply and store the elment in the strong_brew thrice
print(strong_brew) # the elements are repeated thrice 




#exersize
'''
Create a grocery list named my_cart with the items: "apples", "bananas", and "milk"
Print the grocery list.

Add "bread" to the end of the list.
Print the updated grocery list.

Insert "ketchup" at the beginning of the list.
Print the updated grocery list.

Remove "bananas" from the list.
Print the updated grocery list.

Remove the last item from the list and store it in a variable named removed_item.
Print the value of removed_item.

Extend the grocery list by adding "rice" and "butter".
Print the updated grocery list.

Sort the grocery list in alphabetical order.
Print the updated grocery list.

Reverse the order of the grocery list.
Print the updated grocery list.

Concatenate the grocery list with another list containing "juice" and "jam".
Print the resulting list.

Duplicate the grocery list twice.
Print the resulting list.

Define a string with the value "tomato cucumber spinach" and convert it into a list.
Print the converted list.
'''

my_cart = ["apples", "bananas", "milk"]
print(my_cart)
my_cart.append("bread")
my_cart.insert(0,"ketchup")
print(my_cart)
my_cart.remove("bananas")
print(my_cart)

removed_item = my_cart.pop()
print(removed_item)

my_cart.extend(["rice", "butter"])
my_cart.sort()
print(my_cart)
my_cart.reverse()
print(my_cart)
my_cart = my_cart + ["jam", "juice"]
my_cart = my_cart*3

stringVal = "tomato cucumber spinach"
word_list = stringVal.split()
print(word_list)

