import random

monsters = {
    "forest": [("Goblin", 50, 10), ("Wolf", 40, 8)],
    "desert": [("Scorpion", 60, 12), ("Sand Worm", 80, 15)],
    "village": [("Bandit", 70, 14), ("Thief", 50, 10)],
    "castle": [("Knight", 90, 18), ("Dragon", 150, 25)]
}

areas = ["forest", "desert", "village", "castle"]

def generate_enemy(player_level, area):
    base_monster = random.choice(monsters[area])
    name, base_health, base_attack = base_monster
    health = base_health + (player_level * 10)
    attack = base_attack + (player_level * 2)
    return Character(name, health, attack)

def generate_quest(player_level, area):
    base_quest = random.choice(quests[area])
    name, description, base_reward = base_quest
    reward = f"{int(base_reward.split()[0]) + (player_level * 10)} gold"
    return Quest(name, description, reward)
