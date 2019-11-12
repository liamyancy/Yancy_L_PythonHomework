from gamefunctions import gamelives

# what are you trying to compare inside this funtions?
def comparechoices():
	if player.lower() == "quit":
		exit()
	elif gamelives.computer == player:
		print("tie! no one wins, play again")

	elif player.lower() == "rock":
		if gamelives.computer == "paper":
			print("You lose!", gamelives.computer, "covers", player, "\n")
			gamelives.player_lives = gamelives.player_lives - 1
		else:
			print("You win!", player, "smashes", gamelives.computer, "\n")
			gamelives.computer_lives = gamelives.computer_lives - 1

	elif player.lower() == "paper":
		if gamelives.computer == "scissors":
			print("You lose!", gamelives.computer, "cuts", player, "\n")
			gamelives.player_lives = gamelives.player_lives - 1
		else:
			print("You win!", player, "covers", gamelives.computer, "\n")
			gamelives.computer_lives = gamelives.computer_lives - 1

	elif player.lower() == "scissors":
		if gamelives.computer == "rock":
			print("You lose!", gamelives.computer, "smahses", player, "\n")
			gamelives.player_lives = gamelives.player_lives - 1
		else:
			print("You win!", player, "cuts", gamelives.computer, "\n")
			gamelives.computer_lives = gamelives.computer_lives - 1

	else:
		print("thats not a valid choice, try again")
