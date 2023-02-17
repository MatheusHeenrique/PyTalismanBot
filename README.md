Talisman Online Bot

This Python bot is intended for the game Talisman Online. The use of this bot has the advantage of checking the player's life level and healing them when it reaches a defined limit, making the player's death difficult.

It is not possible to use this bot in multiple windows, but it works in the background, allowing the player to minimize the main game window and use another workspace.

To make the bot work correctly, it is necessary to adjust some variables, such as those on lines 10 to 15 of the LerMemoria file. These variables include: self.ponteiro_vida (player's life pointer), self.ponteiro_mana (player's mana pointer), self.ponteiro_selecionar_inimigo (pointer to check if the player has selected an enemy) and self.ponteiro_vida_inimigo (enemy's life pointer). The self.ponteiro_estamina variable is not necessary.
Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.
Prerequisites

This bot requires Python 3.7 or above and the PyAutoGUI and keyboard libraries to be installed. These can be installed using pip:

pip install pyautogui
pip install keyboard

Installing

To install the bot, simply clone the repository:

bash

git clone https://github.com/your_username/talisman-bot.git

Running the Bot

To run the bot, navigate to the directory containing the bot files and run:

css

python main.py

