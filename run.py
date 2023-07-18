import enum
player_weapon = False

class Direction(enum.Enum):
    NORTH = 'N'
    EAST = 'E'
    SOUTH = 'S'
    WEST = 'W'

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
                
    def player_name(self):
        return input("Can you remember your name? (Enter name)\n").strip()
           


    def start_zone(self):
        print("As you slowly regain consciousness, the world around you comes into focus.\n The air feels heavy, carrying a sense of decay and abandonment.\nYou find yourself lying on the cold, damp ground, surrounded by the remnants of what was once a bustling town.\n")
        self.player_name = self.player_name()
        print(f"Good luck surviving the apocalypse {self.player_name}\n")
        print("As you rise to your feet, a mixture of awe and unease fills your heart.\nThe haunting silence and eerie atmosphere of the exclusion zone envelop you.\nNature has reclaimed its territory, with overgrown vegetation and crumbling structures standing as testament to the past.\n")
        while True:
            print(f"So {self.player_name}, which way would you like to head first?\n")
            player_input = input("Options: N/E/S/W").upper().strip()

            if player_input == Direction.NORTH.value:
                self.power_plant()
                break
            elif player_input == Direction.EAST.value:
                self.forest()
                break
            elif player_input == Direction.SOUTH.value:
                self.city()
                break
            elif player_input == Direction.WEST.value:
                self.hospital()
                break
            else:
                print("Have you forgotten how to spell too? Enter a valid direction...")
                
    
    def start_zone_return(self):
        
            print("You return to where you started, not much has changed...")
            print(f"So {self.player_name}, which way would you like to head?\n")
            while True:
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
        power_plant_input = input("You see something scuttling in the shadows, do you investigate? (Y/N)\n").lower().strip()
        while True:
            if power_plant_input == "yes":
                print("monster fight")
                """
                Add logic later
                if player_weapon == True:
                    print("You kill monster and win the game")
                else:
                    print("you die")
                    """
                
            elif power_plant_input == "no":
                directions = ["south"]
                print(f"So {self.player_name}, which way would you like to head?\n")
                direction_input = input("Options: south").lower().strip()
                if direction_input == "south":
                    self.start_zone_return()
                    break
                else:
                    print("Have you forgotten how to spell too? Enter a valid direction...")
                    
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
