  
# Okay, so we are going to create a program for D&D dice
# first lets import the random module
import sys
import random

# now, lets create the dice functions


def twenty():
    print("\nYou rolled:",random.randint(1,20), ) # to choose a random number between 1 and 20

def twelve():
    print("\nYou rolled:",random.randint(1,12)) # to choose between 1 and 12

def ten():
    print("\nYou rolled:",random.randint(1,10)) # to choose between 1 and 10

def eight():
    print("\nYou rolled:",random.randint(1,8)) # to choose between 1 and 8

def six():
    print("\nYou rolled:",random.randint(1,6)) # to choose between 1 and 6

def four():
    print("\nYou rolled:",random.randint(1,4)) # to choose between 1 and 4

def percent():
    print("\nYou rolled:", random.randint(1,100),'%') # to choose between 1% and 100%
    


# now a function to start

def start():
    print('Ready to roll')
    
    valid_inputs = ['20', '12', '10', '8', '6', '4', 'percent', 'exit']
    
    while True: # to keep the program running until you quit 

        try:
            # set the value of "roll" with user input
            roll = input('\nChoose your dice or exit:\n20, 12, 10, 8, 6, 4, or percent.\n>> ')
            
            # prevent the program from breaking if invalid input is used 
            if roll not in valid_inputs:
                print('thats not a valid choice, try again')
                continue
                

            if '20' in roll:
                twenty()
                print("out of 20")
            if '12'in roll:
                twelve()
                print("out of 12")
            if '10'in roll:
                ten()
                print("out of 10")
            if '8' in roll:
                eight()
                print("out of 8")
            if '6' in roll:
                six()
                print("out of 6")
            if '4' in roll:
                four()
                print("out of 4")
            if 'percent'in roll:
                percent()

        except:
            print("That is not an option.")

        if 'exit' in roll:
            print("Goodbye!")
            exit(0)

start()