#!/usr/bin/env python

# Import required modules
import sys

# Function to clear the screen
def cls():
    print("\033[H\033[J")

# Function to pause the game
def pause():
    input("Press enter to continue...")

# Display a title
print("game 1")

# Ask for the player's name
input_name = input("Tell me your name\nWhat is your name? ")

# Welcome the player
print("Welcome", input_name)

# Start the game
print("You hear a chute open you fall and hit the ground everything goes dark...")
print("...")
print("...")
print("...")
print("Open your eyes?")
print("1. Yes")
print("2. No")

# Get the player's choice
input_choice = input()

# Clear the screen
cls()

# Branch based on the player's choice
if input_choice == "1":
    start = "You find yourself in a dark room with no defining feature besides 2 doors"
elif input_choice == "2":
    start = "You remain unconscious"
else:
    start = "Invalid choice"

# Pause the game
pause()
# Show the situation
print(start)

# Ask the player to choose a door
if start == "You find yourself in a dark room with no defining feature besides 2 doors":
    print("Choose a door")
    print("1. Wood")
    print("2. Stone")

    # Get the player's choice
    input_door = input()

    # Clear the screen
    cls()

    # Branch based on the player's choice
    if input_door == "1":
        choice1 = "You enter the wooden door and before you lays a dark misty woodland path you hear a faint howl"
    elif input_door == "2":
        choice1 = "You enter the stone door and find yourself in a dark, damp cave. You hear the sound of dripping water in the distance."

print('You are unsure of where to go, but you see two paths leading deeper into the cave. One path is lit by dim torches, while the other is completely dark.')

print("1. Take the path lit by torches")
print("2. Take the path in complete darkness") 
input_path = input()

if input_path == "1":
path1 = "You follow the path lit by torches and come across a large chamber. In the center of the chamber is a treasure chest."

elif input_path == "2":

path1 = "You cautiously make your way through the dark path, using your hands to feel your way along the wall. After a while, you come across a branching path. One path leads to the left, and the other leads to the right."

print("1. Take the path to the left")
print("2. Take the path to the right")
input_branch = input()

if input_branch == "1":
  
branch1 = "You follow the left path and come across a river of lava. The heat is intense and you can feel it even from a distance. You see a small boat on the other side of the river."

elif input_branch == "2":

branch1 = "You follow the right path and come across a deep pit. You can hear the sound of monsters growling from below."

print("What do you do?")

print("1. Try to cross the lava river")
print("2. Attempt to jump across the pit")
print("3. Turn back and try the other path")
input_action = input()

if input_action == "1":
  
action1 = "You bravely attempt to cross the lava river, but the heat is too intense and you are quickly overcome. You die a painful death."

elif input_action == "2":

action1 = "You take a running start and jump across the pit, barely making it to the other side. You breathe a sigh of relief and continue on your journey."

else:

action1 = "You wisely decide to turn back and try the other path. You find yourself back at the branching path and take the other direction. This leads you to a hidden cave filled with treasure. You win the game!"

print(path1)
print(branch1)
print(action1)


# There are a few errors in this code that would prevent it from running properly.

# Some of the lines are indented incorrectly, which would cause the code to raise indentation errors. Indentation is important in Python 
# because it determines the structure of the code, so it's important to make sure that all lines are indented correctly.

# Some of the variables are not defined before they are used. For example, in the line print(path1), the variable 
# path1 is used but it is not defined anywhere in the code. This would cause a NameError to be raised when the code runs.

# There are some syntax errors in the code. For example, the line input_name = input("Tell me your name\nWhat is your name? ") has a syntax error 
# because the string inside the input function is not properly closed. This would cause a SyntaxError to be raised when the code runs.

# here are some logical errors in the code that would cause the game to behave in unexpected ways. For example, in the line if input_path == "1":,
# the variable path1 is defined, but it is never actually used in the code. This means that if the player chooses to take the path lit by torches, 
# the game will continue as if the player did not make a choice at all. This would be confusing for the player and could make the game less enjoyable.

# The game does not have a clear ending. The code only defines a few possible outcomes for the player, but there is no way for the player to know 
# when they have reached the end of the game or what they need to do to win. This could make the game feel incomplete or unfulfilling for the player.

# In summary, there are several errors in this code that would prevent it from running properly. 
# It would need to be revised and corrected in order to function as intended.