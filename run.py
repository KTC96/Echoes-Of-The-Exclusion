import os
from enum import Enum

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

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
    #SANCTUM = 'SANCTUM'
    ONE = "1"
    TWO = "2"
    THREE = "3"
    #CODE = "survivor"
    RETURN = 'R'

from enum import Enum

# Your Direction and Decisions enums here...

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

    def return_to_location(self, location):
        return_input = self.get_user_input(f"To return to {location}, enter R: ", [Decisions.RETURN.value])
        if return_input == Decisions.RETURN.value:
            location_func()


    def return_to_location(self, location_name):
        return_input = self.get_user_input(f"To return to {location_name}, enter R: ", [Decisions.RETURN.value])
        match return_input:
            case Decisions.RETURN.value:
                match location_name:
                    case "forest":
                        self.forest()
                    case "city":
                        self.city()
                    case "hospital":
                        self.hospital()
                    case "start_zone":
                        self.start_zone_return()

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
        clear_screen()
        print(f"Good luck surviving the apocalypse {self.player_name_input}\n")
        print("As you rise to your feet, a mixture of awe and unease fills your heart.\nThe haunting silence and eerie atmosphere of the exclusion zone envelop you.\nNature has reclaimed its territory, with overgrown vegetation and crumbling structures standing as testament to the past.\n")
        
        print(f"So {self.player_name_input}, which way would you like to head first?\n")
     
        start_direction_map = {
                Direction.NORTH.value: self.power_plant,
                Direction.EAST.value: self.forest,
                Direction.SOUTH.value: self.city,
                Direction.WEST.value: self.hospital
        }

        while True:
            start_direction = self.get_user_input("Options: N/E/S/W", start_direction_map.keys())
            start_direction_map[start_direction]()

               
    def start_zone_return(self):
        clear_screen()
        print("You return to where you started, not much has changed...")
        print(f"So {self.player_name_input}, which way would you like to head?\n")

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


    def power_plant(self):
        clear_screen()
        print("The heart of the disaster, the abandoned power plant looms in the distance, its towering smokestacks and crumbling reactors a haunting reminder of the catastrophic event. It emits an unsettling aura, and caution is advised when venturing too close.\n")
        while True:
            power_plant_input = input("You see something scuttling in the shadows, do you investigate? (Y/N)\n").upper().strip()
            match power_plant_input:
                case Decisions.YES.value:
                    self.monster_fight()
                    break
                case Decisions.NO.value:
                    self.start_zone_return
                    break

    def monster_fight(self):
        clear_screen()
        print("monster fight")
    

    def forest(self):
        clear_screen()
        print("You have walked beyond the city limits to a dense forest tainted by radiation. The trees stand twisted and sickly, their leaves discolored and wilted. The air is heavy with an acrid smell, and eerie glowing fungi dot the forest floor, casting an otherworldly glow.\n")
        print("Walking through the forest, you hear a mysterious sound coming from deep within, what do you do?")
         
        forest_decision_map = {
            Decisions.ONE.value: self.cave,
            Decisions.TWO.value: self.field,
            Decisions.THREE.value: self.fenced_area,
            Direction.WEST.value: self.start_zone_return
        }

        while True:
            forest_decision = self.get_user_input("Options: Follow the sound, explore the forest, build a shelter (1,2,3) or head back (W)\n", forest_decision_map.keys())
            forest_decision_map[forest_decision]()
                    
    def cave(self):
        clear_screen()
        print("As you follow the mysterious sound deeper into the forest, you discover a hidden cave adorned with ancient symbols and an underground waterfall\n")
        print("You see a large symbol, I wonder what it could mean?")
        self.symbol()
        secret_input = input("???").upper().strip()
        match secret_input:
            case "SANCTUM":
                print("The symbol seems to glow faintly and you suddenly notice a passage that you swear was not there before, you crawl through to be met patrolling soldier on the other side\n ")
                self.win_game()
            case _:
                print("That did not seem to do anything, if only you could work out the symbols meaning...\n")
                

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

    def symbol2(self):
        symbol2 = """
                 /\\
                /  \\
               /  * \\
              /   *  \\
              \\  *  //
               \\ * //
                \\ //
                 """
        print(symbol2)

    def symbol3(self):
        symbol3 ="""
                 /\\
                /  \\
               /  | \\
              /   ^  \\
              \\  |  //
               \\ ^ //
                \\ //
                 """
        print(symbol3)

    

    def field(self):
        clear_screen()
        print("As you explore further, you stumble upon a vast open field, amidst the swaying grass and gentle breeze, you an old and dirty radio...\n ")
        print("It comes to life sporadically, revealing a faint but unmistakable voice— a survivor's log, Day 34. The survivor cryptically hints about a weapon crucial for survival, concealed within a safe in a nearby apartment building...")
        

    def fenced_area(self):
        
        radiation_zone = self.get_user_input("While collecting wood to make yourself a sheleter, you come across a fenced off area with a symbol stating 'DO NOT ENTER RADIATION RISK'Do you enter?(Y/N)\n", [Decisions.YES.value, Decisions.NO.value])
        match radiation_zone:
            case Decisions.YES.value:
                print("You start to feel a buzzing sound rattling inside of your skull, maybe the sign was right. You drop the wood you gathered and return to the forest +2 radiation level\n")
                self.radiation_increase(2)
                self.forest()
            case Decisions.NO.value:
                print("You return to the forest and make a comfortable shelter for the night. Radiation points decresed by 1\n")
                self.radiation_decrease(1)
                self.forest()

    def city(self):
        clear_screen()
        print("You have reached the City Center. Once a bustling metropolis, the city now stands in ruins, its buildings crumbling and overgrown with vegetation. The eerie silence is broken only by the haunting howl of the wind, and the streets are littered with debris and remnants of human civilization...\n")

        city_decision_map= {
            Decisions.ONE.value: self.apartment,
            Decisions.TWO.value: self.mine_field,
            Decisions.THREE.value: self.library,
            Direction.NORTH.value: self.start_zone_return}

        while True:
            city_decision = self.get_user_input("Options: Head towards the apartment complex, go to the exclusion zone limit, head to the library (1,2,3) or head back (N)",city_decision_map.keys())
            city_decision_map[city_decision]()
    
    def apartment(self):
        
        print("As you explore the complex, you notice several rooms with open doors, revealing remnants of the past - scattered belongings, overturned furniture, and broken memories. Some rooms are completely dark, and you can only imagine what lies within. However, one particular room catches your attention. A faint light seeps out from beneath the door, hinting at something inside.\n")
        print("You open the door and find a safe, with a strange alphabetized lock, if only you knew the code...\n")
        safe_code_input = input("Enter the code: ")
        match safe_code_input:
            case "survivor":
               print("The safe unlocks with a dull thud, inside you discover a handgun, this is sure to help your survival.")
               self.weapon = True
               self.city()
               
            case _:
                print("That was not correct\n")
                self.city()

    def library(self):
        
        print(" Upon entering the Library you are covered in radioactive dust, lets hope this is worth it (+1 radiation point)\n")
        self.radiation_increase(1)
        print("Inside, the dimly lit space is filled with dusty books and scattered notes, hinting at the knowledge it holds. As you explore, you come across a cryptic diary with the following symbols and text:\n")
        self.symbol2()
        print("HOPE\n")
        self.symbol3()
        print("REFUGE\n")
        self.symbol()
        print("SANCTUM\n")
        print("I wonder what those strange symbols could mean?\n")
        return_to_city = self.get_user_input("Return to the city? (Y)",[Decisions.YES.value])
        match return_to_city:
            case Decisions.YES.value:
                self.city()
            
    def mine_field(self):
        
        print("As you venture toward the outer limits of the city, you spot a menacing sight: a treacherous minefield stretching before you. Warning signs adorned with skull symbols and bold letters caution against entering. The air feels tense, and you can sense the lurking danger that lies ahead.")
        enter_mine_field  = self.get_user_input("Enter the minefield? (Y/N)",[Decisions.YES.value, Decisions.NO.value])
        match enter_mine_field:
            case Decisions.YES.value:
                self.death()
            case Decisions.NO.value:
                print("Surely the city must be safer...\n")
                self.city()

    def hospital(self):
        clear_screen()
        print("You arrive at the abandoned hospital, once a place of healing and hope. Now, it stands as a haunting reminder of the past. Broken windows and overgrown ivy greet you as you step inside. The scent of decay lingers in the air, and eerie silence fills the halls.\n")
        
        hospital_decision_map= {
            Decisions.ONE.value: self.hospital_office,
            Decisions.TWO.value: self.operating_room,
            Decisions.THREE.value: self.basement,
            Direction.EAST.value: self.start_zone_return}

        while True:
            hospital_decision = self.get_user_input("Options: Search the Hospital offices, Explore the operating room, Decend into the basement (1,2,3) or head back (E) ",hospital_decision_map.keys())
            hospital_decision_map[hospital_decision]()

    def hospital_office(self):
        
        print("Upon entering the abandoned hospital offices, you are startled by a chilling sight: a mutated dog lurking in the shadows. Its disfigured appearance and haunting howls evoke terror ")
        enter_office  = self.get_user_input("Search the office? (Y/N)",[Decisions.YES.value, Decisions.NO.value])
        match enter_office:
            case Decisions.YES.value:
                clear_screen()
                print("You manage to sneak past the mutated dog by distracting by throwing a clipboard into another room. There dosn't seem to be much in the office other than a piece of paper with the words 'Narcotic aid' scribbled on them, could it be an anagram...\n")
                #maybe implement damage feature
                self.return_to_location("hospital")
                
            case Decisions.NO.value:
                clear_screen()
                print("That seems like the right choice...\n")
                self.return_to_location("hospital")


    def operating_room(self):
        clear_screen()
        print("You cautiously enter the operating room, and the pungent stench of decay assaults your senses. Your eyes widen as you come face to face with a ghastly sight – a rotting corpse lies on the operating table, remnants of a medical procedure long abandoned.")
        search_body = self.get_user_input("Search the corpse? (Y/N)",[Decisions.YES.value, Decisions.NO.value])
        match search_body:
            case Decisions.YES.value:
                clear_screen()
                print("You search the corpse to discover a syringe labelled 'Antiradioactive particles (-2 radiation points)\n")
                self.radiation_decrease(2)
                self.return_to_location("hospital")

            case Decisions.NO.value:
                clear_screen()
                print("Who knows what diseases that body could have had...\n")
                self.return_to_location("hospital")
   


    def basement(self):
        clear_screen()
        print("There does not seem to be much down here except from radioactive dust (+1 radiation point)")
        self.radiation_increase(1)
        self.return_to_location("hospital")

    def return_to_hospital(self):
        match return_to_hosptial:
            case Decisions.RETURN.value:
                self.return_to_location("hospital")


    def win_game(self):
        clear_screen()
        print("Congratulations! You have successfully navigated through the treacherous Chernobyl Exclusion Zone, overcoming countless challenges and unearthing ancient mysteries. With determination and wit, you have survived the apocalypse and emerged as a true survivor. The world may have changed, but your resilience and bravery have stood the test of time. You are now hailed as a legend, the one who conquered the Zone and unlocked its deepest secrets. Your name will be remembered for generations to come, and your journey will forever be etched in history. Well done, champion of the Echoes of the Exclusion!")
        self.game_introduction()

    def radiation_death(self):
        clear_screen()
        print("Your radiation exposure has exceeded the critical level, your body weakens, and you succumb to the deadly effects, leaving the Exclusion Zone as your final resting place.")
        self.game_introduction()
    
    def death(self):
        clear_screen()
        print("That was not a wise decision. Your journey in the Exclusion Zone has come to a tragic end. The unforgiving forces of the wasteland have claimed your life. May your memory echo through the haunting ruins of Chernobyl.\n")
        self.game_introduction()

    def radiation_increase(self, amount):
        self.radiation_level += amount
        self.player_info()

    def radiation_decrease(self,amount):
        self.radiation_level -= amount
        self.player_info()


# Instantiate the game object and run the game
game = ChernobylSurvivalGame()
game.game_introduction()
