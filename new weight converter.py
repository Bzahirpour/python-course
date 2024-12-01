print('Weight Converter')
weight = input('weight: ')
unit = input('(L)bs or (K)g: ')

if unit.upper() == 'K':
    lbs = int(weight) * 2.20462
    print('Converted weight is: ' + str(lbs) + ' pounds')
elif unit.upper() == 'L':
    kgs = int(weight) * 0.453592
    print('Converted weight is: ' + str(kgs) + ' kilos')
else:
    print('unit must be in Lbs or Kgs')
