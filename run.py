class ChernobylSurvivalGame:
    def __init__(self):
        pass
    
    def game_introduction(self):
        """
        Function to introduce the game and ask the user if they would like to play.
        """
        play_decision = input("Would you like to play? (yes/no)\n")
        if play_decision.lower().strip() == "yes":
            self.start_zone()
        else:
            print("Understood, you are not ready for the challenge...")
    
    def start_zone(self):
        print("As you slowly regain consciousness, the world around you comes into focus.\n The air feels heavy, carrying a sense of decay and abandonment.\nYou find yourself lying on the cold, damp ground, surrounded by the remnants of what was once a bustling town.\n")
        player_name = input("Can you remember your name? (Enter name)").strip()
        print(f"Good luck surviving the apocalypse {player_name}\n")
        print("As you rise to your feet, a mixture of awe and unease fills your heart.\nThe haunting silence and eerie atmosphere of the exclusion zone envelop you.\nNature has reclaimed its territory, with overgrown vegetation and crumbling structures standing as testament to the past.\n")
        while True:
            print(f"So {player_name}, which way would you like to head first?\n")
            directions = ["north", "east", "south", "west"]
            player_input = input("Options: north/south/east/west").lower().strip()
            if player_input == "north":
                self.power_plant()
                break
            elif player_input == "east":
                self.forest()
                break
            elif player_input == "south":
                self.city()
                break
            elif player_input == "west":
                self.hospital()
                break
            else:
                print("Have you forgotten how to spell too? Enter a valid direction...")
    
    def power_plant(self):
        print("Hello, you have reached the power plant.")
    
    def forest(self):
        print("Hello, you have reached the forest.")
    
    def city(self):
        print("Hello, you have reached the city.")
    
    def hospital(self):
        print("Hello, you have reached the hospital.")
        

# Instantiate the game object and run the game
game = ChernobylSurvivalGame()
game.game_introduction()
