# list of users with their total bill amount and coupon code
users = [
    {"id": 1, "total": 100, "coupon": "P20"},
    {"id": 2, "total": 150, "coupon": "F10"},
    {"id": 3, "total": 80, "coupon": "P50"},
]

# dictionary of available coupons
# each coupon maps to a tuple: (percentage_discount, fixed_discount)
discounts = {
    "P20": (0.2, 0),   # 20% discount
    "F10": (0.5, 0),   # 50% discount
    "P50": (0, 10),    # flat 10 rupees discount
}

# loop through each user
for user in users:
    # get the (percent, fixed) discount values for the user's coupon
    # if coupon not found, default is (0, 0)
    percent, fixed = discounts.get(user["coupon"], (0, 0)) #percent,fixed is from discount list which has a key same as a value of a key in elemnets
    
    # calculate the discount = percentage of total + fixed amount
    discount = user["total"] * percent + fixed
    
    # print result for each user
    print(f'{user["id"]} paid {user["total"]} and got discount for next visit of rupees {discount}')


'''
Explanation of whats going on:
We have a list of users. Each user has:
id → their unique identifier,
total → their bill amount,
coupon → coupon code they used.
We have a dictionary discounts that defines how each coupon works:
Some coupons give a percentage discount (P20 = 20%),
Some coupons give a fixed rupee discount (P50 = 10 rupees),
Some may give both percentage + fixed (if defined).
For each user:
We check their coupon in discounts.
Extract its (percent, fixed) values.
If the coupon doesn’t exist, they get (0,0) (no discount).
Discount is calculated as:
'''