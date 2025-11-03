"""
Restaurant Billing System

This program demonstrate:
1. User input for menu item quantities
2. Aritmetic calculations for subtotal, tax and total
3. Formated bill output
4. Basic conditional logic for discounts
"""

print("_" * 50)
print("        RESTAURANT BILLING SYSTEM")
print("_" * 50)
print()

burger_price = 12.99
fries_price = 4.50
soda_price = 2.25

print("Menu Items and Prices:")
print(f"Burger: ${burger_price}")
print(f"Fries: ${fries_price}")
print(f"Soda: ${soda_price}")
print("_" * 30)

print("Please enter the quantity for each item:")
burger_qty = int(input("Number of burgers: "))
fries_qty = int(input("Number of fries: "))
soda_qty = int(input("Number of sodas: "))

print()

subtotal = (burger_qty * burger_price) + (fries_qty * fries_qty) + (soda_qty * soda_price)

tax_rate = 0.10
tax = subtotal * tax_rate

discount = 0
if subtotal >50:
    discount = 5.00

total = subtotal + tax - discount

print("_" * 50)
print("            BILL RECEIPT")
print("_" * 50)

if burger_qty > 0:
    print(f"Burger   x {burger_qty}    @ ${burger_price} each = ${burger_qty * burger_price:.2f}")
if fries_qty > 0:
    print(f"Fries   x {fries_qty}    @ ${fries_price} each = ${fries_qty * fries_price:.2f}")
if soda_qty > 0:
    print(f"Soda   x{soda_qty}    @ ${soda_price} each = ${soda_qty * soda_price:.2f}")

print("_" * 50)
print(f"Subtotal:      ${subtotal:.2f}")
print(f"Tax (10%):     ${tax:.2f}")

if discount > 0:
    print(f"Discount:    -${discount:.2f}")

print("_" * 50)
print(f"TOTAL:      ${total:.2f}")
print("_" * 50)
