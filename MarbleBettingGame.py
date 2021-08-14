import random


# Rules for the Game
# 1. You start with 1,000 gold coins
# 2. The bad has 10 marbles: 4 green and 6 red
# 3. If you draw a green marble you win the amount you bet
# 4. If you draw a red marble you lose the amount you bet
# 5. Before each draw you choose the amount you want to bet
# 6. The game is over after you lose all your coins or you type exit


# Give the user 1,000 gold pieces
# Get an input for the number of rounds
# Loop through each round
#   1. In each round ask the user how much they would like to bet
#   2. After each round, display the data for their # of gold coins
# Use the random function to get a random integer from 1-10
# If the integer is 1-6 (inclusive) then it is green else it is red
# If the user loses all of their money, the game is over

def MarbleBettingGame():
    goldCoins = 1000
    print("Welcome to a virtual marble betting game. Have fun!")
    n = 1
    roundNumber = 0
    marbleColor = ''

    betAmount = ''
    while n == 1:
        if betAmount == 'exit' or goldCoins <= 0:
            break
        roundNumber += 1

        betAmount = input(f'You have {goldCoins} gold coins left. How much would you like to bet? ')

        marble = random.randint(1, 10)
        if marble <= 6:
            goldCoins -= int(betAmount)
            marbleColor = 'Red'
        else:
            goldCoins += int(betAmount)
            marbleColor = 'Green'

        print(f'You got a {marbleColor} marble. And had {goldCoins} gold coins ater round {roundNumber}.')

    print('Thanks for playing!')


MarbleBettingGame()