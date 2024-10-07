import random
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage

def generate_terrain(width, height):
    noise = np.random.randn(width, height)
    smoothed_noise = ndimage.gaussian_filter(noise, sigma=2)
    return smoothed_noise

def generate_biomes(terrain):
    biomes = np.zeros_like(terrain)
    # ... implement biome assignment based on terrain height, etc.
    return biomes

def generate_landmarks(world_map, world_width, world_height):
    num_landmarks = 10  # Adjust number of landmarks
    for _ in range(num_landmarks):
        x = random.randint(0, world_width - 1)
        y = random.randint(0, world_height - 1)
        landmark_type = random.choice(["city", "dungeon", "forest", "mountain"])
        world_map[y][x] = f"{world_map[y][x]}_{landmark_type}"
    return world_map

def generate_elevation(world_map, world_width, world_height):
    for x in range(world_width):
        for y in range(world_height):
            elevation = random.randint(0, 10)  # Adjust elevation range
            world_map[y][x] = {"biome": world_map[y][x], "elevation": elevation}
    return world_map

def generate_rivers(world_map, world_width, world_height):
    for _ in range(5):  # Adjust number of rivers
        river_start = (random.randint(0, world_width - 1), random.randint(0, world_height - 1))
        river_end = (random.randint(0, world_width - 1), random.randint(0, world_height - 1))
        # Implement river generation logic (e.g., using Dijkstra's algorithm)
    return world_map

def generate_point_of_interest(biome):
    point_of_interest_types = {
        "forest": ["village", "clearing", "ancient ruins"],
        "desert": ["oasis", "bandit camp", "hidden treasure"],
        # ... other biome-specific point of interest types
    }
    if biome in point_of_interest_types:
        return random.choice(point_of_interest_types[biome])
    return "generic point of interest"

def generate_world(width, height):
    terrain = generate_terrain(width, height)
    biomes = generate_biomes(terrain)
    world_map = biomes.tolist()  # Convert numpy array to list for easier manipulation
    
    world_map = generate_landmarks(world_map, width, height)
    world_map = generate_elevation(world_map, width, height)
    world_map = generate_rivers(world_map, width, height)
    
    # Generate points of interest
    for y in range(height):
        for x in range(width):
            if random.random() < 0.1:  # 10% chance of point of interest
                poi = generate_point_of_interest(world_map[y][x]['biome'])
                world_map[y][x]['point_of_interest'] = poi
    
    return world_map, terrain, biomes

def visualize_world(terrain, biomes):
    plt.figure(figsize=(12, 5))
    
    plt.subplot(121)
    plt.imshow(terrain, cmap='terrain')
    plt.title('Terrain')
    
    plt.subplot(122)
    plt.imshow(biomes)
    plt.title('Biomes')
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    width, height = 100, 100
    world_map, terrain, biomes = generate_world(width, height)
    visualize_world(terrain, biomes)

import random
import numpy as np
from scipy import ndimage

def generate_terrain(width, height):
    noise = np.random.randn(width, height)
    smoothed_noise = ndimage.gaussian_filter(noise, sigma=2)
    return smoothed_noise

def generate_biomes(terrain, width, height):
    biomes = {
        "forest": {"temperature": "moderate", "humidity": "high", "terrain": "flat"},
        "desert": {"temperature": "hot", "humidity": "low", "terrain": "sandy"},
        "mountain": {"temperature": "cold", "humidity": "low", "terrain": "rocky"},
        "grassland": {"temperature": "moderate", "humidity": "moderate", "terrain": "flat"},
        "tundra": {"temperature": "cold", "humidity": "low", "terrain": "flat"},
        "swamp": {"temperature": "moderate", "humidity": "very high", "terrain": "wet"},
    }

    world_map = [['' for _ in range(width)] for _ in range(height)]

    for y in range(height):
        for x in range(width):
            elevation = terrain[y][x]
            if elevation > 0.7:
                world_map[y][x] = "mountain"
            elif elevation < -0.3:
                world_map[y][x] = "swamp"
            elif -0.3 <= elevation < 0:
                world_map[y][x] = "desert"
            elif 0 <= elevation < 0.3:
                world_map[y][x] = "grassland"
            elif 0.3 <= elevation < 0.7:
                world_map[y][x] = "forest"
            else:
                world_map[y][x] = random.choice(list(biomes.keys()))

    return world_map, biomes

def generate_landmarks(world_map, width, height):
    landmarks = {
        "forest": ["ancient tree", "elven city", "druid circle"],
        "desert": ["oasis", "pyramid", "hidden tomb"],
        "mountain": ["dwarven fortress", "dragon lair", "abandoned mine"],
        "grassland": ["human settlement", "ancient battlefield", "trading post"],
        "tundra": ["ice castle", "frozen lake", "mammoth graveyard"],
        "swamp": ["witch's hut", "sunken temple", "will-o'-wisp marsh"]
    }

    for _ in range(int(width * height * 0.01)):  # Generate landmarks for 1% of the map
        x, y = random.randint(0, width - 1), random.randint(0, height - 1)
        biome = world_map[y][x]
        if biome in landmarks:
            landmark = random.choice(landmarks[biome])
            world_map[y][x] = f"{biome}_{landmark}"

    return world_map

def generate_rivers(world_map, width, height):
    num_rivers = random.randint(1, 5)
    for _ in range(num_rivers):
        x, y = random.randint(0, width - 1), random.randint(0, height - 1)
        length = random.randint(10, 30)
        for _ in range(length):
            if 0 <= x < width and 0 <= y < height:
                world_map[y][x] = f"{world_map[y][x]}_river"
            direction = random.choice(['n', 's', 'e', 'w'])
            if direction == 'n': y -= 1
            elif direction == 's': y += 1
            elif direction == 'e': x += 1
            else: x -= 1

    return world_map

def generate_world(width=100, height=100):
    """Generates a more complex RPG world with enhanced features."""
    print("Generating terrain...")
    terrain = generate_terrain(width, height)
    
    print("Generating biomes...")
    world_map, biomes = generate_biomes(terrain, width, height)
    
    print("Generating landmarks...")
    world_map = generate_landmarks(world_map, width, height)
    
    print("Generating rivers...")
    world_map = generate_rivers(world_map, width, height)
    
    return world_map, biomes, terrain

def print_world_summary(world_map, biomes):
    biome_counts = {biome: sum(row.count(biome) for row in world_map) for biome in biomes}
    landmark_counts = sum(1 for row in world_map for cell in row if '_' in cell)
    river_count = sum(1 for row in world_map for cell in row if 'river' in cell)

    print("\nWorld Summary:")
    print(f"Dimensions: {len(world_map[0])}x{len(world_map)}")
    print("\nBiome Distribution:")
    for biome, count in biome_counts.items():
        print(f"  {biome.capitalize()}: {count}")
    print(f"\nTotal Landmarks: {landmark_counts}")
    print(f"Total River Tiles: {river_count}")

if __name__ == "__main__":
    world_map, biomes, terrain = generate_world()
    print_world_summary(world_map, biomes)

# ... (previous imports and functions)

from CityGenerator import generate_city

def generate_cities(world_map, width, height, num_cities=5):
    cities = []
    for _ in range(num_cities):
        city_x, city_y = random.randint(0, width-1), random.randint(0, height-1)
        while world_map[city_y][city_x] in ['mountain', 'water']:
            city_x, city_y = random.randint(0, width-1), random.randint(0, height-1)
        
        city_size = random.randint(20, 40)
        city_map, _ = generate_city(city_size, city_size)
        
        # Place city on world map
        for y in range(city_size):
            for x in range(city_size):
                if 0 <= city_y + y < height and 0 <= city_x + x < width:
                    if city_map[y][x] != ' ':
                        world_map[city_y + y][city_x + x] = f"city_{city_map[y][x]}"
        
        cities.append((city_x, city_y, city_size))
    
    return world_map, cities

def generate_world(width=100, height=100):
    """Generates a more complex RPG world with enhanced features."""
    print("Generating terrain...")
    terrain = generate_terrain(width, height)
    
    print("Generating biomes...")
    world_map, biomes = generate_biomes(terrain, width, height)
    
    print("Generating landmarks...")
    world_map = generate_landmarks(world_map, width, height)
    
    print("Generating rivers...")
    world_map = generate_rivers(world_map, width, height)
    
    print("Generating cities...")
    world_map, cities = generate_cities(world_map, width, height)
    
    return world_map, biomes, terrain, cities

def print_world_summary(world_map, biomes, cities):
    # ... (previous summary code)
    
    print(f"\nTotal Cities: {len(cities)}")
    for i, (x, y, size) in enumerate(cities, 1):
        print(f"  City {i}: Located at ({x}, {y}), Size: {size}x{size}")

if __name__ == "__main__":
    world_map, biomes, terrain, cities = generate_world()
    print_world_summary(world_map, biomes, cities)

# ... (previous imports and functions)

from DungeonGenerator import generate_dungeon

def generate_point_of_interest(biome):
    point_of_interest_types = {
        "forest": ["ancient tree", "elven city", "druid circle"],
        "desert": ["oasis", "pyramid", "hidden tomb"],
        "mountain": ["dwarven fortress", "dragon lair", "abandoned mine"],
        "grassland": ["human settlement", "ancient battlefield", "trading post"],
        "tundra": ["ice castle", "frozen lake", "mammoth graveyard"],
        "swamp": ["witch's hut", "sunken temple", "will-o'-wisp marsh"]
    }

    point_of_interest_type = random.choice(point_of_interest_types.get(biome, ["mysterious location"]))
    point_of_interest_size = random.randint(1, 5)  # Adjust size range
    
    return {"type": point_of_interest_type, "size": point_of_interest_size}

def generate_dungeons(world_map, width, height, num_dungeons=3):
    dungeons = []
    for _ in range(num_dungeons):
        dungeon_x, dungeon_y = random.randint(0, width-1), random.randint(0, height-1)
        while world_map[dungeon_y][dungeon_x] in ['water', 'city_C', 'city_U', 'city_S']:
            dungeon_x, dungeon_y = random.randint(0, width-1), random.randint(0, height-1)
        
        dungeon_size = random.randint(20, 30)
        dungeon = generate_dungeon(dungeon_size, dungeon_size)
        
        # Place dungeon on world map
        for y in range(dungeon_size):
            for x in range(dungeon_size):
                if 0 <= dungeon_y + y < height and 0 <= dungeon_x + x < width:
                    if dungeon[y][x] != 0:
                        world_map[dungeon_y + y][dungeon_x + x] = f"dungeon_{dungeon[y][x]}"
        
        dungeons.append((dungeon_x, dungeon_y, dungeon_size))
    
    return world_map, dungeons

def generate_world(width=100, height=100):
    """Generates a more complex RPG world with enhanced features."""
    print("Generating terrain...")
    terrain = generate_terrain(width, height)
    
    print("Generating biomes...")
    world_map, biomes = generate_biomes(terrain, width, height)
    
    print("Generating landmarks...")
    world_map = generate_landmarks(world_map, width, height)
    
    print("Generating rivers...")
    world_map = generate_rivers(world_map, width, height)
    
    print("Generating cities...")
    world_map, cities = generate_cities(world_map, width, height)
    
    print("Generating dungeons...")
    world_map, dungeons = generate_dungeons(world_map, width, height)
    
    print("Generating points of interest...")
    points_of_interest = []
    for y in range(height):
        for x in range(width):
            if random.random() < 0.01:  # 1% chance of a point of interest
                biome = world_map[y][x].split('_')[0] if '_' in world_map[y][x] else world_map[y][x]
                poi = generate_point_of_interest(biome)
                world_map[y][x] = f"poi_{poi['type']}"
                points_of_interest.append((x, y, poi))
    
    return world_map, biomes, terrain, cities, dungeons, points_of_interest

def print_world_summary(world_map, biomes, cities, dungeons, points_of_interest):
    # ... (previous summary code)
    
    print(f"\nTotal Cities: {len(cities)}")
    for i, (x, y, size) in enumerate(cities, 1):
        print(f"  City {i}: Located at ({x}, {y}), Size: {size}x{size}")
    
    print(f"\nTotal Dungeons: {len(dungeons)}")
    for i, (x, y, size) in enumerate(dungeons, 1):
        print(f"  Dungeon {i}: Located at ({x}, {y}), Size: {size}x{size}")
    
    print(f"\nTotal Points of Interest: {len(points_of_interest)}")
    for i, (x, y, poi) in enumerate(points_of_interest, 1):
        print(f"  POI {i}: {poi['type']} at ({x}, {y}), Size: {poi['size']}")

if __name__ == "__main__":
    world_map, biomes, terrain, cities, dungeons, points_of_interest = generate_world()
    print_world_summary(world_map, biomes, cities, dungeons, points_of_interest)

# ... (previous imports and functions)

from content.Script.LoreGenerator import world_building_and_lore

def generate_world(width=100, height=100):
    """Generates a more complex RPG world with enhanced features and lore."""
    print("Generating terrain...")
    terrain = generate_terrain(width, height)
    
    print("Generating biomes...")
    world_map, biomes = generate_biomes(terrain, width, height)
    
    print("Generating landmarks...")
    world_map = generate_landmarks(world_map, width, height)
    
    print("Generating rivers...")
    world_map = generate_rivers(world_map, width, height)
    
    print("Generating cities...")
    world_map, cities = generate_cities(world_map, width, height)
    
    print("Generating dungeons...")
    world_map, dungeons = generate_dungeons(world_map, width, height)
    
    print("Generating points of interest...")
    points_of_interest = []
    for y in range(height):
        for x in range(width):
            if random.random() < 0.01:  # 1% chance of a point of interest
                biome = world_map[y][x].split('_')[0] if '_' in world_map[y][x] else world_map[y][x]
                poi = generate_point_of_interest(biome)
                world_map[y][x] = f"poi_{poi['type']}"
                points_of_interest.append((x, y, poi))
    
    print("Generating world lore...")
    world_details, lore = world_building_and_lore()
    
    return world_map, biomes, terrain, cities, dungeons, points_of_interest, world_details, lore

def print_world_summary(world_map, biomes, cities, dungeons, points_of_interest, world_details, lore):
    # ... (previous summary code)
    
    print("\nWorld Details:")
    for key, value in world_details.items():
        print(f"{key.capitalize()}: {value}")
    
    print("\nLore:")
    for item in lore:
        print(f"- {item}")

if __name__ == "__main__":
    world_map, biomes, terrain, cities, dungeons, points_of_interest, world_details, lore = generate_world()
    print_world_summary(world_map, biomes, cities, dungeons, points_of_interest, world_details, lore)

# ... (previous imports and functions)

from ItemGenerator import generate_random_item

def generate_world(width=100, height=100):
    """Generates a more complex RPG world with enhanced features, lore, and items."""
    # ... (previous world generation code)

    print("Generating items...")
    items = [generate_random_item() for _ in range(100)]  # Generate 100 random items

    return world_map, biomes, terrain, cities, dungeons, points_of_interest, world_details, lore, items

def print_world_summary(world_map, biomes, cities, dungeons, points_of_interest, world_details, lore, items):
    # ... (previous summary code)

    print("\nGenerated Items:")
    for i, item in enumerate(items[:10], 1):  # Print first 10 items
        print(f"Item {i}: {item['name']} ({item['rarity']} {item['type']})")

if __name__ == "__main__":
    world_map, biomes, terrain, cities, dungeons, points_of_interest, world_details, lore, items = generate_world()
    print_world_summary(world_map, biomes, cities, dungeons, points_of_interest, world_details, lore, items)

# ... (previous imports and functions)

from content.Script.CharacterGenerator import generate_character

def generate_world(width=100, height=100, num_characters=50):
    """Generates a more complex RPG world with enhanced features, lore, items, and characters."""
    # ... (previous world generation code)

    print("Generating characters...")
    characters = [generate_character() for _ in range(num_characters)]

    return world_map, biomes, terrain, cities, dungeons, points_of_interest, world_details, lore, items, characters

def print_world_summary(world_map, biomes, cities, dungeons, points_of_interest, world_details, lore, items, characters):
    # ... (previous summary code)

    print("\nGenerated Characters:")
    for i, character in enumerate(characters[:10], 1):  # Print first 10 characters
        print(f"Character {i}: {character['name']} ({character['appearance']['race']} {character['background']})")

if __name__ == "__main__":
    world_map, biomes, terrain, cities, dungeons, points_of_interest, world_details, lore, items, characters = generate_world()
    print_world_summary(world_map, biomes, cities, dungeons, points_of_interest, world_details, lore, items, characters)

# ... (previous imports and functions)

from DungeonGenerator import generate_dungeon

def generate_world(width=100, height=100, num_characters=50, num_dungeons=5):
    """Generates a more complex RPG world with enhanced features, lore, items, characters, and dungeons."""
    # ... (previous world generation code)

    print("Generating dungeons...")
    dungeons = []
    for _ in range(num_dungeons):
        dungeon_type = random.choice(['bsp', 'maze'])
        dungeon_width = random.randint(20, 50)
        dungeon_height = random.randint(20, 50)
        dungeon_layout = generate_dungeon(dungeon_width, dungeon_height, dungeon_type)
        
        # Find a suitable location for the dungeon
        while True:
            x = random.randint(0, width - dungeon_width)
            y = random.randint(0, height - dungeon_height)
            if all(world_map[y+dy][x+dx] not in ['water', 'city_C', 'city_U', 'city_S'] 
                   for dy in range(dungeon_height) for dx in range(dungeon_width)):
                break
        
        # Place the dungeon on the world map
        for dy in range(dungeon_height):
            for dx in range(dungeon_width):
                if dungeon_layout[dy][dx] == 0:  # Open space in dungeon
                    world_map[y+dy][x+dx] = 'dungeon_floor'
                elif dungeon_layout[dy][dx] == 1:  # Wall in dungeon
                    world_map[y+dy][x+dx] = 'dungeon_wall'
        
        dungeons.append({
            'x': x,
            'y': y,
            'width': dungeon_width,
            'height': dungeon_height,
            'type': dungeon_type,
            'layout': dungeon_layout
        })

    return world_map, biomes, terrain, cities, dungeons, points_of_interest, world_details, lore, items, characters

def print_world_summary(world_map, biomes, cities, dungeons, points_of_interest, world_details, lore, items, characters):
    # ... (previous summary code)

    print("\nGenerated Dungeons:")
    for i, dungeon in enumerate(dungeons, 1):
        print(f"Dungeon {i}: Type: {dungeon['type']}, Size: {dungeon['width']}x{dungeon['height']}, Location: ({dungeon['x']}, {dungeon['y']})")

if __name__ == "__main__":
    world_map, biomes, terrain, cities, dungeons, points_of_interest, world_details, lore, items, characters = generate_world()
    print_world_summary(world_map, biomes, cities, dungeons, points_of_interest, world_details, lore, items, characters)

# ... (previous imports and functions)

from DungeonGenerator import generate_dungeon

def generate_world(width=100, height=100, num_characters=50, num_dungeons=5):
    """Generates a more complex RPG world with enhanced features, lore, items, characters, and dungeons."""
    # ... (previous world generation code)

    print("Generating dungeons...")
    dungeons = []
    for _ in range(num_dungeons):
        dungeon_type = random.choice(['bsp', 'maze'])
        dungeon_width = random.randint(20, 50)
        dungeon_height = random.randint(20, 50)
        dungeon_layout = generate_dungeon(dungeon_width, dungeon_height, dungeon_type)
        
        # Find a suitable location for the dungeon
        while True:
            x = random.randint(0, width - dungeon_width)
            y = random.randint(0, height - dungeon_height)
            if all(world_map[y+dy][x+dx] not in ['water', 'city_C', 'city_U', 'city_S'] 
                   for dy in range(dungeon_height) for dx in range(dungeon_width)):
                break
        
        # Place the dungeon on the world map
        for dy in range(dungeon_height):
            for dx in range(dungeon_width):
                if dungeon_layout[dy][dx] == 0:  # Open space in dungeon
                    world_map[y+dy][x+dx] = 'dungeon_floor'
                elif dungeon_layout[dy][dx] == 1:  # Wall in dungeon
                    world_map[y+dy][x+dx] = 'dungeon_wall'
        
        dungeons.append({
            'x': x,
            'y': y,
            'width': dungeon_width,
            'height': dungeon_height,
            'type': dungeon_type,
            'layout': dungeon_layout
        })

    return world_map, biomes, terrain, cities, dungeons, points_of_interest, world_details, lore, items, characters

def print_world_summary(world_map, biomes, cities, dungeons, points_of_interest, world_details, lore, items, characters):
    # ... (previous summary code)

    print("\nGenerated Dungeons:")
    for i, dungeon in enumerate(dungeons, 1):
        print(f"Dungeon {i}: Type: {dungeon['type']}, Size: {dungeon['width']}x{dungeon['height']}, Location: ({dungeon['x']}, {dungeon['y']})")

if __name__ == "__main__":
    world_map, biomes, terrain, cities, dungeons, points_of_interest, world_details, lore, items, characters = generate_world()
    print_world_summary(world_map, biomes, cities, dungeons, points_of_interest, world_details, lore, items, characters)

# ... (previous imports and functions)

from ItemGenerator import generate_random_item

def generate_world(width=100, height=100, num_characters=50, num_dungeons=5, num_items=100):
    """Generates a more complex RPG world with enhanced features, lore, items, characters, and dungeons."""
    # ... (previous world generation code)

    print("Generating items...")
    items = [generate_random_item(random.randint(1, 20)) for _ in range(num_items)]

    # ... (rest of the world generation code)

    return world_map, biomes, terrain, cities, dungeons, points_of_interest, world_details, lore, items, characters

def print_world_summary(world_map, biomes, cities, dungeons, points_of_interest, world_details, lore, items, characters):
    # ... (previous summary code)

    print("\nGenerated Items:")
    for i, item in enumerate(items[:10], 1):  # Print first 10 items
        print(f"Item {i}: {item.name} (Level {item.level} {item.rarity} {item.item_type})")

# ... (rest of the WorldGenerator code)
