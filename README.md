# diceRoller

A simple application to automate rolling of dice for tabletop RPG gamemasters (GMs).
Allows for rolling large sets of dice, including modifiers, quickly and easily.
Rolls each virtual die individually to preserve the correct probabilistic distribution.
Supports dice sizes from d2 to d100/percentile.

Usage: diceroller.py [-h] [-v] roll


Options:
    -h       Help, display help
    -v       Verbose, prints the raw die results and the results of intermittent steps.
    
Roll Syntax:
    Example: 3d10x2+1
      3d10, roll 3d10 dice
      x2,   multiply the result by 2
      +1,   add a plus 1 modifier
