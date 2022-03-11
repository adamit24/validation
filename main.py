# Name: Taylor Adami
# Date:
# File: Validation with list and use of if/if not statements
# Project: validationList --> main.py
# ----------------------------------------------------------

# Pre defined variables
inventory = ['dagger', 'shield', 'bracers', 'helmet', 'intellect ring']
firstChoice = ['spell book', 'wand', 'fire staff']
secondChoice = ['rations', 'flint & stone', 'disenchantment powder', 'map', 'lock pick set', 'boss key', 'cocoa puffs']

# Creating the if/else statements to reference the list.
userInputSing = input('Please choose one item of your choice to add to your inventory: \n'
                      'Spell Book \n'
                      'Wand \n'
                      'Fire Staff \n').lower() # Input variable for the user to choose what Item they would like.

if userInputSing not in firstChoice: # if/else statement to check list. Can also use !=
    print('Please choose on of the options in the list') # prints error statement
    userInputSing = input('Please choose one item of your choice to add to your inventory: \n'
                          'Spell Book \n'
                          'Wand \n'
                          'Fire Staff \n').lower() # re-asks the question to the user
    inventory.append(userInputSing) # appends the item to the end of the list
    # What happens if they type something in wrong again? What does the program do? How can we fix this?
else: # Else Statement
    print('Thank you for choosing', userInputSing, 'item! It has been a your added to your inventory') # Confirmation message
    inventory.append(userInputSing) # appends the item to the end of the inventory list

userInputMulti = input('Please choose three of items of your choice and add them to nventory: Please use a comma to separate the items\n'
                       'rations \n'
                       'Flint & Stone \n'
                       'Disenchantment Powder \n'
                       'Map \n'
                       'Lock Pick Set \n'
                       'Boss Key \n'
                       'Cocoa Puffs \n').split(',')
if userInputMulti not in secondChoice :
    print('Please make sure you choose from the list.')
    userInputMulti = input(
        'Please choose three of items of your choice and add them to your inventory: Please use a comma to separate the items\n'
        'rations \n'
        'Flint & Stone \n'
        'Disenchantment Powder \n'
        'Map \n'
        'Lock Pick Set \n'
        'Boss Key \n'
        'Cocoa Puffs \n').split(',')

elif userInputMulti in secondChoice:
    inventory.extend(secondChoice)
    print('thank you for adding these to your inventory')
