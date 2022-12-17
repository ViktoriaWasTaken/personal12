import colorama
from colorama import Back, Fore, Style

colorama.init(autoreset=True)

# Welcome the player and prompt them for their name
print(Fore.RED + "Tell me your name")
name = input("")
print(f"Welcome\n{name}")

# Initialize variables for the game
return_count = 0
progress = 1

while True:
    if progress == 1:
        # Introduce the game and present the first choice
        print(
            Fore.RED +
            "You hear a chute open, you fall and hit the ground. Everything goes dark..."
        )
        print("...")
        print("...")
        print("...")
        print("Open your eyes?")
        print("1. Yes")
        print("2. No")
        print("3. Try to ")
        choice = input("")
        if choice == "1":
            start = "You find yourself in a Small dark room entirely empty with 2 doors"
            progress = 2
        elif choice == "return":
            return_count += 1
            # Return to the beginning of the loop
            continue
        else:
            # End the loop if the player enters an invalid choice
            break
    elif progress == 2:
        # Present the second choice
        print(start)
        print("Choose a door")
        print("1. Wood")
        print("2. Stone")
        choice = input("")
        if choice == "1":
            choice1 = "You enter the wooden door and before you lays a dark misty woodland path. You hear a faint howl"
            progress = 3
        elif choice == "2":
            choice2 = "You enter the stone door and before you lays a dark damp cave. It smells of mold"
            progress = 4
        elif choice == "return":
            return_count += 1
            # Return to the beginning of the loop
            continue
        else:
            # End the loop if the player enters an invalid choice
            break
    elif progress == 3:
        # Present the first branch of the story
        print(choice1)
        print("1. Press onward")
        print("2. Return")
        choice = input("")
        if choice == "1":
            choice1_1 = "You follow the woodland path and find a clearing. You feel as though you're being watched"
            progress = 5
        elif choice == "return":
            return_count += 1
            # Return to the beginning of the loop
            continue
        else:
            # End the loop if the player enters an invalid choice
            break
    elif progress == 4:
        # Present the second branch of the story
        print(choice2)
        print("1. Press onward")
        print("2

