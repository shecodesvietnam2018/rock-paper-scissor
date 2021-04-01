from random import randrange

while True:
	rock = 0
	paper = 1
	scissor = 2
	computer_choice = randrange(0, 2)
	user_choice = input("What is your choice? (Rock: 0, Paper: 1, Scissor: 2) ")
	user_choice = int(user_choice)
	if (user_choice + 1) % 3 == computer_choice:
		print("Computer wins!")
	elif user_choice == computer_choice:
		print("Tie!")
	elif user_choice > 2 or user_choice < 0:
		print("Please select the right choice!")
	else:
		print("You win!")
