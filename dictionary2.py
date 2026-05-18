message = input('>')
words = message.split(' ')
emojis = {
    ':)': '😁',
    ':(': '😔',
    ';)': '😉'
}
output = ''
for word in words:
    output += emojis.get(word, word) + ' '
print(output)


# Convert a number phone number to words
word_of_number = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four"
}
phone = input("whats your number: ")
#print(word_of_number[phone[0]] + ' ' + word_of_number[phone[1]] + ' ' + word_of_number[phone[2]] + ' ' + word_of_number[phone[3]])
output = ''
for number in phone: 
    output += word_of_number.get(number, '!') + ' '

print(output)


# Emoji converter
emoji_dict = {
    ':)': '😁',
    ':(': '☹️',
    ':o': '😮',
    'xp': '😝'
}

string = input()
list = string.split(' ')
output = ''
for word in list:
    if word in emoji_dict:
        output += emoji_dict.get(word) + ' '
    else:
        output += word + ' '

print(output)