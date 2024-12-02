# Create a game when you type help it tells you the actions, 'start' starts the car, 'stop' stops the car, 'quit' exits the game, any other command gives an error
action = input('>')
started = False
while action != 'QUIT':

    if action.upper() == 'HELP':
        print('start - to start the car')
        print('stop - to stop the car')
        print('quit - to exit')
    elif action.upper() == 'START':
        if started:
            print('Car is already started!')
        else:
            started = True
            print('Car started... Ready to go!')
    elif action.upper() == 'STOP':
        if not started:
            print('Car is already stopped!')
        else:
            started = False
            print('Car stopped.')
    elif action.upper() == 'QUIT':
        break
    else:
        print("I don't understand that...")

    action = input('>')

# Mosh's solution
