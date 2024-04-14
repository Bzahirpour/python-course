# Asks for input and assigns it to the variable birth year
birth_year = input('Birth year: ')

# Converts the str into an int, then back into a str
# Take the current year, subracts age and assigns it to the age variable, then prints it to the screen
age = 2024 - int(birth_year)
print('Your age is ' + str(age))

# Challange: ask user their weight in lbs and convert it to kilos
WEIGHT_LBS = input('What is your weight in lbs? ')
WEIGHT_KGS = int(WEIGHT_LBS) * 0.45359237
print('your wieght in kilograms is ' + str(WEIGHT_KGS))