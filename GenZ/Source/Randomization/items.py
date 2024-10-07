class Item:
    def __init__(self, name, durability, performance, efficiency, evolution, quality):
        self.name = name
        self.durability = durability
        self.performance = performance
        self.efficiency = efficiency
        self.evolution = evolution
        self.quality = quality

    def display_attributes(self):
        print(f"Item: {self.name}")
        print(f"Durability: {self.durability}")
        print(f"Performance: {self.performance}")
        print(f"Efficiency: {self.efficiency}")
        print(f"Evolution: {self.evolution}")
        print(f"Quality: {self.quality}")

def generate_item(name, player_level):
    durability = random.randint(50, 100) + (player_level * 5)
    performance = random.randint(10, 20) + (player_level * 2)
    efficiency = random.randint(5, 15) + (player_level * 1)
    evolution = random.randint(1, 5) + (player_level // 2)
    quality = random.choice(["Common", "Uncommon", "Rare", "Epic", "Legendary"])
    return Item(name, durability, performance, efficiency, evolution, quality)
