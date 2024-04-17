# Set a boolean, then if its true print the indented statement to esc press shift and tab
# Note Enjoy your day still prints even if the boolean is false because it is not indented
is_hot = False
is_cold = False

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold: 
    print("It's a cold day")
    print("Wear a warm jacket")
else:
    print("it's a lovely day")

# This message will always print
print('Enjoy your day')


# Challange: price of a house is $1M if the buyer has good credit, they need 10% down
# Otherwise they need 20% down, print the down payment for a buyer with good credit

price_of_house = int(1000000)
good_credit = True
bad_credit = False

if good_credit:
    print("you're down payment is " + '$' + str(price_of_house * .1))
elif bad_credit:
    print("you're down payment is " + '$' + str(price_of_house * .2))
else:
    print('You do not quilify')
