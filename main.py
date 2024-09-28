"""
Runs the main game loop for the game engine. 

This script is the entry point for the game application. It creates a new instance of the `GameEngine` class and calls its `play()` method to start the game loop.
"""
#stussy
# main.py
from game_engine import GameEngine


if __name__ == "__main__":
    game = GameEngine()
    game.play()