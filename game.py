# import the random package so that we can generate a random choice
from random import randint
from gamefunctions import winlose, gamelives

while gamelives.player is False:
	#set player to True
	print("******************************************************\n")
	print("gamelives.Computer lives:", gamelives.computer_lives, "/", gamelives.total_lives, "\n")
	print("Player lives:", gamelives.player_lives, "/", gamelives.total_lives, "\n")
	print("Choose your weapon!\n")
	print("******************************************************\n")
	
	player = input("choose rock, paper or scissors: ")
	player = player.lower()

	print("computer chose", gamelives.computer, "\n")
	print("player chose", player, "\n")




	#handle all lives lost for player or AI
	if gamelives.player_lives is 0:
		winlose.winorlose("lost")
		# print("Out of lives! You suck at this game. Would you like to play again?")
		# choice = input("Y / N")
		# print (choice)

		# if (choice is "N") or (choice is "n"):
		# 	print("You chose to quit.")
		# 	exit()

		# elif (choice is "Y") or (choice is "y"):
		# 	#reset the game so we start over again
		# 	gamelives.player_lives = 5
		# 	gamelives.computer_lives = 5
		# 	player = False
		# 	gamelives.computer = choices[randint(0,2)]

	elif gamelives.computer_lives is 0:
		winlose.winorlose("won")
	# print("gamelives.Computer is out of lives! You rock at this game. Would you like to play again?")
	# choice = input("Y / N")
	# print (choice)

	# if (choice is "N") or (choice is "n"):
	# 	print("You chose to quit.")
	# 	exit()

	# elif (choice is "Y") or (choice is "y"):
	# 	#reset the game so we start over again
	# 	gamelives.player_lives = 5
	# 	gamelives.computer_lives = 5
	# 	player = False
	# 	gamelives.computer = choices[randint(0,2)]

	else:
		# need to check all of our conditions after checking for a tie

		gamelives.player = False
		gamelives.computer = gamelives.choices[randint(0, 2)]
