tea_prices_inr = {
    "masala Chai":80,
    "Green Tea":100,
    "Lemon Tea":90,
}

tea_prices_usd = {tea:price/80 for tea,price in tea_prices_inr.items()}
#this is how to traverse in a dict, {key:value for key,value in dict_name.items()}
#dictname.items returns all the key:value pairs like key:value
print(tea_prices_usd.items())