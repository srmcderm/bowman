#a simple mad libs game
while True:
    name = input('Enter a name: ')
    verb = input('Enter a verb: ')
    adjective = input('Enter an adjective: ')
    noun = input('Enter a noun: ')
    
    sentence = name + ' ' + verb + ' through the forest, hoping to escape the ' + \
        adjective + ' ' + noun + '.'
    
    print('')
    print(sentence)
    print
    
    answer = input('Type q to quit, or anything else (even return/Enter) to continue: ')
    
    if answer == 'q':
        break
    
    print('Bye')