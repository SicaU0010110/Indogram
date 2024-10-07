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

if __name__ == "__main__":
    game_loop()

def combat(player, enemy):
    print(f"Combat started between {player.name} and {enemy.name}!")
    while player.is_alive() and enemy.is_alive():
        # Player's turn
        print(f"\n{player.name}'s turn:")
        player.attack(enemy)
        enemy.display_health()
        
        if not enemy.is_alive():
            print(f"{player.name} has defeated {enemy.name}!")
            exp_gain = random.randint(20, 50)
            player.gain_experience(exp_gain)
            loot = generate_item(f"{enemy.name}'s Loot", player.level)
            player.add_item_to_inventory(loot)
            print(f"You found: {loot.name}")
            break
        
        # Enemy's turn
        print(f"\n{enemy.name}'s turn:")
        enemy.attack(player)
        player.display_health()
        
        if not player.is_alive():
            print(f"{player.name} has been defeated by {enemy.name}!")
            break
