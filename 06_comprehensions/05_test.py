"""
    items: A list of dictionaries, each representing a product with keys:
        - "name": str
        - "price": int
        - "category": str
    
    Returns:
        - List of names of affordable products (price < 500)
        - Set of unique categories
        - Dictionary of product name to price mapping
        - Generator expression converted to list of prices after applying 10% discount
"""

def filter_inventory(items: list[dict]) -> tuple[list[str], set[str], dict[str, int], list[int]]:
    # Note: Using the provided hardcoded 'items' list inside the function
    items = [
        {"name": "Notebook", "price": 250, "category": "Stationery"},
        {"name": "Pen", "price": 100, "category": "Stationery"},
        {"name": "Bag", "price": 1200, "category": "Accessories"},
        {"name": "Bottle", "price": 400, "category": "Utensils"},
    ]

    # 1. Extract names of products priced below ₹500 using list comprehension.
    affordable_names = [
        item["name"]
        for item in items
        if item["price"] < 500
    ]

    # 2. Extract all unique categories using set comprehension.
    unique_categories = {
        item["category"]
        for item in items
    }

    # 3. Create a name-to-price mapping using dictionary comprehension.
    name_to_price_map = {
        item["name"]: item["price"]
        for item in items
    }

    # 4. Generate a list of discounted prices using a generator expression and convert it to a list.
    # The discount is 10%, so the new price is the old price * 0.9.
    # We use int() to cast the result to an integer as required by the return type hint (list[int]).
    discount_gen = (
        int(item["price"] * 0.9)
        for item in items
    )

    # Convert the generator expression result to a list
    discounted_prices = list(discount_gen)

    # Return all four outputs as a tuple
    return (
        affordable_names,
        unique_categories,
        name_to_price_map,
        discounted_prices
    )

# Example Usage:
result = filter_inventory([]) # The function uses its internal list, so the input is ignored
print(f"Affordable Names (List Comp): {result[0]}")
print(f"Unique Categories (Set Comp): {result[1]}")
print(f"Name to Price Map (Dict Comp): {result[2]}")
print(f"Discounted Prices (Gen Exp): {result[3]}")