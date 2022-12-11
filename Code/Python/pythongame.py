import time
import os
# Game title
print("Welcome to the Text Adventure!")
name = input("What is your name? ")
print("Welcome " + "[" + name + "]!")
time.sleep(2)
os.system("clear")
# Initialize player's inventory
inventory = []
# Initialize player's location
location = "outside"

while True:
  # Print player's location
  print(f"You are currently {location}.")

  # Print available actions
  if location == "outside":
    print("You can [enter] the house or [walk] down the road.")
    time.sleep(2)
    os.system("clear")
  elif location == "inside":
    print("You can [explore] the house or [go outside].")
    time.sleep(2)
    os.system("clear")
  elif location == "end":
    print("Thank you for playing" + "[" + name + "]!")
    time.sleep(2)
    os.system("clear")
  # Get player's input
  action = input("> ")

  # Handle player's action
  if action == "enter" and location == "outside":
    location = "inside"
  elif action == "walk" and location == "outside":
    print(
      "You walk down the road and find a treasure chest! do you wish to [unlock] it?"
    )
  elif action == "end" and location == "outside":
    inventory.append("treasure")
  elif action == "explore" and location == "inside":
    print("You explore the house and find a key!")
    inventory.append("key")
  elif action == "go outside" and location == "inside":
    location = "outside"
  elif action == "unlock" and location == "outside":
    location = "end"
  else:
    print("Invalid action.")