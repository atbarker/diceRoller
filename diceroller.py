#dice roller program for GM use in RPG's
#Author: Austen Barker
#date: 5/23/17

#Input syntax
#4d10+4
#Rolls 4 d10's and adds 4 to the result
#3d10x2+3
#rolls 3 d10's, multiplies result by 2 and adds 3
#handles rolls for d2,d4,d6,d8,d10,d12,d20, and d100/percentile

import argparse
import random
import re

def roll(number, dieType, multMod, addMod, verbose):
	#print number
	total = 0
	for num in range(0,number):
		#calculate random value for each die, add to running total
		randRoll = random.randint(1,dieType)
		#print value of each roll
                if verbose:
			print 'single die: %d' % randRoll
		total += randRoll
        #print the raw value of rolls
        if verbose:
		print 'die face sum: %d' % total
        if multMod != 0:
		total *= multMod
        if verbose:
                print 'multiplied roll: %d' % total
	total += addMod
	return total

parser = argparse.ArgumentParser(description='process options')
parser.add_argument('roll', metavar='roll', type=str, help='dice to be rolled with modifiers')
parser.add_argument('-v', action='store_true', help = 'verbose mode, prints values for each die rolled')

args = parser.parse_args()

line = args.roll

#split the string using regular expressions and delimiters using the re.split() method
rollFields = re.split(r'[dx+]\s*',line)
rollFields = map(int, rollFields)
if 'x' in line and '+' in line:
	pass
elif 'x' in line:
	rollFields.append(0)
elif '+' in line:
	rollFields.append(rollFields[2])
	rollFields[2] = 1
else:
	rollFields.append(1)
	rollFields.append(0)

#new object for the roll
#print rollFields
result = roll(rollFields[0],rollFields[1], rollFields[2], rollFields[3], args.v)
print 'result: %d' % result

