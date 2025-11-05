#() is used to create tuples, they are immutable
masala_spices = ("cardamon", "ginger", "pistachio", "lemon")

#how to destructure
(spice1, spice2, spice3, spice4) = masala_spices


#membership check
print(f"is ginger present in our spices : {'ginger' in masala_spices}")