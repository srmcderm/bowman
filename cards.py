import random

#Loop to ask user to pick card.
def pickCard():
    choice = 'yes';
    print('Would you like to pick a card?')
    choice = str.lower(input())
    while choice == 'yes' or choice == 'y':
        shuffleDeck()
        if choice != 'yes' or choice !='y':
            break

#I know the directions said 52 items but I thought this made more sense.
#And my list doesn't end up being huge.
#Function to shuffle deck and select card.
def shuffleDeck():
    cardNumber = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
    cardSuit = ['Spades', 'Clubs', 'Diamonds', 'Hearts']
    i = 0
    print(random.choice(cardNumber) + ' of ' + random.choice(cardSuit))
    pickCard()
        
pickCard()