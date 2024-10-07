import random

def generate_random_world_details():
    """Generates random details for the world."""
    cultures = [
        ("Elven Kingdom", "Ancient and magical"),
        ("Dwarven Clans", "Masters of stone and metal"),
        ("Human Empire", "Ambitious and expansive"),
        ("Orcish Hordes", "Fierce and nomadic"),
        ("Merfolk Alliance", "Guardians of the seas")
    ]

    conflicts = [
        ("The Great War", "A century-long conflict that reshaped the continent"),
        ("The Magical Plague", "A mysterious illness that affects magical beings"),
        ("The Resource Crisis", "Dwindling resources leading to territorial disputes"),
        ("The Divine Schism", "A religious divide that threatens the fabric of society"),
        ("The Technological Revolution", "Rapid advancements causing societal upheaval")
    ]

    historical_events = [
        "the fall of the ancient dragon empire",
        "the discovery of a new continent",
        "the rise of a powerful archmage",
        "the awakening of an elder god",
        "the forging of the world's most powerful artifact"
    ]

    return {
        "cultures": random.sample(cultures, 3),
        "conflicts": random.sample(conflicts, 2),
        "history": random.choice(historical_events)
    }

def generate_lore(world_details):
    """Generates basic lore based on world details."""
    lore = []
    for culture in world_details["cultures"]:
        for conflict in world_details["conflicts"]:
            lore.append(f"{culture[0]} involved in {conflict[0]} due to {world_details['history']}")
    
    # Add some random events and legends
    legends = [
        f"The legend of the {random.choice(['lost', 'hidden', 'sunken'])} city of {random.choice(['Eldoria', 'Mystara', 'Zephyria'])}",
        f"The prophecy of the {random.choice(['chosen one', 'world-ender', 'peace-bringer'])}",
        f"The curse of the {random.choice(['ancient king', 'forgotten queen', 'mad wizard'])}"
    ]
    lore.extend(random.sample(legends, 2))

    return lore

def world_building_and_lore():
    """Creates a rich world with randomly generated lore."""
    world_details = generate_random_world_details()
    lore = generate_lore(world_details)
    return world_details, lore

if __name__ == "__main__":
    world_details, lore = world_building_and_lore()
    print("World Details:")
    for key, value in world_details.items():
        print(f"{key.capitalize()}: {value}")
    print("\nLore:")
    for item in lore:
        print(f"- {item}")
