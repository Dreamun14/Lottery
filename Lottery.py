# Import section
import random 
# Design Plan
# Print information about this game to the screen
print('Come one, come all! Welcome to my lottery game!\nHere you can test your luck and see if you can make a fortune!\nPlease remember to choose a number. In this lottery game, you can choose a number between 1 through 10.\n \nChoose wisely and good luck!')
# Lives
lives = 3
# Loop start
while lives > 0:
    print(f"You currently have {lives} lives left")
    lives = lives - 1
    # Input a number from 1-10
    print('-----------')
    pickednumber = int(input("Please enter a number :> "))
    # Generate a random number from 1-10(hidden)
    winningnumber = random.randrange(1, 10)
    # 3 chances (3 lives)
    # Does the winning number equal your number, if it does, then you win, else you lose
    if pickednumber == winningnumber:
        print('Congratulations! Luck was on your side!')
        input("Press any key to exit")
        break
    else:
        print('I\'m sorry, luck was not on your side today...')
    # show the winning number
    print(f"Thank your for playing, the winning number was {winningnumber} and the number you picked was {pickednumber}")
    input("Press any key to continue")
    print('')
