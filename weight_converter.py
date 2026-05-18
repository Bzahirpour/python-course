# Challange ask the user for their weight and conver it to lbs or kgs after asking which unit their input was is
import sys
weight = input('What is your weight? ')
if weight.isdigit():
    print('Ok lets check if that is in Lbs or Kgs:')
else:
    print('you must enter a number to continue')
    sys.exit()

unit = input('Is your weight in (L)bs or (K)gs? ')
if len(unit) == 1 and unit in 'Ll':
    weight_kgs = (int(weight) * 0.45359237)
    print('Your weight in kgs is ' + str(weight_kgs))

elif len(unit) == 1 and unit in 'Kk':
    weight_lbs = (int(weight) * 2.20462)
    print('Your weight in lbs is ' + str(weight_lbs))

else:
    print('You must enter either Ll or Kk for converting weight to the approriate unit')

# Other solution
while True:
    try:
        weight = float(input('what is your weight?: '))
        break
    except ValueError:
        print('Weight must be a number')
        continue


while True:
    lbs_or_kgs = input('is that in (L)bs or (K)gs?: ').lower()
    if lbs_or_kgs == 'l':
        final_weight = weight / 2.2
        print(f'you are {final_weight} kgs')
        break
    elif lbs_or_kgs == 'k':
        final_weight = weight * 2.2
        print(f'you are {final_weight} lbs')
        break
    else:
        print('you must enter l or k genius')
        continue