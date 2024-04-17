# Len function outputs the length of the string, can be used to dictate length of input from users
course = 'Python for Beginners'
print(len(course))

# Convert all characters to upper case, using a "dot operator" these are called "methods"
# A method is specific to a object
print(course.upper())
print(course.lower())

# If we print the variable it will not retain the method used above
print(course)

# Finds the first occurance of that character in the string
print(course.find('Beginners'))

# Replace a section of string with a new section
print(course.replace('Beginners', 'absolute beginners'))

# Checks if 'Python' is IN the course variable, is a boolean (produces a true or false statement)
print('Python' in course)