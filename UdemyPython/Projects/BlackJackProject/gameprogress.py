
def makebet():
	choice = "Wrong"
	howmuch = 0
	while choice not in ['Y','N']:
		choice = input("\nMake a bet? (Y) for Yes (N) for No. No will default to $1 \n").upper() 
		if choice not in ['Y','N']:
			print("Sorry, You need to type Y or N \n")	
		else:
			if choice == 'Y':
				while howmuch not in ['1','2','3','4','5','6','7','8','9','10']:
					howmuch = input("\nMake a bet? \n")
					if howmuch not in ['1','2','3','4','5','6','7','8','9','10']:
						print("Sorry, You need to bet at least $1 \n")
				return int(howmuch)
			else:
				return 1


def winners(player,hand):
	val = hand.values()
	if player == "bot":
        num = 0
        for i in val:
            num = sum(i) + num
		if num == 21:
			message = "The Bot Wins!"
			return False, message
		elif num > 21:
			message = "The bot player is Bust"
			return False, message
		else:
			message = "Still can play"
			return True, message
    else:
        num = 0
        for i in val:
            num = sum(i) + num
		if num == 21:
			message = "The Player Wins!"
			return False, message
		elif num > 21:
			message = "The player is Bust"
			return False, message
		else:
			message = "Still can play"
			return True, message

hand = {"hearts":[5],"spades":[],"diamonds":[],"clubs":[],"hidden":[6]}
winners('player',hand)
