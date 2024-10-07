import random

def generate_random_quest():
    quest_types = ["Fetch", "Kill", "Escort", "Explore"]
    quest_type = random.choice(quest_types)
    # ... more quest generation logic
    return quest_type
