import random

class Character:
    def __init__(self, name, class_type):
        self.name = name
        self.class_type = class_type
        self.attributes = {}
        self.skills = {}
        self.level = 1
        self.experience = 0
        self.appearance = {}
        self.personality = {}
        self.background = ""
        self.relationships = {}
        self.goals = []
        self.emotional_state = "neutral"

    def generate_attributes(self):
        attribute_ranges = {
            'Warrior': {'Strength': (8, 12), 'Dexterity': (6, 10), 'Constitution': (8, 12),
                        'Intelligence': (4, 8), 'Wisdom': (4, 8), 'Charisma': (4, 8)},
            'Mage': {'Strength': (4, 8), 'Dexterity': (6, 10), 'Constitution': (4, 8),
                     'Intelligence': (8, 12), 'Wisdom': (8, 12), 'Charisma': (6, 10)},
            'Rogue': {'Strength': (6, 10), 'Dexterity': (8, 12), 'Constitution': (6, 10),
                      'Intelligence': (6, 10), 'Wisdom': (4, 8), 'Charisma': (6, 10)},
            'Cleric': {'Strength': (6, 10), 'Dexterity': (4, 8), 'Constitution': (6, 10),
                       'Intelligence': (6, 10), 'Wisdom': (8, 12), 'Charisma': (6, 10)}
        }
        
        for attr, (min_val, max_val) in attribute_ranges[self.class_type].items():
            self.attributes[attr] = random.randint(min_val, max_val)

    def generate_skills(self):
        skill_sets = {
            'Warrior': {'Swordsmanship': 1, 'Axe Mastery': 0, 'Shield Bash': 0},
            'Mage': {'Arcane Magic': 1, 'Elemental Magic': 0, 'Summoning': 0},
            'Rogue': {'Stealth': 1, 'Lockpicking': 0, 'Pickpocket': 0},
            'Cleric': {'Healing': 1, 'Divine Magic': 0, 'Exorcism': 0}
        }
        self.skills = skill_sets[self.class_type]

    def level_up(self):
        self.level += 1
        self.experience = 0
        for attr in self.attributes:
            self.attributes[attr] += random.randint(1, 3)
        
        skill_to_improve = random.choice(list(self.skills.keys()))
        self.skills[skill_to_improve] += 1

    def gain_experience(self, amount):
        self.experience += amount
        if self.experience >= self.level * 100:
            self.level_up()

    def customize(self, attribute_changes, skill_changes):
        for attr, value in attribute_changes.items():
            if attr in self.attributes:
                self.attributes[attr] += value
        for skill, value in skill_changes.items():
            if skill in self.skills:
                self.skills[skill] += value

    def generate_appearance(self):
        self.appearance = {
            'race': random.choice(['Human', 'Elf', 'Dwarf', 'Orc']),
            'gender': random.choice(['Male', 'Female']),
            'hair_color': random.choice(['Brown', 'Black', 'Blonde', 'Red']),
            'eye_color': random.choice(['Brown', 'Blue', 'Green', 'Grey']),
            'height': random.randint(150, 200),
            'weight': random.randint(50, 100)
        }

    def generate_personality(self):
        traits = ['Brave', 'Wise', 'Loyal', 'Mischievous', 'Confident', 'Shy', 'Arrogant', 'Compassionate']
        self.personality['traits'] = random.sample(traits, 2)
        self.personality['flaw'] = random.choice(['Greedy', 'Cowardly', 'Impatient', 'Jealous'])
        self.personality['virtue'] = random.choice(['Honest', 'Loyal', 'Brave', 'Compassionate', 'Generous'])

    def generate_background(self):
        backgrounds = [
            "Born into a noble family, {name} was trained from a young age in the art of {class_type}.",
            "Orphaned at a young age, {name} learned the ways of the {class_type} to survive on the streets.",
            "Raised in a secluded monastery, {name} honed their skills as a {class_type} through rigorous training.",
            "A former soldier, {name} now uses their {class_type} skills to seek adventure and fortune."
        ]
        self.background = random.choice(backgrounds).format(name=self.name, class_type=self.class_type)

    def generate_goal(self):
        goals = [
            "Become the greatest {class_type} in the land",
            "Avenge the death of a loved one",
            "Discover an ancient artifact of immense power",
            "Establish a guild of skilled {class_type}s",
            "Explore uncharted territories and make new discoveries"
        ]
        self.goals.append(random.choice(goals).format(class_type=self.class_type))

def generate_character(name, class_type):
    character = Character(name, class_type)
    character.generate_attributes()
    character.generate_skills()
    character.generate_appearance()
    character.generate_personality()
    character.generate_background()
    character.generate_goal()
    return character

def generate_npc(npc_type):
    npc = generate_character(generate_random_name(), random.choice(['Warrior', 'Mage', 'Rogue', 'Cleric']))
    npc.npc_type = npc_type
    
    if npc_type == "merchant":
        npc.skills['Bargaining'] = random.randint(1, 5)
        npc.skills['Appraisal'] = random.randint(1, 5)
    elif npc_type == "guard":
        npc.skills['Perception'] = random.randint(1, 5)
        npc.skills['Intimidation'] = random.randint(1, 5)
    
    return npc

def generate_random_name():
    first_names = ['Alice', 'Bob', 'Charlie', 'Diana', 'Ethan', 'Fiona', 'George', 'Hannah']
    last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis']
    return f"{random.choice(first_names)} {random.choice(last_names)}"

if __name__ == "__main__":
    # Test character generation
    player_character = generate_character("Aria", "Mage")
    print(f"Generated character: {player_character.name}, the {player_character.class_type}")
    print(f"Attributes: {player_character.attributes}")
    print(f"Skills: {player_character.skills}")
    print(f"Appearance: {player_character.appearance}")
    print(f"Personality: {player_character.personality}")
    print(f"Background: {player_character.background}")
    print(f"Goal: {player_character.goals[0]}")

    # Test NPC generation
    npc = generate_npc("merchant")
    print(f"\nGenerated NPC: {npc.name}, the {npc.npc_type}")
    print(f"Attributes: {npc.attributes}")
    print(f"Skills: {npc.skills}")
