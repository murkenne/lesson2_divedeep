'''You are provided with a Python script that is supposed to 
guide a user through an adventure game, but it has some errors. Identify adn fix them.
'''
place = input("Choose a place: (forest or cave) ? ")

if place == "forest":
    action = input("climb a tree or cross a river? ")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else:
        pass # Handle invalid action
elif place == "cave":
    action = input("light a torch or proceed in the dark? ")
    if action == "light a torch":
        print("The path of the cave is visible")
    elif action == "proceed in the dark":
        print("Tread carefully for the cave is too dark!")
    else:
        print("Invalid action chosen.")
else:
    pass # Handle invalid action

