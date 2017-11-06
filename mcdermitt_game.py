#Shannon Mcdermitt - Author

#Import statements are below:
from sys import exit

#Function to quit game.
def quitGame():
    choice = input('To quit press Q. To proceed press enter.')
    if choice == 'q' or choice == 'Q':
        exit()
    
#Initiate quit game function at the onset.
quitGame()
#welcome() function prints out welcome messages
#and asks users if they want to play.
def welcome():
    print('\nHello! Welcome to the collection game!')
    print('To play it will require the participation of two players. [press enter]')
    print(input(''))
    letsPlay = str.lower(input('Do you have a friend nearby? yes or no?\n'))
    if letsPlay == 'yes' or letsPlay == 'y':
        print('Cool, let\'s get started.\n')
        rules()
        makePlayer()
    elif letsPlay == 'no' or letsPlay == 'n':
        print('Make a friend and come back later.')

#rules() function to print rules out
def rules():
    print('The rules of the game are as follows.\n')
    print('First I\'m going to collect some information.\n')
    print('Nothing crazy. Just your name and favorite animal.\n')
    print('After that each player will be prompted to select five items.\n')
    print('After your items are chosen each player will take turns guessing')
    print('items in their partner\'s collection.\n')
    print('The first person to guess all five item\'s wins!\n')
    print('It\'s not rocket science but it\'s fun!\n')
  
def hideItems():
    count = 0
    while(count < 45):
        print('.')
        count = count + 1
        
#Function to make player and fill dictionary values.
def makePlayer():
    print('Alright player one I need some information from you.')
    players = {}
    players['player1'] = {}
    players['player1']['name'] = input('What is your name: ')
    players['player1']['age'] = input('How old are you: ')
    players['player1']['job'] = input('What is your current occupation:  ')
    players['player1']['animal'] = input('What is your favorite animal:  ')
    player1Name = str.upper(players['player1']['name'])
    print('Alright player two avert your eyes, ' + player1Name + ' is picking their items.')
    
    #Initialize player one's item inventory
    players['player1']['items'] = {}
    players['player1']['items']['item1'] = input('\nitem 1: ')
    players['player1']['items']['item2'] = input('\nitem 2: ')
    players['player1']['items']['item3'] = input('\nitem 3: ')
    players['player1']['items']['item4'] = input('\nitem 4: ')
    players['player1']['items']['item5'] = input('\nitem 5: ')
    p1ItemList = players['player1']['items'].values()
    hideItems()
    
    #Initialize player two's item inventory
    print('Ok player 2 it\'s your turn now.')
    players['player2'] = {}
    players['player2']['name'] = input('What is your name: ')
    players['player2']['age'] = input('How old are you: ')
    players['player2']['job'] = input('What is your current occupation:  ')
    players['player2']['animal'] = input('What is your favorite animal:  ')
    player2Name = str.upper(players['player2']['name'])
    print('Cool, thanks for the info.')
    print('Ok ' + player1Name + ' turn away. It\'s time for ' + player2Name +  ' to choose their items.')
    #Initialize player two's item inventory
    players['player2']['items'] = {}
    players['player2']['items']['item1'] = input('\nitem 1: ')
    players['player2']['items']['item2'] = input('\nitem 2: ')
    players['player2']['items']['item3'] = input('\nitem 3: ')
    players['player2']['items']['item4'] = input('\nitem 4: ')
    players['player2']['items']['item5'] = input('\nitem 5: ')
    p2ItemList = players['player2']['items'].values()
    hideItems()

    #Function checks items
    def checkItems():
        p1Score = 0
        p2Score = 0
        def printScore():
            print(player1Name, ': ', p1Score)
            print(player2Name, ': ', p2Score)
        while (p1Score < 5 and p2Score < 5):
            p2ItemCheck = input(player1Name + ' please guess an item in ' + player2Name +  '\'s inventory:' )
            if p2ItemCheck in p2ItemList:
                print('Great guess!', player1Name, '. You guessed ', p2ItemCheck)
                p1Score = p1Score + 1
                printScore()
            else:
                print('Sorry, guess again')
                printScore()
            p1ItemCheck = input(player2Name + ' please guess an item in ' + player1Name +  '\'s inventory:' )
            if p1ItemCheck in p1ItemList:
                print('Great guess!', player2Name, '. You guessed ', p1ItemCheck )
                p2Score = p2Score + 1
                printScore()
            else:
                print('Sorry, guess again')
                printScore()
        if (p1Score == 5 or p2Score == 5):
            print('You made five correct guesses and won the game!')
            printScore()
    checkItems()
    
#Asks player if they'd like to play again
playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
    welcome()
    print('Do you want to play again? (yes or no)')
    playAgain = input()     
    if playAgain == 'no' or playAgain == 'n':
        print('See you next time!')
        break