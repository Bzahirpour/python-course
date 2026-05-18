def emoji_conversion(message):
    words = message.split(' ')
    emojis = {
        ':)': '😁',
        ':(': '😔',
        ';)': '😉'
    }
    output = ''
    for word in words:
        output += emojis.get(word, word) + ' '
    return output


message = input('> ')
print(emoji_conversion(message))


# Another solution
def emoji_converter(message):
    emoji_dict = {
        ':)': '😁',
        ':(': '☹️',
        ':o': '😮',
        'xp': '😝'
    }
    words = message.split(' ')
    output = ''
    for word in words:
        output += emoji_dict.get(word, word) + ' '

    return output

say_things = input()
print(emoji_converter(say_things))