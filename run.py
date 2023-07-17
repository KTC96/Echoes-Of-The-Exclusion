class ChernobylSurvivalGame:
    def __init__(self):
        pass
    
    def game_introduction(self):
        """
        Function to introduce the game and ask the user if they would like to play.
        """
        while True:
            play_decision = input("Would you like to play? (yes/no)\n")
            if play_decision.lower().strip() == "yes":
                self.start_zone()
                break
            elif play_decision.lower().strip() == "no":
                print("Understood, you are not ready for the challenge...")
                break
            else:
                print("I did not understand that")
                
                
                
    
    def start_zone(self):
        print("As you slowly regain consciousness, the world around you comes into focus.\n The air feels heavy, carrying a sense of decay and abandonment.\nYou find yourself lying on the cold, damp ground, surrounded by the remnants of what was once a bustling town.\n")
        player_name = input("Can you remember your name? (Enter name)\n").strip()
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
        print("The heart of the disaster, the abandoned power plant looms in the distance, its towering smokestacks and crumbling reactors a haunting reminder of the catastrophic event. It emits an unsettling aura, and caution is advised when venturing too close.\n")
        power_plant_input = input("You see something scuttling in the shadows, do you investivate? (Y/N)\n").lower().strip()
        while True:
            if power_plant_input =="Y":
                print("monster fight")
            elif power_plant_input =="N":
                print(f"So {player_name}, which way would you like to head?\n")
                player_input = input("Options: south").lower().strip()
            else: 
                print("Have you forgotten how to spell too? Enter a valid direction...")

            
      
    
    def forest(self):
        print("Hello, you have reached the forest.")
    
    def city(self):
        print("Hello, you have reached the city.")
    
    def hospital(self):
        print("Hello, you have reached the hospital.")
        

# Instantiate the game object and run the game
game = ChernobylSurvivalGame()
game.game_introduction()
