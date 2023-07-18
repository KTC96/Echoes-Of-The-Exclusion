import enum
player_weapon = False

class Direction(enum.Enum):
    NORTH = 'N'
    EAST = 'E'
    SOUTH = 'S'
    WEST = 'W'

class Decisions(enum.Enum):
    YES = 'Y'
    NO = 'N'

class ChernobylSurvivalGame:
    def __init__(self):
        pass
    
    def game_introduction(self):
        """
        Function to introduce the game and ask the user if they would like to play.
        """
        while True:
            decision = input("Would you like to play? (Y/N)\n").upper().strip()
            match decision:
                case Decisions.YES.value:
                    self.start_zone()
                    break
                case Decisions.NO.value:
                    print("Understood, you are not ready for the challenge...")
                    break
                case _:
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

            match player_input: 
                case Direction.NORTH.value:
                    self.power_plant()
                    break
                case Direction.EAST.value:
                    self.forest()
                    break
                case Direction.SOUTH.value:
                    self.city()
                    break
                case Direction.WEST.value:
                    self.hospital()
                    break
                case _:
                    print("Have you forgotten how to spell too? Enter a valid direction...")
                
    
    def start_zone_return(self):
        print("You return to where you started, not much has changed...")
        print(f"So {self.player_name}, which way would you like to head?\n")

        while True:
            player_input = input("Options: N/E/S/W").upper().strip()
            match player_input: 
                case Direction.NORTH.value:
                    self.power_plant()
                    break
                case Direction.EAST.value:
                    self.forest()
                    break
                case Direction.SOUTH.value:
                    self.city()
                    break
                case Direction.WEST.value:
                    self.hospital()
                    break
                case _:
                    print("Have you forgotten how to spell too? Enter a valid direction...")

    
    def power_plant(self):
        print("The heart of the disaster, the abandoned power plant looms in the distance, its towering smokestacks and crumbling reactors a haunting reminder of the catastrophic event. It emits an unsettling aura, and caution is advised when venturing too close.\n")
        power_plant_input = input("You see something scuttling in the shadows, do you investigate? (Y/N)\n").lower().strip()
        while True:
            match power_plant_input:
                case Decisions.YES.value:
                    print("monster fight")
                    """
                    Add logic later
                    if player_weapon == True:
                        print("You kill monster and win the game")
                     else:
                        print("you die")
                    """

                case Decisions.NO.value:
                    print(f"So {self.player_name}, which way would you like to head?\n")
                    player_input = input("Options: S").lower().strip()
                    match player_input:
                        case Direction.SOUTH.value:
                            self.start_zone_return()
                            break
                        case _:
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
