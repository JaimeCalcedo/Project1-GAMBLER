import random
#Dealer cards, because we need a place to store the different random cards the dealer obtains.
dealer_cards = []
#Player cards 
player_cards = []
#We create a list with all the different cards in the standard 52-card pack. 
#We will consider Jacks, Queens and Kings as 10s in the list considering their value in BJ. 
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
#Deal the cards, in this variable we must program the deal of 2 random cards to the dealer and the player. 
    #Dealer Cards: we got a also consider that from the 2 cards given to the dealer, only one is going to be seen by the player. 
while len(dealer_cards) != 2:
    dealer_cards.append(random.choice(cards))                        
    if len(dealer_cards) == 2:
        print("Dealer has:", dealer_cards[1], "faced up and another card faced down")
    #Player cards 
while len(player_cards) != 2:
    player_cards.append(random.choice(cards))   
    if len(player_cards) == 2:
        print("Player has:", player_cards)

#Sum of cards: now we are going to add up the value of the cards the player has. 
sum_of_player_cards = sum(player_cards)
sum_of_dealer_cards = sum(dealer_cards)

#Now we have to offer the player his 2 options: Hit or Stay, if he chooses another option we´ll force him to choose between our two options. 
print("You have", sum_of_player_cards, "What would you like to do?")
option = ""
#We also got to consider that the player can ask for another card (hit) as many times as he wants. 
while sum_of_player_cards < 21:
    option = input("Choose to Hit or to Stay: ")
    if option == "Hit":
        player_cards.append(random.choice(cards))   
        sum_of_player_cards = sum(player_cards)
        print(player_cards)
        print("Player has:", sum_of_player_cards)
        if sum_of_player_cards > 21:
            break
        while option == "Hit":
            option = input("Choose to Hit or to Stay: ")
            if option == "Hit":
                player_cards.append(random.choice(cards))   
                sum_of_player_cards = sum(player_cards)
                print(player_cards)
                print("Player has:", sum_of_player_cards)
                if sum_of_player_cards > 21:
                    break
            elif option == "Stay":
                print("You´ve stayed with", sum_of_player_cards)
                break
    elif option == "Stay":
        print("You´ve stayed with", sum_of_player_cards)
        break

if sum_of_player_cards > 21:
    print("You busted, YOU LOSE")
elif sum_of_player_cards <= 21:
    print("You stand a chance, lets watch the dealer")
    #Now we have to see what score the dealer gets.
    #Remember that main casino´s policy is that dealers stand with 17 or more and hits with less.
    print("Dealer flips the other card", dealer_cards, "Dealer has:", sum_of_dealer_cards)

    #Let´s apply the casino´s policy:
    while sum_of_dealer_cards < 17:
        dealer_cards.append(random.choice(cards))   
        sum_of_dealer_cards = sum(dealer_cards)
        print("Dealer hits and gets", dealer_cards, sum_of_dealer_cards)

    if sum_of_dealer_cards > 21:
        print("Dealer has", sum_of_dealer_cards,"so its busted, YOU WIN")
    else:
        print("Dealer has", sum_of_dealer_cards, "so it stays")
        #Finally (if we get to this point), lets compare the dealer´s and player´s scores:
        if sum_of_dealer_cards > sum_of_player_cards:
            print("YOU LOSE")
        elif sum_of_dealer_cards < sum_of_player_cards:
            print("YOU WIN")
        elif sum_of_dealer_cards == sum_of_player_cards:
            print("IT´S A TIE")