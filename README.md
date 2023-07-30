# Echoes Of The Exclusion

Echoes Of The Exclusion is a text based survival adventure game written using python. The game allows players to explore a mysterious exlusion zone, hunting for clues, evading radiation and making key decisions. The challenging interactive game provides feedback to the player based upon their decisions and has high replay value as there are multiple ways to win an lose. 
<br>
![EchoesOfTheExclusion](./README_images/Screenshot%20(68).png)

## [Link to live site](https://echoes-of-the-exclusion-f4944290133d.herokuapp.com/)

## Contents

1. [How to play](#how-to-play)
2. [Features](#features)
   * [Existing Features](#existing-features)
   * [Future Features](#future-features)
3. [Data Model](#data-model)
4. [Testing](#testing)
   * [Bugs](#bugs)
        * [Solved Bugs](#solved-bugs)
        * [Remaining Bugs](#remaining-bugs)
   * [Validator Testing](#validator-testing)
5. [Deployment](#deployment)
6. [Credits](#credits)


## How to play

Echoes Of The Exclusion is an interactive text based adventure game. You can read more about the general theme on [Wikipedia](https://en.wikipedia.org/wiki/Text-based_game)
This game is based on surviving the Exclusion zone, based on Chernobyl. The player enters their name and they can then choose which direction to travel by inputting N, E, S or W (North, East, South, West). This takes the player to a new area which they can explore. They are given either multiple options which can be selected by inputting 1, 2 or 3 or head back to the previous location by entering the character displayed. There are also Yes/ No options which are decided by entering either Y or N. 

There are different ways to win and lose, depending on the players memory, luck and skills.  

## Features

### Exisiting Features

* Game introduction screen
    * Introduces the scope of the game to the player.
    * Gives the player a tip about radiation points and prompts them if they would like to play.
    * Input validation: If the player enters a non valid character they are shown an error message and asked to input again.

![Intro Screen](./README_images/Screenshot%20(58).png)

* Name input
    * The player is asked for their name which is capitalized upon entering.
    * Their name is stored as an instance variable so if they choose to play again they do not have to re-enter their name

![Name input](./README_images/Screenshot%20(59).png)

* Direction choices
    * The player can choose which way they would like to travel.
    * When arrving at a destination they are greeted with a description of the area and multiple options they can pursue. Or they can head back and revisit previously visited locations

![Directions](./README_images/Screenshot%20(60).png)

* Winning the game
    * There are two ways to win the game. They can find a secret hidden meaning or find a weapon and defeat a monster

![Way to win 1](./README_images/Screenshot%20(61).png)

![Way to win 2](./README_images/Screenshot%20(66).png)

* Radiation points
    * The player starts on 0 radiation points but based on their decisions this can increase. Once it reaches 3 they player recieves a message that they died from radiation exposure. 

![Radiation Death](./README_images/Screenshot%20(62).png)

* Healing
    * The player is also able to reduce their radiation points through certain in game actions.
    * To prevent explotation of this mechanic, areas where the players radiation points are reduced can only be visited once. 
    * If they player's radiaiton points were alredy at 0, then a message is displayed informing them of this and the radiation points are not set to a negative integer.

![Healing](./README_images/Screenshot%20(67).png)

* Other ways to lose the game
    * The player can run into different scenarioes where they die.
    * The player has to remember these dangerous zones for next time, which increases replay value.

![Monster Death](./README_images/Screenshot%20(63).png)

![Minefield Death](./README_images/Screenshot%20(64).png)

* The player has to find clues and solve a puzzle to unlock the games secrets. 
   * For example an anagram must be solved in order to unlock a safe so the player gains access to a weapon

![Code entry](./README_images/Screenshot%20(65).png)




 




### Future Features

* Count how many times the player had to restart the game in order to win.
* Count how many inputs (decisions and directions) it took for the player to successfully complete the game and display high scores.
* Implement a health feature, more weapons and a combat system. 
* Have more items that can be stored in the players inventory which can be checked by entering a specific word.
* Properly integrate classes for different instances of the game

## Data Model

I decided to use a text-based data model. The mechanics, interactions and story progression are implemented using text-based input and output.

The game uses Python's enum module to define enumerations for directions (Direction) and decisions (Decisions). This provids a way to represent and handle different choices available to the player during the game. 

The game also  maintains attributes for the player, such as radiation_level, weapon, and visited_sublocations. These attributes store the player's progress, choices made, and game state. 

The game uses methods and conditional statements to control the flow of the game. The game state evolves based on the player's decisions and actions.

The game defines various locations and sublocations and the player can navigate through these areas based on their choices. The game uses text-based print statements to provide descriptions, dialogues, and narrations to convey the story and set the atmosphere.



## Testing

### Bugs

#### Solved Bugs

Issue: The use of self.player_name in the start_zone() method:

Explanation: The method attempted to access self.player_name before it was set, resulting in an AttributeError. The correct variable name is self.player_name_input.

Issue: Missing cases in the start_zone_return() method:

Explanation: The statement inside start_zone_return() did not have cases for each direction (N, E, S, W). It caused the game to break when the player attempted to go in a direction not listed in the switch statement.

Issue: Incorrect method call in field(): 

Explanation: The incorrect method call to self.forest() in the field() method was removed, allowing the player to continue the game after reading the survivor's log.

Issue: Game continuation after death():

Explanation: When the player died and was asked to play, if they chose 'N' (No) the game continued. A new method play_again_prompt was implemented to call sys.exit() if they player entered 'N'.

Issue: get_user_input was case insensitve

Explanation: The get_user_input method was modified to convert the valid options to uppercase to ensure case-insensitive comparison with the user's input. This prevents issues where the user might enter lowercase characters for valid options.

Issue: When replaying the game, visiting the library caused duplication of print statements.

Explanation:

The play_again_prompt() method was being called multiple times when the player chooses to play again. Modification of the play_again_prompt() method to include a loop solved the issue. 

#### Remaining Bugs

There are no remaining bugs


### Validator Testing

* PEP8
   * Error free code checked on [CI Python Linter](https://pep8ci.herokuapp.com/#)
   * *Errors for character length but this is not applicable due to indentation and use of \n (new line)



## Deployment

This project was deployed using Code Institues mock terminal for Heroku:

* Steps for deployment:
   * Create a new Heroku app
   * Set Config vars key to "PORT" and value to "8000"
   * Set buildpacks to Python and NodeJS in that order
   * Link the Heroku app to my github repository
   * Click on deploy


## Credits

For the inspiration and base of my code I followed this [tutorial](https://www.makeuseof.com/python-text-adventure-game-create/) and this video on [YouTube](https://www.youtube.com/watch?v=DEcFCn2ubSg)

[Match case statements](https://learnpython.com/blog/python-match-case-statement/)
[System Exit](https://stackoverflow.com/questions/14639077/how-to-use-sys-exit-in-python)
[Clear Screen](https://www.geeksforgeeks.org/clear-screen-python/)
[Enumerations](https://www.geeksforgeeks.org/enum-in-python/)





I would like to thank my mentor Jack Wachira for his valuable help and feedback throughout this project as well as Code Institute for the deployment terminal. 
