import random

print('-'*67)
print('Welcome to Rock, Paper, Scissors (Version 1)')
print('')
print("Let's play!")
playerChoice = input('Rock, Paper, Scissors shoot: ')
playerChoice = playerChoice.title()
computerChoice = random.choice(['Rock','Paper','Scissors'])
print('\n\t\t\t****************************\n\t\t\tPlayer chooses: {}\n\t\t\t\t vs \n\t\t\tComputer chooses: {}\n\t\t\t****************************\n'.format(playerChoice,computerChoice))
if playerChoice == computerChoice:
	print("It's a tie!")
elif (playerChoice == 'Rock' and computerChoice == 'Scissors') or (playerChoice == 'Scissors' and computerChoice == 'Paper') or (playerChoice == 'Paper' and computerChoice == 'Rock'):
	print('Player WINS!')
else:
	print('Player LOSES!')
print('-'*67)