def biggest_number(numbers):
    biggest = numbers[0]
    for number in numbers:
        if number > biggest:
            biggest = number
    return biggest

