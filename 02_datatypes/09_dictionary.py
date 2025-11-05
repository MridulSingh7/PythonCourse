#a dictionary is a key value pair , key = value
chai_order = dict(type="masala chai", sugar=2, size="large")

#you can also create an empty dictionary and then add accordingly
chai_recipie = {}
chai_recipie["base"] = "milk"
chai_recipie["spice"] = ["ginger", "cardamon"]
chai_recipie["sugar"] = 2
print(chai_recipie)
print(chai_order)

#for deletion you can do del name("key")
#for membership test "key" in name 


print(f"printing only keys :{chai_order.keys()}")
print(f"printing only values :{chai_order.values()}")
print(f"printing only items :{chai_order.items()}")

#updating
new_dict = dict(cardamon="crushed")
chai_order.update(new_dict)
print(chai_order)

#getting a value, 
customer_note = chai_order.get("customer_note", "No note available") 
#automatically set to no note available when no key named customer_note

