secret_number = 9
tries = 0
print('Guess the secret number')
while tries < 3:
    guess = input('Guess: ')
    if int(guess) == int(secret_number):
        print('You win!')
        exit()
    else:
        tries = tries + 1
print('Better luck next time!')