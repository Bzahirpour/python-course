# Use double quotes in a string when you want to use an apostrophe in the string
course = "Python's course for beginners"
print(course)

# For multi line strings use triple quotes
print(''' 
Hi john,
      Here is our first email to you.
      thank you,
      The support team
''')

# For indexing each character is represented by a digit 01234 etc
# Use square brackets to identify which index we want to use (0 will return a P in this case)
line = 'Python for beginners'
print(line[0])

# Negitive index counts from the end of the string
# Negitive one will return s in this case
cat = 'Python for beginners'
print(cat[-1])

# To return multiple characters you can use the following
# 0:3 will return 012 in this case Pyt (from the first index to the last but not including the last)
cat = 'Python for beginners'
print(cat[0:3])

# Default index leave it blank will start or end at beginning or end of the string
# Will return the entire string
cat = 'Python for beginners'
print(cat[0:])