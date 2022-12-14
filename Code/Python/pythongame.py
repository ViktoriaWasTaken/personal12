import time
import os
# Game title
print("Welcome to the Text Adventure!")
name = input("What is your name? ")
print("Welcome " + "[" + name + "]!")
time.sleep(2)


# Function to clear the screen
def clear_screen():
  time.sleep(2)
  os.system("clear")


# Initialize player's inventory
inventory = []

# Flag to track if player has found the chest
chest_found = False


# Function to check if player has key
def has_key():
  return "key" in inventory


# Initialize player's location
location = "outside"

while True:
  # Clear the screen
  clear_screen()

  # Print player's location
  print(f"You are currently {location}.")

  # Print available actions
  if location == "outside":
    if not chest_found:
      print("You can [enter] the house, [walk] down the road.")
    else:

      print(
        "You can [enter] the house, [walk] down the road, or [search] the road for the chest."
      )

  elif location == "inside":

    print("You can [explore] the house or [go outside].")
  elif location == "chest":

    print("You are at the treasure chest. You can [unlock] it or [go back].")

  elif location == "end":
    print("Thank you for playing" + "[" + name + "]!")
  # Get player's input
  action = input("> ")

  # Handle player's action
  if action == "enter" and location == "outside":
    location = "inside"
    
  elif action == "walk" and location == "outside":
    
    if not chest_found:
      print("You walk down the road and find a treasure chest!")
      location = "chest"
      chest_found = True
      
    else:
      location = "road"
      print("You walk down the road.")

  elif action == "end" and location == "outside":
    inventory.append("treasure")

  elif action == "explore" and location == "inside":
    print("You explore the house and find a key!")
    inventory.append("key")

  elif action == "go outside" and location == "inside":
    location = "outside"

  elif action == "unlock" and location == "chest" and has_key():
    # Only allow player to unlock chest if they have the key
    location = "end"

  elif action == "go back" and location == "chest":
    location = "outside"

  elif action == "search" and location == "road":
    
    if chest_found:
      print("You search the road and find the treasure chest.")
      location = "chest"

    else:
      print("You search the road but don't find anything.")

  else:
    print("Invalid action.")