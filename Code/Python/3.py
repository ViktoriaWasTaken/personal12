import time
import os


def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')


import colorama
from colorama import Back, Fore, Style

colorama.init(autoreset=True)

# Welcome the player and prompt them for their name
print(Fore.RED + "Tell me your name")
name = input("")
clear_screen()
print(f"Welcome\n[{name}]")
time.sleep(2)
clear_screen()
# Initialize variables for the game
return_count = 0
progress = 1
progress2 = 1
branch = 0
no_count = 0
version = 0.3
while True:
  time.sleep(0)
  if progress == 1:
    # Introduce the game and present the first choice
    print(
      Fore.GREEN +
      "You hear a chute open, you fall and hit the\nground. Everything goes dark..."
    )
    print("...")
    print("...")
    print("...")
    print("Open your eyes?")
    print("1. Yes")
    print("2. No")
    print("3. Try to... ")
    choice = input("")
    if choice == "1" and branch == 0 and return_count <= 1:
      start = Fore.CYAN + "You find yourself in a Small dark room entirely empty with 2 doors"
      progress = 2
      no_count = 0
      clear_screen()
    if choice == "1" and branch == 0 and no_count >= 3:
      start = Fore.CYAN + "You find yourself in a Small dark room entirely empty with 2 doors"
      progress = 2
      clear_screen()
    if choice == "1" and branch == 0 and return_count >= 1:
      start = Fore.CYAN + "You find yourself in a Small dark room entirely empty with 2 doors"
      progress = 2
      clear_screen()
    if choice == "2" and branch == 0 and no_count >= 3:
      start = Fore.CYAN + "You find yourself in a Small dark room entirely empty with 2 doors"
      no_count += 1
      progress = 1
      clear_screen()
      print(Fore.RED + "Shall you sleep forever?")
    elif choice == "2" and no_count <= 3:
      progress = 1
      no_count += 1
      branch = 0
      # Return to the beginning of the loop
      clear_screen()
      continue
    elif choice == "3" and no_count <= 3:
      branch = 0
      progress = 1
      clear_screen()
      print(Fore.RED + "THERE IS NO ESCAPE")
    elif choice == "3" and no_count >= 3:
      branch = 0
      progress = 1
      clear_screen()
      print(Fore.RED + "THERE IS NO ESCAPE")
      print(Fore.RED + "Shall you sleep forever?")
    else:
      clear_screen()
      # End the loop if the player enters an invalid choice
      continue
  elif progress == 2:
    # Present the second choice
    print(start)
    print("Choose a door")
    print("1. Wood")
    print("2. Stone")
    choice = input("")
    if choice == "1":
      choice1 = Fore.CYAN + "You enter the wooden door and before you lays a dark misty woodland path. You hear a faint howl"
      progress = 3
      branch = 1
      clear_screen()
    elif choice == "2":
      choice2 = Fore.CYAN + "You enter the stone door and before you lays a dark damp cave. It smells of mold"
      progress = 4
      branch = 2
      clear_screen()
    elif choice == "2":
      progress = 2
      return_count += 1
      branch = 0
      clear_screen()
      # Return to the beginning of the loop
      continue
    else:
      clear_screen()
      # End the loop if the player enters an invalid choice
      continue
  elif progress == 3:
    # Present the first branch of the story
    print(choice1)
    print("1. Press onward")
    print("2. Return")
    choice = input("")
    if choice == "1":
      choice1_1 = "You follow the woodland path and find a clearing. You feel as though you're being watched"
      progress = 5
      branch = 1
    elif choice == "return":
      progress = 2
      return_count += 1
      branch = 0
      # Return to the beginning of the loop
      continue
    else:
      # End the loop if the player enters an invalid choice
      continue
  elif progress == 5:
    # Present the first sub-branch of the story
    print(choice1_1)
    print(
      Fore.CYAN +
      "As you approach the end of the woodland path, you find a large tree with a strange symbol engraved on a door built into the front of the tree. It's surrounded by a circle pathway dug into the dirt"
    )
    print("1. Enter the tree")
    print("2. Examine the tree")
    print("3. Return")
    choice = input("")
    if choice == "1":
      choice1_2 = "You enter the door and it is remarkably heavy"
      progress = 6
    elif choice == "2":
      choice1_1_1 = "You examine the tree and find that the symbol on the door looks familiar"
    elif choice == "return":
      return_count += 1
      # Return to the beginning of the loop
      continue
    else:
      # End the loop if the player enters an invalid choice
      continue
  elif progress == 4:
    # Present the second branch of the story
    print(choice2)
    print("1. Press onward")
    print("2. Return")
    choice = input("")
    if choice == "1":
      # Do something here when the player chooses to press onward
      progress = 5
      branch = 2
    elif choice == "return":
      return_count += 1
      branch = 0
      # Return to the beginning of the loop
      continue
    else:
      # End the loop if the player enters an invalid choice
      continue
  elif progress == 6:
    # Present the second sub-branch of the story
    print(choice1_2)
    print("You enter the tree and find a small room with 3 doors")
    print("1.")
    print("2.")
    print("3.")
    print("4. Return")
    choice = input("")
    if choice == "1":
      choice1_2_1 = "You enter the red door and find a room filled with treasure"
    elif choice == "2":
      choice1_2_2 = "You enter the green door and find a room filled with weapons"
    elif choice == "3":
      choice1_2_3 = "You enter the blue door and find a room filled with magical artifacts"
    elif choice == "return":
      return_count += 1
      # Return to the beginning of the loop
      continue
    else:
      # End the loop if the player enters an invalid choice
      continue


    


