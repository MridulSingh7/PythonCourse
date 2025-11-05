##############numbers###################
black_tea_grams = 14
ginger_grams = 3

total_grams = black_tea_grams + ginger_grams
print(f"total grams : {total_grams}")

remaining_grams = black_tea_grams - ginger_grams
print(f"remaining grams : {remaining_grams}")


#normal division
milk_litres = 7
people = 3
milk_per_serving = milk_litres/people
print(f"milk per person:{milk_per_serving}")

#for remainder
milk_remaining = milk_litres%people
print(f"milk per person:{milk_remaining}")

#for just the whole number, not fractional part
equal_distribution = milk_litres//people
#this will have only the whole number, 4//3 = 1 , 4/3 = 1.33


#powers
base=2
scale=5
final_value = base**scale #2 to the power 5


#YOU CAN ALSO WRITE 
val = 100000000
val = 1_000_000_000 #the underscores are ignored

#swapping numbers
a=1
b=2
a,b=b,a 
print(a,b)