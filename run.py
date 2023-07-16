def game_introduction():
    """
    Function to introduce the game and ask the user if they would like to play.
    """
    play_decision = input("Would you like to play? (yes/no)")
    if play_decision.lower().strip() == "yes":
        start_zone()
    else:
        print("Understood, you are not ready for the challenge...")

        
def start_zone():
        print("As you slowly regain consciousness, the world around you comes into focus.\n The air feels heavy, carrying a sense of decay and abandonment.\nYou find yourself lying on the cold, damp ground, surrounded by the remnants of what was once a bustling town.\n")
        player_name = input("Can you remember your name? (Enter name)").strip()
        print(f"Good luck surviving the apocalypse {player_name}\n")
        print("As you rise to your feet, a mixture of awe and unease fills your heart.\nThe haunting silence and eerie atmosphere of the exclusion zone envelop you.\nNature has reclaimed its territory, with overgrown vegetation and crumbling structures standing as testament to the past.\n")
        print(f"So {player_name}, which way would you like to head first?")
        directions = ["north", "east", "south","west"]
        player_input =""
        input("Options: north/south/east/west")
        if player_input == "north":
            power_plant()
        elif player_input == "east":
            forest()
        elif player_input == "south":
            city()
        elif player_input == "west":
            hospital()
        else: 
            print("Have you forgotten how to spell too? Enter a valid direction...")
        

       
        



game_introduction()
