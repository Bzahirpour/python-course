#
secret_number = 9
guesses_used = 0
guess_limit = 3
while guesses_used < guess_limit:
    guess = int(input('Guess: '))
    guesses_used = guesses_used + 1
    if guess == secret_number:
        print('You win!')
        break
else:
    print('Try again!')
