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


# Other solution

#guessing game

secret_number = 7
number_of_guesses = 3

while number_of_guesses > 0:
    guess = input('Guess a number: ')
    if int(guess) == secret_number:
        print('You Win!')
        break
    else:
        number_of_guesses -= 1
        print(f'{number_of_guesses} guesses remaining')
        continue

if number_of_guesses == 0:
    print('You Lose!')