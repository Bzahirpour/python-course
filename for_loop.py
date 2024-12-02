for item in 'Python':
    print(item)

# items inside of square brackets are a list:
for item in ['Ben', 'John', 'Sarah']:
    print(item)

# range function can create an object (two creates a step)
for item in range(5, 10, 2):
    print(item)

# prices is the items in the cart, total starts at zero
prices = [10, 20, 30]
total = 0
for price in prices:
    total = price + total
print(total)

for items in [30, 40, 90]:
    tot = items + total
print(tot)
