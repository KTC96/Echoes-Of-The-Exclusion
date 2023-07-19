from enum import Enum

class Direction(Enum):
    """
    Enum "constant" class for holidng values for directions in the game
    """
    
    NORTH = 'N'
    EAST = 'E'
    SOUTH = 'S'
    WEST = 'W'

class Decisions(Enum):
    """
    Enum "constant" class for holding Y/N decisions in the game
    """

    YES = 'Y'
    NO = 'N'
    SANCTUM = 'SANCTUM'

#class Player_info(Enum):

class ChernobylSurvivalGame:
    def __init__(self):
        pass

    def get_user_input(self, prompt, valid_options):
        """
        Utility function to validate and return user input
        """
        while True:
            user_input = input(prompt).upper().strip()
            if user_input in valid_options:
                return user_input
            else:
                print("Have you forgotten how to spell too? Try again...")

    def game_introduction(self):
        """
        Asks the player if they want to play or not
        """
        while True:
            decision = self.get_user_input("Would you like to play? (Y/N)\n", [Decisions.YES.value, Decisions.NO.value])
            match decision:
                case Decisions.YES.value:
                    self.start_zone()
                    break
                case Decisions.NO.value:
                    print("Understood, you are not ready for the challenge...")
                    break
                
    def get_player_name(self):
        return input("Can you remember your name? (Enter name)\n").strip()

    def start_zone(self):
        print("As you slowly regain consciousness, the world around you comes into focus.\n The air feels heavy, carrying a sense of decay and abandonment.\nYou find yourself lying on the cold, damp ground, surrounded by the remnants of what was once a bustling town.\n")
        self.player_name_input = self.get_player_name()
        print(f"Good luck surviving the apocalypse {self.player_name_input}\n")
        print("As you rise to your feet, a mixture of awe and unease fills your heart.\nThe haunting silence and eerie atmosphere of the exclusion zone envelop you.\nNature has reclaimed its territory, with overgrown vegetation and crumbling structures standing as testament to the past.\n")
        print(f"So {self.player_name_input}, which way would you like to head first?\n")
        while True:
            player_input = self.get_user_input("Options: N/E/S/W\n", [d.value for d in Direction])
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
               

    def start_zone_return(self):
        print("You return to where you started, not much has changed...")
        print(f"So {self.player_name_input}, which way would you like to head?\n")

        while True:
            player_input =  self.get_user_input("Options: N/E/S/W\n", [d.value for d in Direction])
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

    def power_plant(self):
        print("The heart of the disaster, the abandoned power plant looms in the distance, its towering smokestacks and crumbling reactors a haunting reminder of the catastrophic event. It emits an unsettling aura, and caution is advised when venturing too close.\n")
        while True:
            power_plant_input = input("You see something scuttling in the shadows, do you investigate? (Y/N)\n").upper().strip()
            match power_plant_input:
                case Decisions.YES.value:
                    self.monster_fight()
                    break
                case Decisions.NO.value:
                    self.return_to_start_zone()
                    break

    def monster_fight(self):
        print("monster fight")
       

    def return_to_start_zone(self):
        print(f"So {self.player_name_input}, which way would you like to head?\n")
        while True:
            player_input = self.get_user_input("Options: S\n", [d.value for d in Direction])
            match player_input:
                case Direction.SOUTH.value:
                    self.start_zone_return()
                    break

    def forest(self):
        print("You have walked beyond the city limits to a dense forest tainted by radiation. The trees stand twisted and sickly, their leaves discolored and wilted. The air is heavy with an acrid smell, and eerie glowing fungi dot the forest floor, casting an otherworldly glow.\n")
        print("Walking through the forest, you hear a mysterious sound coming from deep within, what do you do?")
        while True:
            forest_decision =  input("Options: Follow the sound, explore the forest, build a shelter (1,2,3) or head back (W)\n").upper().strip()
            match forest_decision:
                case "1":
                    self.cave()
                    break
                case "2":
                    print("field")
                    break
                case "3":
                    print("clue")
                    break
                case "W":
                    self.start_zone_return()
                case _:
                    print("Have you forgotten how to spell too? Try again...")
                    


    def city(self):
        print("Hello, you have reached the city.")

    def hospital(self):
        print("Hello, you have reached the hospital.")

    def cave(self):
        print("As the player follows the mysterious sound deeper into the forest, they discover a hidden cave adorned with ancient symbols and an underground waterfall\n")
        cave_input = self.get_user_input("Do you venture behind the waterfall?",[Decisions.YES.value, Decisions.NO.value])
        match cave_input:
                case Decisions.YES.value:
                    print("You see a large symbol, I wonder what it could mean?" )
                    self.symbol()
                    secret_input = input(""),[Decisions.SANCTUM.value]
                    match secret_input:
                        case Decisions.SANCTUM.value:
                            print("The symbol seems to glow faintly and you suddenly notice a passage that you swear was not there before, you crawl through to be met patrolling soldier on the other side\n ")
                            #self.win_game()
                        case _:
                            print("That did not seem to do anything, if only you could work out the symbols meaning...\n")
                            self.cave()
                            
                case Decisions.NO.value:
                            print()
                            self.forest()
               
                    
                
    def symbol(self):
        symbol = """
                 /\\
                /  \\
               /  ^ \\
              /   ^  \\
              \\  ^  //
               \\ ^ //
                \\ //
                 """
        print(symbol)
# Instantiate the game object and run the game
game = ChernobylSurvivalGame()
game.game_introduction()
