import random
import numpy as np
from scipy import ndimage

def generate_terrain(width, height):
    noise = np.random.randn(width, height)
    smoothed_noise = ndimage.gaussian_filter(noise, sigma=2)
    return smoothed_noise

def generate_city(width, height):
    # Generate random terrain
    terrain = generate_terrain(width, height)

    # Determine city shape and size
    city_center = (random.randint(0, width - 1), random.randint(0, height - 1))
    city_radius = random.randint(10, 30)

    # Initialize city map
    city_map = [[' ' for _ in range(width)] for _ in range(height)]

    # Generate city layout
    for y in range(height):
        for x in range(width):
            distance = ((x - city_center[0])**2 + (y - city_center[1])**2)**0.5
            if distance <= city_radius:
                if distance <= city_radius * 0.2:
                    city_map[y][x] = 'C'  # City center
                elif distance <= city_radius * 0.6:
                    city_map[y][x] = 'U'  # Urban area
                else:
                    city_map[y][x] = 'S'  # Suburbs

    # Generate roads
    for _ in range(random.randint(3, 6)):
        start = (random.randint(0, width-1), random.randint(0, height-1))
        end = (random.randint(0, width-1), random.randint(0, height-1))
        generate_road(city_map, start, end)

    # Place important buildings
    place_important_buildings(city_map, width, height)

    return city_map, terrain

def generate_road(city_map, start, end):
    x, y = start
    while (x, y) != end:
        if x < end[0]:
            x += 1
        elif x > end[0]:
            x -= 1
        elif y < end[1]:
            y += 1
        elif y > end[1]:
            y -= 1
        if 0 <= x < len(city_map[0]) and 0 <= y < len(city_map):
            city_map[y][x] = 'R'

def place_important_buildings(city_map, width, height):
    buildings = ['T', 'M', 'P', 'H']  # Town Hall, Market, Palace, Harbor
    for building in buildings:
        x, y = random.randint(0, width-1), random.randint(0, height-1)
        while city_map[y][x] not in ['C', 'U']:
            x, y = random.randint(0, width-1), random.randint(0, height-1)
        city_map[y][x] = building

def print_city(city_map):
    for row in city_map:
        print(''.join(row))

if __name__ == "__main__":
    city_map, _ = generate_city(50, 50)
    print_city(city_map)
