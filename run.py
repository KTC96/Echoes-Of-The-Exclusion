def game_introduction():
    """
    Function to introduce the game and ask the user if they would like to play.
    """
    play_decision = input("Would you like to play? (yes/no)\n")
    if play_decision.lower().strip() == "yes":
        start_zone()
    else:
        print("Understood, you are not ready for the challenge...")


def start_zone():
    print("As you slowly regain consciousness, the world around you comes into focus.\n The air feels heavy, carrying a sense of decay and abandonment.\nYou find yourself lying on the cold, damp ground, surrounded by the remnants of what was once a bustling town.\n")
    player_name = input("Can you remember your name? (Enter name)").strip()
    print(f"Good luck surviving the apocalypse {player_name}\n")
    print("As you rise to your feet, a mixture of awe and unease fills your heart.\nThe haunting silence and eerie atmosphere of the exclusion zone envelop you.\nNature has reclaimed its territory, with overgrown vegetation and crumbling structures standing as testament to the past.\n")
    print(f"So {player_name}, which way would you like to head first?\n")
    while True:
        directions = ["north", "east", "south", "west"]
        player_input = input("Options: north/south/east/west").lower().strip()
        if player_input == "north":
            power_plant()
            break
        elif player_input == "east":
            forest()
            break
        elif player_input == "south":
            city()
            break
        elif player_input == "west":
            hospital()
            break
        else:
            print("Have you forgotten how to spell too? Enter a valid direction...")


def power_plant():
    print("Hello, you have reached the power plant.")


def forest():
    print("Hello, you have reached the forest.")


def city():
    print("Hello, you have reached the city.")


def hospital():
    print("Hello, you have reached the hospital.")


while True:
    game_introduction()
    break
