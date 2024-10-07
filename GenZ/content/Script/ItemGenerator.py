import random

# Define rarity weights (you might want to load this from a config file)
rarity_weights = {
    "Common": 60,
    "Uncommon": 30,
    "Rare": 8,
    "Epic": 2
}

def generate_random_rarity():
    total_weight = sum(rarity_weights.values())
    
    rand_value = random.uniform(0, total_weight)
    
    cumulative_weight = 0
    
    for rarity, weight in rarity_weights.items():
        cumulative_weight += weight
        if rand_value <= cumulative_weight:
            return rarity
    
    # In case of any unexpected issues, return the most common rarity
    return "Common"

# Example usage
if __name__ == "__main__":
    # Generate and print 10 random rarities
    for _ in range(10):
        print(generate_random_rarity())

import random

def generate_random_affix():
    affix_types = ['damage', 'defense', 'speed', 'health', 'mana', 'critical']
    affix_value = random.randint(1, 10)
    return f"{random.choice(affix_types)}+{affix_value}"

def generate_item(item_type, item_subtype, item_rarity):
    item = {'type': item_type, 'subtype': item_subtype, 'rarity': item_rarity, 'affixes': []}

    # Base stats based on item type and subtype
    base_stats = {
        'weapon': {'damage': 10},
        'armor': {'defense': 5},
        'accessory': {'bonus': 3},
        'consumable': {'effect': 5},
        # ... other item types
    }

    item['stats'] = base_stats.get(item_type, {}).copy()

    # Stat modifiers based on rarity
    rarity_modifiers = {
        'Common': 1.0,
        'Uncommon': 1.2,
        'Rare': 1.5,
        'Legendary': 2.0,
        'Mythic': 2.5,
        'God': 3.0
    }

    item['stats'] = {k: int(v * rarity_modifiers[item_rarity]) for k, v in item['stats'].items()}

    # Add random affixes based on rarity
    if item_rarity in ['Rare', 'Legendary', 'Mythic', 'God']:
        num_affixes = random.randint(1, 3)
        for _ in range(num_affixes):
            affix = generate_random_affix()
            item['affixes'].append(affix)

    # Generate a name for the item
    item['name'] = generate_item_name(item)

    return item

def generate_item_name(item):
    prefixes = ['Ancient', 'Mystic', 'Divine', 'Infernal', 'Celestial']
    suffixes = ['of Power', 'of the Titan', 'of Destruction', 'of Protection', 'of Speed']
    
    if item['rarity'] in ['Common', 'Uncommon']:
        return f"{item['subtype'].capitalize()}"
    elif item['rarity'] == 'Rare':
        return f"{random.choice(prefixes)} {item['subtype'].capitalize()}"
    else:
        return f"{random.choice(prefixes)} {item['subtype'].capitalize()} {random.choice(suffixes)}"

def generate_random_item():
    item_types = ['weapon', 'armor', 'accessory', 'consumable']
    item_subtypes = {
        'weapon': ['sword', 'axe', 'bow', 'staff', 'dagger'],
        'armor': ['helmet', 'chestplate', 'leggings', 'boots'],
        'accessory': ['ring', 'amulet', 'bracelet'],
        'consumable': ['potion', 'scroll', 'food']
    }
    rarities = ['Common', 'Uncommon', 'Rare', 'Legendary', 'Mythic', 'God']
    
    item_type = random.choice(item_types)
    item_subtype = random.choice(item_subtypes[item_type])
    item_rarity = random.choices(rarities, weights=[50, 30, 15, 4, 0.9, 0.1])[0]
    
    return generate_item(item_type, item_subtype, item_rarity)

if __name__ == "__main__":
    # Test the item generation
    for _ in range(10):
        item = generate_random_item()
        print(f"Generated Item: {item['name']}")
        print(f"Type: {item['type']}, Subtype: {item['subtype']}, Rarity: {item['rarity']}")
        print(f"Stats: {item['stats']}")
        if item['affixes']:
            print(f"Affixes: {', '.join(item['affixes'])}")
        print()

import random

class Item:
    def __init__(self, name, item_type, rarity, level, stats, tags, evolution_path=None):
        self.name = name
        self.item_type = item_type
        self.rarity = rarity
        self.level = level
        self.stats = stats
        self.tags = tags
        self.evolution_path = evolution_path
        self.experience = 0

    def gain_experience(self, amount):
        self.experience += amount
        print(f"{self.name} gains {amount} experience points.")
        self.check_evolution()

    def check_evolution(self):
        if self.evolution_path and self.experience >= self.evolution_path["experience_required"]:
            self.evolve()

    def evolve(self):
        self.name = self.evolution_path["evolved_name"]
        for stat, increase in self.evolution_path["stat_increases"].items():
            self.stats[stat] += increase
        self.rarity = self.evolution_path["new_rarity"]
        print(f"{self.name} has evolved! New attributes: {self.stats}, New Rarity: {self.rarity}")

rarity_weights = {
    'Common': 50,
    'Uncommon': 30,
    'Rare': 15,
    'Epic': 4,
    'Legendary': 1
}

item_types = ['weapon', 'armor', 'accessory', 'consumable']

item_subtypes = {
    'weapon': ['sword', 'axe', 'bow', 'staff', 'dagger'],
    'armor': ['helmet', 'chestplate', 'leggings', 'boots'],
    'accessory': ['ring', 'amulet', 'bracelet'],
    'consumable': ['potion', 'scroll', 'food']
}

item_tags = {
    'Berserker': ['strength', 'attack_speed'],
    'Mage': ['intelligence', 'spell_power'],
    'Rogue': ['dexterity', 'critical_chance'],
    'Tank': ['constitution', 'defense'],
    'Healer': ['wisdom', 'healing_power']
}

def generate_random_rarity():
    total_weight = sum(rarity_weights.values())
    rand_value = random.uniform(0, total_weight)
    cumulative_weight = 0
    for rarity, weight in rarity_weights.items():
        cumulative_weight += weight
        if rand_value <= cumulative_weight:
            return rarity

def calculate_item_level(player_level):
    return random.randint(max(1, player_level - 2), player_level + 2)

def generate_random_item_tags():
    tags = []
    if random.random() < 0.3:
        tags.append(random.choice(list(item_tags.keys())))
    return tags

def generate_item_stats(item_type, rarity, level):
    base_stats = {
        'weapon': {'damage': 10, 'attack_speed': 1.0},
        'armor': {'defense': 5, 'durability': 100},
        'accessory': {'bonus': 3},
        'consumable': {'effect': 5, 'duration': 30}
    }

    rarity_multipliers = {
        'Common': 1.0,
        'Uncommon': 1.2,
        'Rare': 1.5,
        'Epic': 2.0,
        'Legendary': 2.5
    }

    stats = base_stats.get(item_type, {}).copy()
    for stat in stats:
        stats[stat] = int(stats[stat] * rarity_multipliers[rarity] * (level / 10 + 0.5))

    return stats

def generate_evolution_path(item):
    if random.random() < 0.1:  # 10% chance for an item to have an evolution path
        return {
            "experience_required": random.randint(100, 500),
            "evolved_name": f"Enhanced {item.name}",
            "stat_increases": {stat: random.randint(5, 20) for stat in item.stats},
            "new_rarity": min(list(rarity_weights.keys())[list(rarity_weights.keys()).index(item.rarity) + 1:] + ['Legendary'])
        }
    return None

def generate_random_item(player_level):
    item_type = random.choice(item_types)
    item_subtype = random.choice(item_subtypes[item_type])
    rarity = generate_random_rarity()
    level = calculate_item_level(player_level)
    stats = generate_item_stats(item_type, rarity, level)
    tags = generate_random_item_tags()

    name = f"{rarity} {item_subtype.capitalize()}"
    item = Item(name, item_type, rarity, level, stats, tags)
    item.evolution_path = generate_evolution_path(item)

    return item

if __name__ == "__main__":
    # Test item generation and evolution
    player_level = 10
    for _ in range(5):
        item = generate_random_item(player_level)
        print(f"Generated Item: {item.name}")
        print(f"Type: {item.item_type}, Rarity: {item.rarity}, Level: {item.level}")
        print(f"Stats: {item.stats}")
        print(f"Tags: {item.tags}")
        if item.evolution_path:
            print(f"Evolution Path: {item.evolution_path}")
        print()

    # Test item evolution
    evolving_item = generate_random_item(player_level)
    while not evolving_item.evolution_path:
        evolving_item = generate_random_item(player_level)
    
    print(f"Testing evolution for: {evolving_item.name}")
    print(f"Initial stats: {evolving_item.stats}")
    print(f"Experience required: {evolving_item.evolution_path['experience_required']}")
    
    evolving_item.gain_experience(evolving_item.evolution_path['experience_required'])
