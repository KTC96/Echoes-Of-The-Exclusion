# Base of game inspiration and code https://www.youtube.com/watch?v=DEcFCn2ubSg
# https://www.makeuseof.com/python-text-adventure-game-create/
import os
import sys
from enum import StrEnum

# Credit from https://www.geeksforgeeks.org/clear-screen-python/


def clear_screen():
    """
    Method checks the operating system and uses appropriate command to clear
    the screen.
    """
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# Credit from https://www.geeksforgeeks.org/enum-in-python/


class Direction(StrEnum):
    """
    Enum class to hold constant direction values
    """
    NORTH = 'N'
    EAST = 'E'
    SOUTH = 'S'
    WEST = 'W'


class Decisions(StrEnum):
    """
    Enum class to hold constant decisions in the game
    """
    YES = 'Y'
    NO = 'N'
    ONE = "1"
    TWO = "2"
    THREE = "3"
    RETURN = 'R'


class ChernobylSurvivalGame:
    def __init__(self):
        """
        Intitlilize instance variables
        """
        self.radiation_level = 0
        self.weapon = False
        self.visited_sublocations = {
            "fenced_area": False,
            "operating_room": False
        }

        self.player_name = ""

    def player_info(self):
        if self.radiation_level >= 3:
            self.radiation_death()

    def get_user_input(self, prompt, valid_options):
        """
        Utility function to validate and return user input.
        If it does not match the valid options it provides an
        error message
        """
        while True:
            user_input = input(prompt).upper().strip()
            if user_input in valid_options:
                return user_input
            else:
                print("Have you forgotten how to spell too? Try again...\n")

    def return_to_location(self, location_name):
        """
        Allows player to return to a main location from a sublocation
        while still wllowing the player to read the sublocation print
        statement before returning there
        """
        return_input = self.get_user_input(f"To return to {location_name}, enter R: ", [Decisions.RETURN])
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

    def reset_game(self):
        """
        Resets the instance variables so the game can be played again
        """
        self.radiation_level = 0
        self.weapon = False
        self.visited_sublocations = {
            "fenced_area": False,
            "operating_room": False
        }

    def game_introduction(self):
        """
        Introduces the player to the game and asks if they want to play.
        If the player chooses to play (by entering 'Y'), the game is initiated
        by calling the 'reset_game()' and 'start_zone()' methods. If the player
        declines (by entering 'N'), the game does not start, and a farewell
        message is displayed.
        """
        while True:
            print("""
                            ////////////////////////
                            ECHOES OF THE EXCLUSION
                            ////////////////////////

                                Can you survive
                                the wasteland?

                       Objective: Esacpe the Exclusion zone.
                          Your decisions decide your fate.

            Tip: Your maximum radiation points are 3
            """)
            decision = self.get_user_input("Would you like to play? (Y/N)\n", [Decisions.YES.value, Decisions.NO.value])
            clear_screen()
            if decision == Decisions.YES:
                self.reset_game()
                self.start_zone()
            elif decision == Decisions.NO:
                print("Understood, you are not ready for the challenge...")
                self.player_name = ""
                break

    def play_again_prompt(self):
        """
        Prompts the player to decide if they want to play again.
        """
        while True:
            play_again = self.get_user_input("Do you want to play again? (Y/N)\n", [Decisions.YES.value, Decisions.NO.value])
            clear_screen()
            if play_again == Decisions.YES:
                self.reset_game()
                self.start_zone()
                break
            elif play_again == Decisions.NO:
                print("Thanks for playing! See you next time.")
                self.player_name = ""
                # Credit https://stackoverflow.com/questions/14639077/how-to-use-sys-exit-in-python
                sys.exit()

    def start_zone(self):
        """
        This method provides introductary narrative.The player is prompted to
        enter their name and is given the choice to determine the direction
        they want to head first.
        """
        clear_screen()
        print("As you slowly regain consciousness, the world around you comes into focus. The")
        print("air feels heavy, carrying a sense of decay and abandonment. You find")
        print("yourself lying on the cold, damp ground, surrounded by the remnants of")
        print("what was once a bustling town.\n")
        if not self.player_name:
            self.player_name = input("Can you remember your name? (Enter name)\n").strip().capitalize()
        clear_screen()
        print(f"Good luck surviving the apocalypse {self.player_name}\n")
        print("As you rise to your feet, a mixture of awe and unease fills your")
        print("heart. The haunting silence and eerie atmosphere of the")
        print("exclusion zone envelop you. Nature has reclaimed its territory,")
        print("with overgrown vegetation and crumbling structures standing as")
        print("testament to the past.\n")
        print(f"So {self.player_name}, which way would you like to head first?\n")
        start_direction_map = {
                Direction.NORTH.value: self.power_plant,
                Direction.EAST.value: self.forest,
                Direction.SOUTH.value: self.city,
                Direction.WEST.value: self.hospital
        }

        while True:
            start_direction = self.get_user_input("Options: N/E/S/W\n", start_direction_map.keys())
            start_direction_map[start_direction]()

    def start_zone_return(self):
        """
        Handles the player's return to the starting point after exploring a
        location. It clears the screen, displays a message indicating the return
        to the starting area, and prompts the player to choose a direction for
        further exploration.
        """
        clear_screen()
        print("You return to where you started, not much has changed...")
        print(f"So {self.player_name}, which way would you like to head?\n")

        while True:
            player_input = self.get_user_input("Options: N/E/S/W\n", [d.value for d in Direction])
            match player_input:
                case Direction.NORTH.value:
                    self.power_plant()
                case Direction.EAST.value:
                    self.forest()
                case Direction.SOUTH.value:
                    self.city()
                case Direction.WEST.value:
                    self.hospital()

    def power_plant(self):
        """
        Explores the abandoned power plant. Upon entering player gains 2
        radiation points. Asks player if they want to investigate movement in
        the shadows.If the player chooses yes the fight monster function is
        called. If no, the player returns to the start zone.
        """
        clear_screen()
        print("The heart of the disaster, the abandoned power plant looms in the")
        print("distance, its towering smokestacks and crumbling reactors a")
        print("haunting reminder of the catastrophic event. It emits an ")
        print("unsettling aura, and caution is advised when venturing too close.\n")
        print("This was the incident epicenter, +2 radiation points\n")
        self.radiation_increase(2)
        power_plant_input = self.get_user_input("You see something scuttling in the shadows, do you investigate? (Y/N)\n", [Decisions.YES.value, Decisions.NO.value])
        if power_plant_input == Decisions.YES:
            clear_screen()
            self.monster_fight()
        elif power_plant_input == Decisions.NO:
            clear_screen()
            print("Who knows what that could have been, probably best to explore elsewhere first.\n")
            self.return_to_location("start_zone")

    def monster_fight(self):
        """
        Handles the monster encounter and its consequences.
        If the player has a weapon, the win game method is called, if not the player dies
        """
        clear_screen()
        print(" Turning a corner you are faced with a gigantic mutated monster,")
        print("a nightmarish fusion of twisted limbs and glowing eyes.")
        if self.weapon is True:
            clear_screen()
            print("You shoot the monster on a glowing lump on its underbelly, it explodes")
            print("and the monster drops onto the ground\n")
            self.win_game()
        elif self.weapon is False:
            clear_screen()
            print("The monster ripped you limb from limb if only you had a weapon..\n")
            self.death()

    def forest(self):
        """
        Player explores the forest and encounters various options.
        Player is offered with different options which lead to different
        sublocations, or they can head back to the starting zone
        """
        clear_screen()
        print("You have walked beyond the city limits to a dense forest tainted by radiation.")
        print("The trees stand twisted and sickly, their leaves discolored and wilted. The")
        print("air is heavy with an acrid smell, and eerie glowing fungi dot the forest floor")
        print("casting an otherworldly glow.\n")
        print("Walking through the forest, you hear a mysterious sound coming from deep within.\n")
        print("what do you do?\n")

        forest_decision_map = {
            Decisions.ONE.value: self.cave,
            Decisions.TWO.value: self.field,
            Decisions.THREE.value: self.fenced_area,
            Direction.WEST.value: self.start_zone_return
        }

        while True:
            forest_decision = self.get_user_input("Options: Follow the sound, explore the forest, build a shelter (1,2,3)\nor head back (W)\n", forest_decision_map.keys())
            forest_decision_map[forest_decision]()

    def cave(self):
        """
        Player follows the sound and finds a symbol. If the meaning
        has been found elsewhere in the game the win game method is
        called. If not they are told that nothing happened and they
        are prompted to return to the forest.
        """
        clear_screen()
        print("As you follow the mysterious sound deeper into the forest, you discover a hidden")
        print("cave adorned with ancient symbols and an underground waterfall.\n")
        print("You see a large symbol, I wonder what it could mean?\n")
        self.symbols(1)
        secret_input = input("???\n").upper().strip()
        if secret_input == "SANCTUM":
            clear_screen()
            print("The symbol seems to glow faintly and you suddenly notice a passage")
            print("that you swear was not there before, you crawl through to be met by a")
            print("patrolling soldier on the other side...\n ")
            self.win_game()
        else:
            clear_screen()
            print("That did not seem to do anything")
            print("if only you could work out the symbols meaning...\n")
            self.return_to_location("forest")

    def symbols(self, symbol_number):
        """
        Provides the different symbols and their related meaning.
        """
        all_symbols = [
            """
                     /\\
                    /  \\
                   /  ^ \\
                  /   ^  \\
                  \\  ^  //
                   \\ ^ //
                    \\ //
                     """,
            """
                     /\\
                    /  \\
                   /  * \\
                  /   *  \\
                  \\  *  //
                   \\ * //
                    \\ //
                     """,
            """
                     /\\
                    /  \\
                   /  | \\
                  /   ^  \\
                  \\  |  //
                   \\ ^ //
                    \\ //
                     """
        ]

        print(all_symbols[symbol_number - 1])

    def field(self):
        """
        Provides the player with a clue to where they can find a weapon and returns
        them to the forest
        """
        clear_screen()
        print("As you explore further, you stumble upon a vast open field, amidst the swaying")
        print("grass and gentle breeze, you an old and dirty radio...\n")
        print("It comes to life sporadically, revealing a faint but unmistakable voice:")
        print("a survivor's log, Day 34. The survivor cryptically hints about a weapon")
        print("crucial for survival, concealed within a safe in a nearby apartment building...\n")
        self.return_to_location("forest")

    def fenced_area(self):
        """
        While collecting wood for the shelter the player encounters a fenced-off area.
        If the player has not visited the fenced area before, they are presented with a
        choice to enter or not. If they enter, their radiation level increases by 2, and they return to
        the forest. If they choose not to enter, their radiation points decrease by 1, and they return to
        the forest. If the player has already visited the fenced area, they are informed that they have
        built enough and should continue their search elsewhere.
        """
        clear_screen()
        if not self.visited_sublocations["fenced_area"]:
            self.visited_sublocations["fenced_area"] = True

            radiation_zone = self.get_user_input("While collecting wood to make yourself a shelter, you come across a\n fenced off area with a symbol stating 'DO NOT ENTER RADIATION RISK'.\nDo you enter?(Y/N)\n", [Decisions.YES.value, Decisions.NO.value])
            if radiation_zone == Decisions.YES:
                clear_screen()
                print("You start to feel a buzzing sound rattling inside of your skull,")
                print("maybe the sign was right. You drop the wood you gathered and return")
                print("to the forest.\n")
                print("+2 radiation points\n")
                self.radiation_increase(2)
                self.return_to_location("forest")
            elif radiation_zone == Decisions.NO:
                clear_screen()
                print("You return to the forest and make a comfortable shelter for the night.")
                print("Radiation points decresed by 1.\n")
                self.radiation_decrease(1)
                self.return_to_location("forest")
        else:
            print("That's enough building, continue your search elsewhere...\n")
            self.return_to_location("forest")

    def city(self):
        """
        In this method, the player reaches the City Center. The player can
        head towards the apartment complex, go to the exclusion zone limit,
        head to the library, or head back to the starting zone.
        """
        clear_screen()
        print("You have reached the City Center. Once a bustling metropolis, the city")
        print("now stands in ruins, its buildings crumbling and overgrown with vegetation.")
        print("The eerie silence is broken only by the haunting howl of the wind, and the")
        print("streets are littered with debris and remnants of human civilization...\n")

        city_decision_map = {
            Decisions.ONE.value: self.apartment,
            Decisions.TWO.value: self.mine_field,
            Decisions.THREE.value: self.library,
            Direction.NORTH.value: self.start_zone_return}

        while True:
            city_decision = self.get_user_input("Options: Head towards the apartment complex, go to the exclusion zone limit,\nhead to the library (1,2,3) or head back (N)\n", city_decision_map.keys())
            city_decision_map[city_decision]()

    def apartment(self):
        """
        In this method, the player explores the abandoned apartment complex. The player is prompted
        to enter the code, and if the correct code ('RADIOACTIVE') is entered, the safe unlocks to
        reveal a weapon. Otherwise, the player is informed that the entered code was incorrect and
        they return to the city.
        """

        clear_screen()
        print("As you explore the complex, you notice several rooms with open doors,")
        print("revealing remnants of the past - scattered belongings, overturned furniture,")
        print("and broken memories. Some rooms are completely dark, and you can only imagine")
        print("what lies within. However, one particular room catches your attention. A faint")
        print("light seeps out from beneath the door, hinting at something inside.\n")
        print("You open the door and find a safe, with a strange alphabetized lock,")
        print("if only you knew the code...\n")
        safe_code_input = input("Enter the code:\n ").upper().strip()
        if safe_code_input == "RADIOACTIVE":
            clear_screen()
            print("The safe unlocks with a dull thud, inside you discover a handgun,")
            print("this is sure to help your survival.\n")
            self.weapon = True
            self.return_to_location("city")
        else:
            clear_screen()
            print("That was not correct\n")
            self.return_to_location("city")

    def library(self):
        """
        In this method, the player explores the library. As the playerenters the library,
        they are covered in radioactive dust, resulting in a +1 radiation pointincrease.
        Inside the player comes across a diary with symbols and text that reads 'HOPE,'
        'REFUGE,' and 'SANCTUM.' After exploring the library, the player is prompted to
        return to the City Center.
        """

        clear_screen()
        print(" Upon entering the Library you are covered in radioactive dust.\nLets hope this is worth it (+1 radiation point)\n")
        self.radiation_increase(1)
        print("Inside, the dimly lit space is filled with dusty books and scattered notes,")
        print("hinting at the knowledge it holds. As you explore, you come across a cryptic")
        print("diary with the following symbols and text:\n")
        self.symbols(2)
        print("HOPE\n")
        self.symbols(3)
        print("REFUGE\n")
        self.symbols(1)
        print("SANCTUM\n")
        print("I wonder what those strange symbols could mean?\n")
        self.return_to_location("city")

    def mine_field(self):
        """
        In this method, the player is prompted to decide whether they wantto enter the
        minefield or not. If the player chooses to enter (input 'Y'), the player meets
        their tragic end, and the `death()` method is called. If the player decides not
        to enter (input 'N'), the player returns to the City Center.
        """
        clear_screen()
        print("As you venture toward the outer limits of the city, you spot a menacing sight:")
        print("a treacherous minefield stretching before you. Warning signs adorned with skull")
        print("symbols and bold letters caution against entering. The air feels tense, and you")
        print("can sense the lurking danger that lies ahead.\n")
        enter_mine_field = self.get_user_input("Enter the minefield? (Y/N)\n", [Decisions.YES, Decisions.NO])
        if enter_mine_field == Decisions.YES:
            clear_screen()
            print("That was not a wise decision...")
            self.death()
        elif enter_mine_field == Decisions.NO:
            clear_screen()
            print("Surely the city must be safer...\n")
            self.return_to_location("city")

    def hospital(self):
        clear_screen()
        print("You arrive at the abandoned hospital, once a place of healing and hope")
        print("Now, it stands as a haunting reminder of the past. Broken windows and")
        print("overgrown ivy greet you as you step inside.The scent of decay lingers")
        print("in the air,and eerie silence fills the halls.\n")

        hospital_decision_map = {
            Decisions.ONE: self.hospital_office,
            Decisions.TWO: self.operating_room,
            Decisions.THREE: self.basement,
            Direction.EAST.value: self.start_zone_return}

        while True:
            hospital_decision = self.get_user_input("Options: Search the Hospital offices, Explore the operating room, Decend into\nthe basement (1,2,3) or head back (E)\n ", hospital_decision_map.keys())
            hospital_decision_map[hospital_decision]()

    def hospital_office(self):
        clear_screen()
        print("Upon entering the abandoned hospital offices, you are startled by")
        print("a chilling\n sight: a mutated dog lurking in the shadows. Its")
        print("disfigured appearance and haunting howls evoke terror\n ")
        enter_office = self.get_user_input("Search the office? (Y/N)\n", [Decisions.YES.value, Decisions.NO.value])
        if enter_office == Decisions.YES:
            clear_screen()
            print("You manage to distract the mutated dog by throwing a clipboard")
            print("into another room. There dosn't seem to be much in the office,")
            print("other than a piece of paper with the words 'Narcotic aid'")
            print("scribbled on them, could it be an anagram...\n")
            self.return_to_location("hospital")
        elif Decisions.NO:
            clear_screen()
            print("That seems like the right choice...\n")
            self.return_to_location("hospital")

    def operating_room(self):
        clear_screen()
        if not self.visited_sublocations["operating_room"]:

            print("You cautiously enter the operating room, and the pungent")
            print("stench of decayassaults your senses. Your eyes widen as you")
            print("come face to face with a ghastly sight :a rotting corpse")
            print("lies on the operating table, remnants of a medical procedure")
            print("long abandoned.\n")
            search_body = self.get_user_input("Search the corpse? (Y/N)\n", [Decisions.YES.value, Decisions.NO.value])
            if search_body == Decisions.YES:
                clear_screen()
                print("You search the corpse to discover a syringe labelled")
                print("'Anti-radioactive particles' (removes all current radiation points)\n")
                self.radiation_level = 0
                self.visited_sublocations["operating_room"] = True
                self.return_to_location("hospital")
            elif search_body == Decisions.NO:
                clear_screen()
                print("Who knows what diseases that body could have had...\n")
                self.return_to_location("hospital")
        else:
            print("You have already taken the medicine, continue your search elsewhere...\n")
            self.return_to_location("hospital")

    def basement(self):
        clear_screen()
        print("There does not seem to be much down here except from radioactive dust\n(+1 radiation point)")
        self.radiation_increase(1)
        self.return_to_location("hospital")

    def win_game(self):
        print("Congratulations! You have successfully navigated through the")
        print("treacherous Chernobyl Exclusion Zone, overcoming countless")
        print("challenges and unearthing ancient mysteries. With determination")
        print("and wit, you have survived the apocalypse and emerged as a true")
        print("survivor. The world may have changed, but your resilience and")
        print("bravery have stood the test of time. You are now hailed as a")
        print("legend, the one who conquered the Zone and unlocked its deepest")
        print("secrets. Your name will be remembered for generations to come,")
        print("and your journey will forever be etched in history. Well done,")
        print("champion of the Echoes of the Exclusion!\n")
        self.play_again_prompt()

    def radiation_death(self):
        print("Your radiation exposure has exceeded the critical level, your")
        print("body weakens, and you succumb to the deadly effects, leaving the")
        print("Exclusion Zone as your final resting place.\n")
        self.play_again_prompt()

    def death(self):
        print("Your journey in the Exclusion Zone has come to a tragic end. The")
        print("unforgiving forces of the wasteland have claimed your life. May")
        print("your memory echo through the haunting ruins of Chernobyl.\n")
        self.play_again_prompt()

    def radiation_increase(self, amount):
        self.radiation_level += amount
        self.player_info()

    def radiation_decrease(self, amount):
        if self.radiation_level >= 1:
            self.radiation_level -= amount
            self.player_info()
        else:
            print("Your radiation level was already at 0, but at least you can enjoy some self reflection...\n")

# Instantiate the game object and run the game


if __name__ == "__main__":
    game = ChernobylSurvivalGame()
    game.game_introduction()
