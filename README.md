# Talisman Online Bot

This Python bot is intended for the game Talisman Online. The use of this bot has the advantage of checking the player's life level and healing them when it reaches a defined limit, making the player's death difficult.

It is not possible to use this bot in multiple windows, but it works in the background, allowing the player to minimize the main game window and use another workspace.

To make the bot work correctly, it is necessary to adjust some variables, such as those on lines 10 to 15 of the read_memory.py file. These variables include: self.pointer_life (player's life pointer), self.mana_pointer (player's mana pointer), self.pointer_select_enemy (pointer to check if the player has selected an enemy) and self.enemy_life_pointer (enemy's life pointer). The self.stamina_pointer variable is not necessary.
## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.
### Prerequisites

This bot requires Python 3.7 or above and requires the libraries listed in requirements.txt. These can be installed using pip:

  pip install -r requirements.txt

### Installing

To install the bot, simply clone the repository:

bash

  git clone https://github.com/your_username/talisman-bot.git

### Running the Bot

To run the bot, navigate to the directory containing the bot files and run:

bash

  python main.py

