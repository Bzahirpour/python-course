cart = [10, 20, 40]
total_price = 0
for item in cart:
    print(f'Item Cost: {item}')
    total_price += item
tax = total_price * .06
total_price_with_tax = total_price * 1.06
print(f'Subtotal: {total_price}')
print(f'Tax: {tax}')
print(f'Total: {total_price_with_tax}')