daily_sales = [5, 10, 12, 7, 3, 8, 9, 15]

total_cups = (sale for sale in daily_sales if sale > 5)

print(total_cups)


#generator comprehensions are memory efficient and uses (), same as any other comprehension
#you need to add methods to it to do the work ex sum(generator comprehension) will give the sum of all elements passing the condition



daily_sales = [5, 10, 12, 7, 3, 8, 9, 15]

total_cups = sum(sale for sale in daily_sales if sale > 5)

print(total_cups)