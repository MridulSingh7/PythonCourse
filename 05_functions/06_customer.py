def generate_invoice(customer_name="Guest", *items, **charges) -> str:
    lines = [f"Invoice for {customer_name}:"]

    # Items section
    if items:
        lines.append("Items:")
        for item in items:
            lines.append(f"- {item}")

    # Charges section
    if charges:
        lines.append("Charges:")
        for charge_name, amount in charges.items():#how to access keywords and values in ** functions
            lines.append(f"{charge_name.capitalize()}: {amount}")

    # Total amount due
    total = sum(charges.values())
    lines.append(f"Total Amount Due: ₹{total}")

    return "\n".join(lines)

# Examples
print(generate_invoice("Amit", "Burger", "Fries", tax=50.0, service=20.0))
print()
print(generate_invoice("Riya", tax=30.0))
print()
print(generate_invoice())
print()
print(generate_invoice("John", "Pizza", "Coke"))
