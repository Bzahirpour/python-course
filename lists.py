list = [8, 3, 7, 6, 1, 9, 2, 3, 5, 7]
biggest_number = list[0]
for current_number in list:
    if biggest_number < current_number:
        biggest_number = current_number
print(biggest_number)
