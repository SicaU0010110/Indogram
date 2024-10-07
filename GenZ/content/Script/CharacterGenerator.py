import random

def generate_character():
    """Generates a comprehensive character with random attributes, skills, appearance, and backstory."""
    
    # Attributes
    attributes = {
        "strength": random.randint(1, 20),
        "dexterity": random.randint(1, 20),
        "constitution": random.randint(1, 20),
        "intelligence": random.randint(1, 20),
        "wisdom": random.randint(1, 20),
        "charisma": random.randint(1, 20),
        "luck": random.randint(1, 20)
    }

    # Skills
    all_skills = ["swordsmanship", "magic", "stealth", "healing", "crafting", "perception"]
    skills = {skill: random.randint(1, 50) for skill in random.sample(all_skills, random.randint(3, 5))}

    # Appearance
    races = ["human", "elf", "dwarf", "orc", "halfling", "gnome"]
    appearance = {
        "race": random.choice(races),
        "gender": random.choice(["male", "female"]),
        "hair_color": random.choice(["brown", "black", "blonde", "red"]),
        "eye_color": random.choice(["brown", "blue", "green", "grey"]),
        "height": random.randint(150, 200),  # in cm
        "weight": random.randint(50, 100)  # in kg
    }

    # Background and Personality
    backgrounds = ["noble", "commoner", "adventurer", "soldier", "rogue", "scholar"]
    personality_traits = ["brave", "wise", "loyal", "mischievous", "confident", "shy"]
    motivations = ["wealth", "power", "knowledge", "revenge", "love", "adventure"]

    character = {
        "attributes": attributes,
        "skills": skills,
        "appearance": appearance,
        "background": random.choice(backgrounds),
        "personality": random.choice(personality_traits),
        "motivation": random.choice(motivations)
    }

    # Generate a name for the character
    character["name"] = generate_character_name(character["appearance"]["race"])

    return character

def generate_character_name(race):
    """Generates a name based on the character's race."""
    name_parts = {
        "human": (["John", "Mary", "Michael", "Sarah", "David", "Emma"], ["Smith", "Johnson", "Williams", "Brown", "Jones"]),
        "elf": (["Aelindra", "Caelynn", "Thaelar", "Sylindra", "Faelar"], ["Moonwhisper", "Starweaver", "Sunseeker", "Nightwalker"]),
        "dwarf": (["Thorin", "Dwalin", "Balin", "Gloin", "Oin"], ["Ironforge", "Stonehammer", "Goldbeard", "Copperheart"]),
        "orc": (["Grok", "Thokk", "Morg", "Durg", "Zug"], ["the Mighty", "Bonecrusher", "Skullsplitter", "Ironhide"]),
        "halfling": (["Bilbo", "Frodo", "Sam", "Merry", "Pippin"], ["Baggins", "Gamgee", "Brandybuck", "Took"]),
        "gnome": (["Fizban", "Gimble", "Namfoodle", "Zook", "Dabbledob"], ["Beren", "Nackle", "Raulnor", "Scheppen", "Timbers"])
    }

    first_names, last_names = name_parts.get(race, name_parts["human"])
    return f"{random.choice(first_names)} {random.choice(last_names)}"

def allow_customization(character):
    """Placeholder for character customization functionality."""
    print("Character customization would be implemented here.")
    return character

if __name__ == "__main__":
    # Test the character generation
    for _ in range(5):
        character = generate_character()
        print(f"Generated Character: {character['name']}")
        print(f"Race: {character['appearance']['race']}, Gender: {character['appearance']['gender']}")
        print(f"Background: {character['background']}, Personality: {character['personality']}")
        print(f"Motivation: {character['motivation']}")
        print(f"Attributes: {character['attributes']}")
        print(f"Skills: {character['skills']}")
        print()
