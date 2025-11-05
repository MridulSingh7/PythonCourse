#are immutable, you cannot change values of strings, they create a new reference everytime you update a string
chai_name="ginger tea"
customer_name="Priya"

print(f"order for {customer_name} : {chai_name}")

#2.concept of indexing
chai_description = "aromatic and soothing"
first_word = chai_description[0:8]
#always, isme 0 to 7 hona chahie tha but 1 up karna pdta hia because last index in [x:y] is not inclusive
#example, agar 0 se 8th index tak ka chahie to 0:9 karna pdega
#now python me reverse indexing bhi hoti hai, 0,1,2,3,4 === -1,-2,-3,-4,-5 from back, hence you can also reverse the string
word_reversed = chai_description[::-1]
print(word_reversed)




#we often do encoding in case of special characters in strings 
label_text = "Chai Spècial"
encoded_text = label_text.encode("utf-8") #encoding the string
print(f"normal text : {label_text}")
print(f"encoded text : {encoded_text}")
#you can decode it
decoded_text = encoded_text.decode("utf-8")
print(f"decoded text : {decoded_text}")