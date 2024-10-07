import random

class Item:
    def __init__(self, name, durability, performance, efficiency, evolution, quality):
        self.name = name
        self.durability = durability
        self.performance = performance
        self.efficiency = efficiency
        self.evolution = evolution
        self.quality = quality
        self.experience = 0

    def gain_experience(self, amount):
        self.experience += amount
        print(f"{self.name} gains {amount} experience points.")
        self.check_evolution()

    def check_evolution(self):
        if self.experience >= self.evolution["experience_required"]:
            self.evolve()

    def evolve(self):
        self.name = self.evolution["evolved_name"]
        self.durability += self.evolution["durability_increase"]
        self.performance += self.evolution["performance_increase"]
        self.efficiency += self.evolution["efficiency_increase"]
        self.quality = self.evolution["new_quality"]
        print(f"{self.name} has evolved! New attributes: Durability: {self.durability}, Performance: {self.performance}, Efficiency: {self.efficiency}, Quality: {self.quality}")

# Item generation constants and configurations
item_types = ['weapon', 'armor', 'consumable', 'jewelry', 'artifact']
item_subtypes = {
    'weapon': ['sword', 'axe', 'mace', 'bow', 'staff', 'dagger'],
    'armor': ['helmet', 'chestplate', 'leggings', 'boots'],
    # ... other item types
}
affix_prefixes = ['Fiery', 'Icy', 'Poisonous', 'Electric']
affix_suffixes = ['of the Bear', 'of the Dragon', 'of the Void']
rarity_weights = {
    'Common': 70,
    'Uncommon': 20,
    'Rare': 8,
    'Legendary': 2,
    'Mythic': 0.5,
    'God': 0.1
}
item_sets = {
    'Berserker': ['Berserker Sword', 'Berserker Helm', 'Berserker Chestplate'],
    # ... other item sets
}
item_tags = {
    'Berserker': ['strength', 'attack_speed'],
    'Mage': ['intelligence', 'spell_power'],
    # ... other item tags
}

def generate_item_name(item_type, rarity, affixes):
    prefixes = ["Ancient", "Mystical", "Shadowy", "Blazing", "Frostbitten"]
    suffixes = ["of Power", "of the Void", "of the Deep", "of the Sky"]
    
    name = ""
    if rarity == "Common":
        name = f"{random.choice(prefixes)} {item_type}"
    elif rarity == "Uncommon":
        name = f"{random.choice(prefixes)} {item_type} {random.choice(suffixes)}"
    elif rarity == "Rare":
        # ... more complex naming logic for higher rarities
        pass
    else:
        # ... even more complex naming logic for legendary and mythic items
        pass
    
    # Incorporate affix names into the item name
    for affix in affixes:
        name += f" {affix}"
    
    return name

def generate_item_effects(item_type, rarity, affixes):
    effects = []
    base_effects = {
        "weapon": {"damage": random.randint(1, 10)},
        "armor": {"defense": random.randint(1, 5)},
        # ... other item types
    }
    effects.extend(base_effects.get(item_type, {}).items())
    # Add effects based on rarity and affixes
    return effects

def generate_random_rarity():
    total_weight = sum(rarity_weights.values())
    rand_value = random.uniform(0, total_weight)
    cumulative_weight = 0
    for rarity, weight in rarity_weights.items():
        cumulative_weight += weight
        if rand_value <= cumulative_weight:
            return rarity

def calculate_item_level(player_level):
    return random.randint(player_level - 2, player_level + 2)

def generate_random_item_tags(item_type):
    tags = []
    if random.random() < 0.3:
        tags.append(random.choice(list(item_tags.keys())))
    return tags

def generate_item(item_level, rarity):
    item_type = random.choice(item_types)
    item_subtype = random.choice(item_subtypes[item_type])
    
    item = {
        'name': generate_item_name(item_subtype, rarity, []),  # Initial name without affixes
        'type': item_type,
        'subtype': item_subtype,
        'effects': generate_item_effects(item_type, rarity, []),
        'level': item_level,
        'rarity': rarity,
        'tags': generate_random_item_tags(item_type)
    }
    
    # Adjust item stats based on item level
    for effect in item['effects']:
        item['effects'][effect] *= item_level
    
    return item

def calculate_item_power(item):
    power = 0
    effect_weights = {
        'damage': 1.5,
        'defense': 1.2,
        # ... other effect weights
    }
    rarity_modifiers = {
        'Common': 1,
        'Uncommon': 1.2,
        'Rare': 1.5,
        'Legendary': 2,
        'Mythic': 2.5,
        'God': 3
    }
    
    for effect, value in item['effects'].items():
        power += value * effect_weights.get(effect, 1)
    
    # Add power based on rarity and level
    power *= rarity_modifiers[item['rarity']] * item['level']
    
    return power

def check_item_synergies(item, inventory):
    # Check for item set bonuses
    # Check for affix combinations (e.g., two fire affixes)
    # ... implement synergy logic
    pass

# Example usage
if __name__ == "__main__":
    player_level = 10
    item_level = calculate_item_level(player_level)
    rarity = generate_random_rarity()
    new_item = generate_item(item_level, rarity)
    print(f"Generated item: {new_item['name']}")
    print(f"Type: {new_item['type']}, Subtype: {new_item['subtype']}")
    print(f"Level: {new_item['level']}, Rarity: {new_item['rarity']}")
    print(f"Effects: {new_item['effects']}")
    print(f"Tags: {new_item['tags']}")
    print(f"Item Power: {calculate_item_power(new_item)}")

    # Example of item evolution
    evolution_path = {
        "experience_required": 100,
        "evolved_name": "Enhanced Sword",
        "durability_increase": 20,
        "performance_increase": 10,
        "efficiency_increase": 5,
        "new_quality": "Rare"
    }
    sword = Item("Basic Sword", 50, 10, 5, evolution_path, "Common")
    sword.gain_experience(50)
    sword.gain_experience(50)
