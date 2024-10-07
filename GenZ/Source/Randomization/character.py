import random
import pickle

class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.level = 1
        self.experience = 0
        self.experience_to_next_level = 100
        self.inventory = {}

    def attack(self, other):
        other.health -= self.attack_power
        print(f"{self.name} attacks {other.name} for {self.attack_power} damage.")

    def is_alive(self):
        return self.health > 0

    def display_health(self):
        print(f"{self.name} has {self.health} health remaining.")

    def gain_experience(self, amount):
        self.experience += amount
        print(f"{self.name} gains {amount} experience points.")
        self.check_level_up()

    def check_level_up(self):
        while self.experience >= self.experience_to_next_level:
            self.experience -= self.experience_to_next_level
            self.level += 1
            self.experience_to_next_level = int(self.experience_to_next_level * 1.5)
            self.health += 20
            self.attack_power += 5
            print(f"{self.name} leveled up to level {self.level}!")
            print(f"New stats - Health: {self.health}, Attack Power: {self.attack_power}")

    def add_item_to_inventory(self, item, quantity=1):
        if item.name in self.inventory:
            self.inventory[item.name]["quantity"] += quantity
        else:
            self.inventory[item.name] = {"item": item, "quantity": quantity}
        print(f"Added {quantity} x {item.name} to inventory.")

    def display_inventory(self):
        if self.inventory:
            print("Current Inventory:")
            for item_name, item_info in self.inventory.items():
                item_info["item"].display_attributes()
                print(f"Quantity: {item_info['quantity']}")
        else:
            print("Inventory is empty.")

    @staticmethod
    def load_game(filename="savegame.pkl"):
        with open(filename, 'rb') as f:
            player = pickle.load(f)
        print("Game loaded successfully.")
        return player
