import random

print('-'*67)
print('Welcome to Rock, Paper, Scissors (Version 1)')
print('')
print("Let's play!")

wins = 0
losses = 0
playing = True

while playing == True:
	playerChoice = input('Rock, Paper, Scissors shoot: ')
	playerChoice = playerChoice.title() # Makes it the right format for comparing

	while playerChoice not in ['Rock','Paper','Scissors']:
		print('Sorry that is not an option.')
		playerChoice = input('Rock, Paper, Scissors shoot: ')
		playerChoice = playerChoice.title()

	computerChoice = random.choice(['Rock','Paper','Scissors'])
	print('\n\t\t\t****************************\n\t\t\tPlayer chooses: {}\n\t\t\t\t vs \n\t\t\tComputer chooses: {}\n\t\t\t****************************\n'.format(playerChoice,computerChoice))
	if playerChoice == computerChoice:
		print("It's a tie!")
	elif (playerChoice == 'Rock' and computerChoice == 'Scissors') or (playerChoice == 'Scissors' and computerChoice == 'Paper') or (playerChoice == 'Paper' and computerChoice == 'Rock'):
		print('Player WINS!')
		wins = wins + 1
	else:
		print('Player LOSES!')
		losses = losses + 1
	print('Score')
	print('\tWins: {}'.format(wins))
	print('\tLosses: {}'.format(losses))
	stop = input('If you want to stop playing type QUIT, otherwise press enter: ')
	if stop.upper() == 'QUIT':
		playing = False
print('-'*67)




