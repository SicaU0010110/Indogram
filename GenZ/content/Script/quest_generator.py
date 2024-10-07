import random

class Quest:
    def __init__(self, quest_data):
        self.type = quest_data['type']
        self.objective = quest_data['objective']
        self.reward = quest_data['reward']
        self.giver = quest_data['giver']
        self.status = 'active'
        self.progress = 0
        self.total_steps = quest_data['total_steps']

    def update_quest(self, action):
        if action == self.objective['action']:
            self.progress += 1
            if self.progress == self.total_steps:
                self.status = 'completed'
                return True
        return False

def generate_quest(world, npcs):
    quest_types = ['fetch', 'kill', 'escort', 'explore']
    quest_type = random.choice(quest_types)
    
    quest_objective = generate_quest_objective(quest_type, world)
    quest_reward = generate_quest_reward(quest_type)
    quest_giver = random.choice(npcs)
    total_steps = random.randint(1, 3)

    return Quest({
        'type': quest_type,
        'objective': quest_objective,
        'reward': quest_reward,
        'giver': quest_giver,
        'total_steps': total_steps
    })

def generate_quest_objective(quest_type, world):
    if quest_type == 'fetch':
        item = random.choice(world['items'])
        location = random.choice(world['locations'])
        return {
            'action': 'find_item',
            'item': item,
            'location': location,
            'description': f"Find the {item} in {location}"
        }
    elif quest_type == 'kill':
        enemy = random.choice(world['enemies'])
        location = random.choice(world['locations'])
        return {
            'action': 'defeat_enemy',
            'enemy': enemy,
            'location': location,
            'description': f"Defeat the {enemy} in {location}"
        }
    elif quest_type == 'escort':
        npc = random.choice(world['npcs'])
        destination = random.choice(world['locations'])
        return {
            'action': 'escort_npc',
            'npc': npc,
            'destination': destination,
            'description': f"Escort {npc} safely to {destination}"
        }
    elif quest_type == 'explore':
        location = random.choice(world['locations'])
        return {
            'action': 'explore_location',
            'location': location,
            'description': f"Explore and map out {location}"
        }

def generate_quest_reward(quest_type):
    reward_types = ['gold', 'experience', 'item']
    reward_type = random.choice(reward_types)

    if reward_type == 'gold':
        return {'type': 'gold', 'amount': random.randint(50, 500)}
    elif reward_type == 'experience':
        return {'type': 'experience', 'amount': random.randint(100, 1000)}
    elif reward_type == 'item':
        return {'type': 'item', 'item': generate_random_item()}

def generate_random_item():
    item_types = ['weapon', 'armor', 'potion']
    item_type = random.choice(item_types)
    
    if item_type == 'weapon':
        weapons = ['sword', 'axe', 'bow', 'staff']
        return f"{random.choice(['Iron', 'Steel', 'Elven', 'Dwarven'])} {random.choice(weapons)}"
    elif item_type == 'armor':
        armor_pieces = ['helmet', 'chestplate', 'leggings', 'boots']
        return f"{random.choice(['Leather', 'Chainmail', 'Plate'])} {random.choice(armor_pieces)}"
    elif item_type == 'potion':
        potion_types = ['healing', 'mana', 'strength', 'invisibility']
        return f"Potion of {random.choice(potion_types)}"

if __name__ == "__main__":
    # Test quest generation
    from character_generator import generate_npc

    world = {
        'items': ['Ancient Scroll', 'Magic Gem', 'Enchanted Sword'],
        'locations': ['Dark Forest', 'Abandoned Mine', 'Haunted Castle'],
        'enemies': ['Dragon', 'Orc Chieftain', 'Necromancer'],
        'npcs': [generate_npc('merchant') for _ in range(3)]
    }

    quest = generate_quest(world, world['npcs'])
    print(f"Quest Type: {quest.type}")
    print(f"Objective: {quest.objective['description']}")
    print(f"Reward: {quest.reward}")
    print(f"Given by: {quest.giver.name}")
    print(f"Total steps: {quest.total_steps}")

    # Test quest update
    print("\nUpdating quest progress:")
    for _ in range(quest.total_steps):
        completed = quest.update_quest(quest.objective['action'])
        print(f"Progress: {quest.progress}/{quest.total_steps}")
        if completed:
            print("Quest completed!")
            break
