#blackjack or 21 game

import random
#the planning phase
	# dealer cards
dealer_cards = []

	# player cards
player_cards = []

	# deal the cards
	# display the cards
# dealer cards
while len(dealer_cards) != 2:
	dealer_cards.append(random.randint(1, 11))
	if len(dealer_cards) == 2:
		print("Dealer has X &", dealer_cards[1])

# player cards
while len(player_cards) != 2:
	player_cards.append(random.randint(1, 11))
	if len(player_cards) == 2:
		print("You have ", dealer_cards)

# sum of the dealer cards
if sum(dealer_cards) == 21:
	print("Dealer has 21 and wins!")
elif sum(dealer_cards) > 21:
	print("Dealer has busted!")

# sum of the player cards

while sum(player_cards) < 21:
	action_taken = str(input("Do you want to stay or hit? "))
	if action_taken == "hit":
		player_cards.append(random.randint(1,11))
		print("You now have a total of " + str(sum(player_cards)) + " from these cards", player_cards)
	else:
		print("The dealer has a total of " + str(sum(dealer_cards)) + " with ", dealer_cards)
		print("You have a total of " + str(sum(player_cards)) + "with ", player_cards)
		if sum(dealer_cards) > sum(player_cards):
			print ("Dealer wins!")
		else: 
			print("You win!")
			break

if sum(player_cards) > 21:
	print("You BUSTED! Dealer wins.")
elif sum(player_cards) == 21:
	print("You have BLACKJACK! You win!! 21")

# compare the sums of the cards between D v P 
# if the p sum is greater than 21 = bust
# if p sum is less than 21 = option hit or stay
# if p option stay copmare sum of D v P 
# if p sum < 21 & > d then p wins!
# if p sum < d sum then p loses
