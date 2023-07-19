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
    ONE = "1"
    TWO = "2"
    THREE = "3"
    CODE = "survivor"

class ChernobylSurvivalGame:
    def __init__(self):
        self.radiation_level = 0
        self.weapon = False

    def player_info(self):

        
        if self.radiation_level >= 3:
            self.radiation_death()
    

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
            forest_decision =  self.get_user_input("Options: Follow the sound, explore the forest, build a shelter (1,2,3) or head back (W)\n",  [Decisions.ONE.value, Decisions.TWO.value, Decisions.THREE.value, Direction.WEST.value])
            match forest_decision:
                case "1":
                    self.cave()
                    break
                case "2":
                    self.field()
                    break
                case "3":
                    self.fenced_area()
                    break
                case "W":
                    self.start_zone_return()
                case _:
                    print("Have you forgotten how to spell too? Try again...")
                    
    def cave(self):
        print("As the player follows the mysterious sound deeper into the forest, they discover a hidden cave adorned with ancient symbols and an underground waterfall\n")
        cave_input = self.get_user_input("Do you venture behind the waterfall?",[Decisions.YES.value, Decisions.NO.value])
        match cave_input:
                case Decisions.YES.value:
                    
                    self.symbol()
                    secret_input = input("You see a large symbol, I wonder what it could mean?").upper().strip()
                    match secret_input:
                        case Decisions.SANCTUM.value:
                            print("The symbol seems to glow faintly and you suddenly notice a passage that you swear was not there before, you crawl through to be met patrolling soldier on the other side\n ")
                            self.win_game()
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

    def field(self):
        print("As you explore further, you stumble upon a vast open field, amidst the swaying grass and gentle breeze, you an old and dirty radio...\n ")
        print("It comes to life sporadically, revealing a faint but unmistakable voice— a survivor's log, Day 34. The survivor cryptically hints about a weapon crucial for survival, concealed within a safe in a nearby apartment building...")
        self.forest()

    def fenced_area(self):
        radiation_zone = self.get_user_input("While collecting wood to make yourself a sheleter, you come across a fenced off area with a symbol stating 'DO NOT ENTER RADIATION RISK'Do you enter?(Y/N)\n", [Decisions.YES.value, Decisions.NO.value])
        match radiation_zone:
            case Decisions.YES.value:
                print("You start to feel a buzzing sound rattling inside of your skull, maybe the sign was right. You drop the wood you gathered and return to the forest +2 radiation level\n")
                self.radiation_level += 2
                self.player_info()
                self.forest()
            case Decisions.NO.value:
                print("You return to the forest and make a comfortable shelter for the night. Radiation levels reset to 0\n")
                self.radiaiton_level = 0
                self.forest()

    def city(self):
        print("You have reached the City Center. Once a bustling metropolis, the city now stands in ruins, its buildings crumbling and overgrown with vegetation. The eerie silence is broken only by the haunting howl of the wind, and the streets are littered with debris and remnants of human civilization...\n")
        city_decision = self.get_user_input("Options: Head towards the apartment complex, go to the exclusion zone limit, head to the library (1,2,3) or head back (N)", [Decisions.ONE.value, Decisions.TWO.value, Decisions.THREE.value, Direction.NORTH.value])
        match city_decision:
            case Decisions.ONE.value:
                self.apartment()
            case Decisions.TWO.value:
                print("mine field")
            case Decisions.THREE.value:
                print("library")
            case Direction.NORTH.value:
                self.start_zone_return()
    
    def apartment(self):
        print("As you explore the complex, you notice several rooms with open doors, revealing remnants of the past - scattered belongings, overturned furniture, and broken memories. Some rooms are completely dark, and you can only imagine what lies within. However, one particular room catches your attention. A faint light seeps out from beneath the door, hinting at something inside.\n")
        print("You open the door and find a safe, with a strange alphabetized lock, if only you knew the code...\n")
        safe_code_input = input("Enter the code:")
        match safe_code_input:
            case Decisions.CODE.value:
               print("The safe unlocks with a dull thud, inside you discover a handgun, this is sure to help your survival.")
               self.weapon = True
               self.city()
            case _:
                print("that was not correct")
                self.apartment()
                
                
                
               



    def hospital(self):
        print("Hello, you have reached the hospital.")

    def win_game(self):
        print("Congratulations! You have successfully navigated through the treacherous Chernobyl Exclusion Zone, overcoming countless challenges and unearthing ancient mysteries. With determination and wit, you have survived the apocalypse and emerged as a true survivor. The world may have changed, but your resilience and bravery have stood the test of time. You are now hailed as a legend, the one who conquered the Zone and unlocked its deepest secrets. Your name will be remembered for generations to come, and your journey will forever be etched in history. Well done, champion of the Echoes of the Exclusion!")
        self.game_introduction()

    def radiation_death(self):
        print("Your radiation exposure has exceeded the critical level, your body weakens, annd you succumb to the deadly effects, leaving the Exclusion Zone as your final resting place.")
        self.game_introduction()
# Instantiate the game object and run the game
game = ChernobylSurvivalGame()
game.game_introduction()
