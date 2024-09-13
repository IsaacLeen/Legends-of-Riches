"""
Represents an item in the game.

The `Item` class encapsulates the basic properties of an item, such as its name, description, and value. It also provides a `use` method that can be overridden by subclasses to implement the specific behavior of using the item.
"""
# item.py

class Item:
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    def use(self, player, target=None):
        print(f"You can't use {self.name} here.")