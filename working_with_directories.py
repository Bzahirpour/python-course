from pathlib import Path

path = Path('/Users/benz/Documents/Python/Mosh/python-course/ecommerce/neato')

print(path.exists()) # returns a boolean

if path.exists() == True:
    path.rmdir()
if path.exists() == False:
    path.mkdir() # makes a dir called neato from the path class above


thispath = Path()
for file in thispath.glob('*.py'):
    print(file)



