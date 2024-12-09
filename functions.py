def greet_user(name):
    print(f'Hi, {name}!')
    print('Welcome aboard')

name = input('What is your name? ').capitalize()
print('Start')
greet_user(name)
print('Finish')



#names in this case are the parameter (the placeholders for our arguments)
def greet_names(first_name, last_name):
    print(f'Hello, {first_name} {last_name}')
    print('How are you today?')

#john and mary are the arguments (the things that get assigned to our parameter)
greet_names('John', 'Smith')
greet_names('Mary', 'Hatton')


greet_names(last_name='John', first_name='Smith')
greet_names('Mary', 'Hatton')



#
def square(number):
    return number * number

print(square(3))