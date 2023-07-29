# Echoes Of The Exclusion

Echoes Of The Exclusion is a text based survival adventure game written using python. The game allows players to explore a mysterious exlusion zone, hunting for clues, evading radiation and making key decisions. The challenging interactive game provides feedback to the player based upon their decisions and has high replay value as there are multiple ways to win an lose. 
<br>
![EchoesOfTheExclusion](#)

## [Link to live site](https://echoes-of-the-exclusion-f4944290133d.herokuapp.com/)

## Contents

1. [How to play](#how-to-play)
2. [Features](#features)
   * [Existing Features](#existing-features)
   * [Future Features](#future-features)
3. [Data Model](#data-model)
4. [Testing](#testing)
   * [Bugs](#bugs)
        * [Solved](#solved-bugs)
   * [Validator Testing](#validator-testing)
5. [Deployment](#deployment)
6. [Credits](#credits)


## How to play

Echoes Of The Exclusion is an interactive text based adventure game. You can read more about the general theme on [Wikipedia](https://en.wikipedia.org/wiki/Text-based_game)
This game is based on surviving the Exclusion zone, based on Chernobyl. The player enters their name and they can then choose which direction to travel by inputting N, E, S or W (North, East, South, West). This takes the player to a new area which they can explore. They are given either multiple options which can be selected by inputting 1, 2 or 3 or head back to the previous location by entering the character displayed. There are also Yes/ No options which are decided by entering either Y or N. 

There are different ways to win the game and different ways to lose, depending on the players memory, luck and skills.  

## Features

### Exisiting Features

### Future Features

* Count how many times the player had to restart the game in order to win.
* Count how many inputs (decisions and directions) it took for the player to successfully complete the game and display high scores.
* Implement a health feature, more weapons and a combat system. 
* Have more items that can be stored in the players inventory which can be checked by entering a specific word.

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


### Validator  Testing

## Deployment

## Credits