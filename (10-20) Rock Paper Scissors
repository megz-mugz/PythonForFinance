from random import randint

def RPS ():
    option = ['rock', 'paper', 'scissors']
    wins = 0
    losses = 0
    for i in range(1,101):
        bot = option[randint(0,2)]

        user = input('rock, paper, or scissors?')

        # same option selected
        if bot == user:
            print('Tie')
            print('bot threw:', bot)
            print('You threw:', user)

        # conditions w/ bot == rock
        elif bot == 'rock' and user == 'paper':
            print('YOU WIN!!!')
            wins += 1
        elif bot == 'rock' and user == 'scissors':
            print('YOU LOSE :(')
            losses += 1

        # conditions w/ bot == paper
        elif bot == 'paper' and user == 'rock':
            print('YOU LOSE :(')
            losses += 1
        elif bot == 'paper' and user == 'scissors':
            print('YOU WIN!!!')
            wins += 1

        # conditions w/ bot == scissors
        elif bot == 'scissors' and user == 'rock':
            print('YOU WIN!!!')
            wins += 1
        elif bot == 'scissors' and user == 'paper':
            print('YOU LOSE :(')
            losses += 1

        # odd ball conditions
        elif user != 'rock' or 'paper' or 'scissors':
            print(TypeError, "INVALID INPUT")


        print('Wins:', wins, "Losses:", losses)

RPS()
