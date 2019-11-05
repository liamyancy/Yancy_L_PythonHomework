from random import randint
def winorlose(status):
	# status will be either won or lost
	print("called win or lose")
	print("******************************************************")

	print("You", status, "! Would you like to play again?")

	choice = input("Y / N ")
	print (choice)

	if (choice is "N") or (choice is "n"):
		print("You chose to quit.")
		exit()

	elif (choice is "Y") or (choice is "y"):
		#reset the game so we start over again
		global player_lives
		global computer_lives
		global player
		global computer
		global choices

		player_lives = 5
		computer_lives =5
		player = False
		computer = choices[randint(0,2)]