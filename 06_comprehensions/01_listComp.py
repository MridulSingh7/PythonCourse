# [expression for item in iterable_list if condition]
menu = [
    "masala chai",
    "Iced masala chai",
    "Iced ginger tea",
    "normal tea",
    "Regular tea",
    "Iced peach tea"
]

iced_tea = [items for items in menu if "Iced" in items]
#new list = [expression for item in iterable if condition]
#expression = jisko naya value milega, here expression must be same as item because item hi naya value milne wala hai
#for item in menu (a list) , if "Iced" present in the elements of menu add it in
print(iced_tea)
