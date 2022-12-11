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


# Function to check if player has key
def has_key():
  return "key" in inventory


# Initialize player's location
location = "outside"

while True:
  # Print player's location
  print(f"You are currently {location}.")

  # Print available actions
  if location == "outside":
    print("You can [enter] the house, [walk] down the road, or [look] around.")
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
    print("You walk down the road and find a treasure chest!")
    location = "chest"
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
  else:
    print("Invalid action.")