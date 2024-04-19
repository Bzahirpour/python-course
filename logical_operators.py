# If both statements are true, print to screen
has_high_income = True
has_good_credit = True

if has_high_income and has_good_credit:
    print('Eligible for loan')

# Can be done with OR also
has_good_credit = True
has_high_income = False

if has_high_income or has_good_credit:
    print('Eligible for loan')

# Not changes the boolean value to the opposite, so in this case makes the and statement a double true like the example above
has_good_credit = True
has_criminal_record = False

if has_good_credit and not has_criminal_record:
    print('Eligible for loan')