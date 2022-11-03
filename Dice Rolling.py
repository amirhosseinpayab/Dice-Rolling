import random
user = input("\nDo you want to rolling dice (y or n) ? ")
if user == 'y' or user == 'n':
    while user == 'y':
        dice = [1,2,3,4,5,6]
        computer = random.choice(dice)
        print(computer)
        user = input("Do you want agian (y or n) ? ")
        if user == 'n':
            print('\nGood bye :)\n')
            break
else:
        print('You are type wrong ! please do agian ...')
