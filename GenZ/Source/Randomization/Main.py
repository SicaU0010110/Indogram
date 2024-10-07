from character import Character
from combat import combat
from quests import Quest, QuestLog
from items import Item, generate_item

from character import Character
from combat import combat
from quests import Quest, QuestLog
from items import Item, generate_item
from world import generate_enemy, generate_quest, areas
from crafting import implement_crafting_system

def game_loop():
    player = Character("Hero", 100, 20)
    quest_log = QuestLog()
    
    while True:
        command = input("Enter command (explore, fight, quest, craft, inventory, quit): ").strip().lower()
        
        if command == "explore":
            area = random.choice(areas)
            enemy = generate_enemy(player.level, area)
            print(f"You explore the {area} and find a {enemy.name}!")
            combat(player, enemy)
        
        elif command == "fight":
            area = random.choice(areas)
            enemy = generate_enemy(player.level, area)
            print(f"You engage in combat with a {enemy.name}!")
            combat(player, enemy)
        
        elif command == "quest":
            area = random.choice(areas)
            quest = generate_quest(player.level, area)
            quest_log.add_quest(quest)
        
        elif command == "craft":
            area = random.choice(areas)
            implement_crafting_system(player, area)
        
        elif command == "inventory":
            player.display_inventory()
        
        elif command == "quit":
            print("Exiting game.")
            break
        
        else:
            print("Invalid command.")
        
        if not player.is_alive():
            print("Game Over!")
            break

if __name__ == "__main__":
    game_loop()
