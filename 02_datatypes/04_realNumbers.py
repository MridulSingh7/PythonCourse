import sys

ideal_temp = 95.5
real_temp = 95.4999999999
#now, python cannot compute that small number differences, to know that you can import sys package
difference = ideal_temp-real_temp #this will have a wrong answer 
print(difference) 
print(sys.float_info)