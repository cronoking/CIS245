# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: <author>
# Creation Date: <date>
# Below is a simple program with 10 issues (some are syntax errors and some are logic errors.  You need to identify the issues and correct them.

import random
import time

def displayIntro():
	print('''You are in a land full of dragons. In front of you,
	you see two caves. In one cave, the dragon is friendly
	and will share his treasure with you. The other dragon
	is greedy and hungry, and will eat you on sight.''')
  #--empty print is called instead of using newline(1)
	print()

def chooseCave():
  cave = ''
  while cave != '1' and cave != '2':
	  print('Which cave will you go into? (1 or 2)')
	  cave = input()
  #--return variable is misspelled(2)
  return caves

def checkCave(chosenCave):
	print('You approach the cave...')
	#sleep for 2 seconds
	time.sleep(2)
	print('It is dark and spooky...')
	#sleep for 2 seconds
  #--comment suggests time.sleep should be 2 seconds not 3(3)
	time.sleep(3)
	print('A large dragon jumps out in front of you! He opens his jaws and...')
  #--empty print is called instead of using newline(4)
	print()
	#sleep for 2 seconds
	time.sleep(2)
	friendlyCave = random.randint(1, 2)

	if chosenCave == str(friendlyCave):
		print('Gives you his treasure!')
	else:
    #--print is missing parentheses(5)
		print 'Gobbles you down in one bite!'

playAgain = 'yes'
#--loop conditions using assignment instead of comparator(6)
while playAgain = 'yes' or playAgain = 'y':
	displayIntro()
  #--chooseCave is missing capitalization on Cave(7)
	caveNumber = choosecave()
	checkCave(caveNumber)
    
	print('Do you want to play again? (yes or no)')
	playAgain = input()
  #--only checks for no and not 'n'(8)
	if playAgain == "no":
    #--playing is misspelled(9)
		print("Thanks for planing")
    #--program doesn't exit(10)

