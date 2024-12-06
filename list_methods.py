numbers = [5, 2, 1, 7, 4]
# add a number to the end of a list
numbers.append(20)
# insert a number, first number is the location
numbers.insert(0, 5)
numbers.remove(5)
# remove last number
numbers.pop()
# check for the existence of a number in a list
print(numbers.index(5))
# OR (returns a boolean)
print(5 in numbers)
# count the number of times it occurs in the list
print(numbers.count(5))
# sort
(numbers.sort())
# reverse
numbers.reverse()
print(numbers)
# copy a list
numbers2 = numbers.copy()
numbers2.reverse()
print(numbers2)

#write a program to remove the duplicates in a list
list = [1,1,1,2,3,4,5,5,5,5,2,3,3]
list2 = []
list3 = []
for current_number in list:
    if current_number in list2:
        list3.append(current_number)
    else:
        list2.append(current_number)
print(list2)

#Moshs solution (I did not know you can do 'NOT in'
list = [1,2,3,1,2,3,4,5,3,5,3,2,1,6]
list2 = []
for current_number in list:
    if current_number not in list2:
        list2.append(current_number)
print(list2)