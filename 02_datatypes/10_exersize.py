'''
Create a dictionary named customer with the following fields:

"name": "John Doe"
"age": 32

"city": "New York"
Print the dictionary.

Add "email" and "phone" to the dictionary.
Print the updated dictionary.

Print the customer's "name" and "city" values.
Check whether the key "email" exists in the dictionary and print the result.

Delete the "age" field from the dictionary.
Print the updated dictionary.

Print all dictionary keys, values, and items.
Remove and print the last inserted key-value pair.

Use .get() to access the key "membership" (which doesn’t exist).
Print the result.

Update the dictionary with a new field "address" set to "221B Baker Street".
Print the final dictionary.'''

customer = dict(name="John Doe", age=32, city="New York")
print(customer)

customer.update(email="johndoe@gmail.com")#adds the email
print(customer)

print(customer["name"])
print(customer["city"])

email = customer.get("email", "NO EMAIL AVAILABLE") #finding a key value pair from dictionary
print(email)

del customer["age"]#deleting a key value pair from dictionary
print(customer)

print(f"all dictionary keys : {customer.keys()}")
print(f"all dictionary values : {customer.values()}")
print(f"all dictionary items : {customer.items()}")

last_item = customer.popitem() #to remove a key value pair
print(last_item)

membership = customer.get("Membership", "Sorry, No membership available for this user")
print(membership)

customer.update(address="221B Baker Street")
print(customer)