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
import sys
SHELL_STATUS_RUN = 1
SHELL_STATUS_STOP = 0

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
        #print the raw value of rolls if verbose is on
        if verbose:
		print 'die face sum: %d' % total
        if multMod != 0:
		total *= multMod
        if verbose:
                print 'multiplied roll: %d' % total
	total += addMod
	return total

def parseRoll(verbose, line):
	rollFields = re.split(r'[dx+]\s*', line)
        #debugging print statement
        #print rollFields
        if rollFields[0] == '':
                rollFields[0] = "1"
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
	result = roll(rollFields[0],rollFields[1], rollFields[2], rollFields[3], args.v)
	return result

def shell(args):
	status = SHELL_STATUS_RUN
        #shell loop
        while status == SHELL_STATUS_RUN:
        	sys.stdout.write('> ')
                sys.stdout.flush()
                line = sys.stdin.readline()
                #exit the shell
                if 'quit\n' in line or 'exit\n' in line:
                	status = SHELL_STATUS_STOP
                #toggle verbose while shell is running
                elif 'verbose\n' in line:
                        temp = args.v
                        args.v = not temp
                #by default handle a roll
                #change to check if stuff matches the regex     
                else:
                        #multiple rolls in the same line
                        result = 0
                        if ';' in line:
                                rollSerial = line.split(';')
                                for each in rollSerial:
                                	partial = parseRoll(args.v, each)
                                        print "result: %d" % partial
                        #multiple rolls to be added in same line
                        if ' + ' in line:
                                rollCombo = line.split(' + ')
				for each in rollCombo:
                                	result += parseRoll(args.v, each)
                                        print "result: %d" % result
                        else:
                                result = parseRoll(args.v, line)
                                print "result: %d" % result
                #print invalid warning
                #else:
                #        print 'Invalid input'
                

def main(args):
        #just start the shell
        print("Welcome to dice roller.\n")
	shell(args)


if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='process options')
	#parser.add_argument('roll', metavar='roll', type=str, help='dice to be rolled with modifiers')
	parser.add_argument('-v', action='store_true', help = 'verbose mode, prints values for each die rolled')
	args = parser.parse_args()
        main(args)
