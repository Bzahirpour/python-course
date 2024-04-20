# If the temp is greater than 30 print to screen its a hot day
temp = 30

if temp > 30:
    print("It's a hot day")
else:
    print("It's not a hot day")

# If temp is greater than 30 is a boolean expression (a peice of code that produces a value)
temp = 35

if temp > 30:
    print("It's a hot day")
else:
    print("it's not a hot day")

# There is also greater than or equal to >= and less than or equal to <=
# Equal to is written like this, not it is different from the assignment operator that has only one equal sign
# Last one is not equal to !=
temp = 35

if temp == 30:
    print("It's a hot day")
else:
    print("It's not a hot day")

# Challange: Input form (name entered on form must be at least 3 characters long and no more than 50)
name = 'Ben'

if len(name) < 3:
    print('Name must be at least 3 characters')
if len(name) > 50:
    print('Name can be a maximum of 50 characters')
if len(name) >= 3 and len(name) <= 50: 
    print('Name looks good!')

# Mosh's solution
name = 'Ben'

if len(name) < 3:
    print('Name must be at least 3 characters')
elif len(name) > 50:
    print('Name can be a maximum of 50 characters')
else:
    print('Name looks good!')