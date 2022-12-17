# Adventure game in Python

# Define a list of actions that the player can take
actions = ["go north", "go south", "go east", "go west", "pick up object", "talk to NPC"]

# Define a list of objects that the player can interact with
objects = ["key", "sword", "shield"]

# Define a dictionary that maps actions to their descriptions
action_descriptions = {
    "go north": "You move north.",
    "go south": "You move south.",
    "go east": "You move east.",
    "go west": "You move west.",
    "pick up object": "You pick up an object.",
    "talk to NPC": "You speak with an NPC."
}

# Define a dictionary that maps objects to their descriptions
object_descriptions = {
    "key": "A small, metal key.",
    "sword": "A sharp, shining sword.",
    "shield": "A sturdy, wooden shield."
}

# Define a list of NPCs that the player can interact with
npcs = ["shopkeeper", "guard"]

# Define a dictionary that maps NPCs to their descriptions
npc_descriptions = {
    "shopkeeper": "A friendly shopkeeper who sells useful items.",
    "guard": "A tough guard who protects the town from danger."
}

# Define a list of the player's inventory
inventory = []

# Define a dictionary that maps locations to their descriptions
locations = {
    "town square": "You are in the town square, surrounded by shops and buildings.",
    "north of town": "You are north of the town, in a peaceful, grassy field.",
    "south of town": "You are south of the town, near a deep, dark forest.",
    "east of town": "You are east of the town, near a fast-flowing river.",
    "west of town": "You are west of the town, on a rocky, mountainous path."
}

# Define the player's current location
current_location = "town square"

# Define a function that presents the player with a description of their current situation
def describe_situation():
    print("You are currently in: " + locations[current_location])
    print("You can see the following objects:")
    for obj in objects:
        print(object_descriptions[obj])
    print("You can see the following NPCs:")
    for npc in npcs:
        print(npc_descriptions[npc])
    print("You have the following items in your inventory:")
    for item in inventory:
        print(object_descriptions[item])
    print("You can take the following actions:")
    for action in actions:
        print(action_descriptions[action])

# Define a function that allows the player to take an action
def take_action(action):
    global current_location
    if action == "go north":
        current_location = "north of town"
    elif action == "go south":
        current_location = "south of town"
    elif action == "go east":
        current_location = "east of town"
    elif action == "go west":
        current_location = "west of town"

def interaction(action):
    global npc_interaction
    if action = "talk to guard" and location = "town square"
            print():