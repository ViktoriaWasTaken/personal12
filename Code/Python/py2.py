import colorama
from colorama import Back, Fore, Style

colorama.init(autoreset=True)

#------------------------------------------------------------------------------------
#                                                                                   |
#                                   Game Start  :Beginning                          |
#                                                                                   |
#------------------------------------------------------------------------------------
#Saves and remebers name
print(Fore.RED + "Tell me your name")
name = input("")
print(f"Welcome\n{name}")

print(Fore.RED + "You hear a chute open, you fall and hit the ground. Everything goes dark...")
print("...")
print("...")
print("...")
print("Open your eyes?")
print("1. Yes")
print("2. No")
print("3. Try to ")
choice = input("")
#choices
if choice == "1":
    start = "You find yourself in a Small dark room entirely empty with 2 doors"

#------------------------------------------------------------------------------------
#                                                                                   |
#                                First choice     :FC                               |
#                                                                                   |
#------------------------------------------------------------------------------------                                                                  
print(start)
print("Choose a door")
print("1. Wood")
print("2. Stone")
choice = input("")
#choices
if choice == "1":
    choice1 = "You enter the wooden door and before you lays a dark misty woodland path. You hear a faint howl"
elif choice == "2":
    choice2 = "You enter the stone door and before you lays a dark damp cave. It smells of mold"

#------------------------------------------------------------------------------------
#                                                                                   |
#    made to create story paths based off the play returning to the start :return   |
#                                                                                   |
#------------------------------------------------------------------------------------

print("Choose a door")
print("1. Wood")
print("2. Stone")
choice = input("")
#choices
if choice == "1":
    choice1 = "You enter the wooden door and before you lays a dark misty woodland path. You hear a faint howl"
elif choice == "2":
    choice2 = "You enter the stone door and before you lays a dark damp cave. It smells of mold"

#------------------------------------------------------------------------------------
#                                                                                   |
#                                   start of path :start1                           |
#                                                                                   |
#------------------------------------------------------------------------------------
print(choice1)
print("1. Press onward")
print("2. Return")
choice = input("")
#choices
if choice == "1":
    choice1_1 = "You follow the woodland path and find a clearing. You feel as though you're being watched"
elif choice == "return":
    choiceR = "You return to the dark room. It's just as boring as you remember"

#------------------------------------------------------------------------------------
#
#                                   |path 1 part 1| 1:1
#
#------------------------------------------------------------------------------------
print(choice1_1)
print("as you approach the end of the woodland path and find a large tree with a strange symbol engraved on a door built into the front of the tree it's surrounded by a circle pathway dug into the dirt")
print("1. Enter the tree")
print("2. examine the tree")
choice = input("")
#choices
if choice == "1":
    choice1_2 = "You enter the door it is remarkably heavy"
if choice == "2":
    choice1_1_1_1 = ""
elif choice == "return":
    choiceR = "You return to the dark room. It's just as boring as you remember"
#------------------------------------------------------------------------------------
#                               |path 1 part 1 branch 1 part 1| 1:1;1/1
#------------------------------------------------------------------------------------
print(choice1_1_1_1)
print("you look closely at the strange symbol it seems to be a intracately carved large tree with 4 branches surounded by an ring with tribal spirals and knots")
print("1.")
print("2.")
choice = input("")
#choices
if choice == "1":
    choice = ""
elif choice == "2":
    choice1_2 = "You enter the door it is remarkably heavy"
elif choice == "3":
    choice1_1_1_2 = ""
elif choice == "return":
    choiceR = "You return to the dark room. It's just as boring as you remember"
#------------------------------------------------------------------------------------
#                             |path 1 part 1 branch 1 part 2| 1:1;1/2
#------------------------------------------------------------------------------------
print(choice1_1_1_2)
print("")
print("1.")
print("2.")
choice = input("")
#choices
if choice == "1":
    choice1_2 = "You enter the door it is remarkably heavy"
elif choice == "return":
    choice1_1_1_3 = ""
elif choice == "return":
    choiceR = "You return to the dark room. It's just as boring as you remember"
#------------------------------------------------------------------------------------
#                             |path 1 part 1 branch 1 part 3| 1:1;1/3
#------------------------------------------------------------------------------------
print(choice1_1_1_3)
print("")
print("1.")
print("2.")
choice = input("")
#choices
if choice == "2":
    choice1_2 = "You enter the door it is remarkably heavy"
elif choice == "return":
    choiceR = "You return to the dark room. It's just as boring as you remember"
#------------------------------------------------------------------------------------
#
#                                  |path 1 part 2| 1:2
#
#------------------------------------------------------------------------------------
print(choice1_2)
print("1. Descend")
print("2. Return")
print("3. Return")
choice = input("")
#choices
if choice == "1":
    choice1_3 = "You find yourself in a room with a table and a chest. The room is lit by a single candle and decorated by many pelts and animal heads" 
elif choice == "return":
    choiceR = "You return to the dark room. It's just as boring as you remember"
#------------------------------------------------------------------------------------
#
#                                   |path 1 part 3| 1:3
#
#------------------------------------------------------------------------------------
print(choice1_3)
print("1. Open the chest")
print("2. Leave the chest alone")
choice = input("")
#choices
if choice == "1":
    print("You find a key inside the chest. It looks old and worn")
elif choice == "2":
    print("You leave the chest alone and take a look around the room")
elif choice == "return":
    choiceR = "You return to the dark room. It's just as boring as you remember"

#------------------------------------------------------------------------------------
#                                                                                   |
#                                   start of path 2 :start2                         |
#                                                                                   |
#------------------------------------------------------------------------------------
print(choice2)
print("1. Press onward")
print("2. Return")
choice = input("")
#choices
if choice == "1":
    choice2_1 = "You follow the cave path and find a chamber. You feel a gust of cold air"
elif choice == "return":
    choiceR = "You return to the dark room. It's just as boring as you remember"

#------------------------------------------------------------------------------------
#                                   |path 2 part 1| 2:1
#------------------------------------------------------------------------------------
print(choice2_1)
#choices
choice = input("")
if choice == "1":
    choice2_2 = "" 
elif choice == "return":
    choiceR = "You return to the dark room. It's just as boring as you remember"
#------------------------------------------------------------------------------------
#                                   |path 2 part 2| 2:2
#------------------------------------------------------------------------------------
print(choice2_2)
print("1. Descend")
print("2. Return")
choice = input("")
#choices
if choice == "1":
    choice2_3 = "" 
elif choice == "return":
    choiceR = "You return to the dark room. It's just as boring as you remember"
#------------------------------------------------------------------------------------
#                                   |path 2 part 3| 2:3
#------------------------------------------------------------------------------------
print(choice2_3)
print("You find yourself in a room with a table apon which is a small stone box. The room is lit by a single candle")
print("1. Open the Box")
print("2. Contiune")
print("Return")
choice = input("")
if choice == "1":
    print("You find a key inside the box. It looks old and worn")
elif choice == "2":
    choice2_3_1 = "You leave the chest alone and take a look around the room"
elif choice == "return":
    choiceR = "You return to the dark room. It's just as boring as you remember"
#------------------------------------------------------------------------------------
#                               |path 2 part 3 branch 1| 2:3;1
#------------------------------------------------------------------------------------
print(choice2_3)
print("")
print("1.")
print("2.")
print("Return")
choice = input("")
if choice == "1":
    print("")
elif choice == "2":
    print("")
    choice2_3_1 = ""
elif choice == "return":
    choiceR = "You return to the dark room. It's just as boring as you remember"

#------------------------------------------------------------------------------------

