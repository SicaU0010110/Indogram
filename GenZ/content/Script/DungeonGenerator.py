import random

def generate_dungeon(width, height, birth_threshold=4, survival_threshold=4, num_iterations=5):
    grid = [[0 for _ in range(width)] for _ in range(height)]

    # Randomly initialize the grid
    for x in range(width):
        for y in range(height):
            grid[y][x] = 1 if random.random() < 0.5 else 0

    for _ in range(num_iterations):  # Number of generations
        new_grid = [[0 for _ in range(width)] for _ in range(height)]
        for x in range(1, width - 1):
            for y in range(1, height - 1):
                neighbors = sum(grid[y + i][x + j] for i in [-1, 0, 1] for j in [-1, 0, 1] if i != 0 or j != 0)
                if grid[y][x] == 1 and survival_threshold[0] <= neighbors <= survival_threshold[1]:
                    new_grid[y][x] = 1
                elif grid[y][x] == 0 and neighbors >= birth_threshold:
                    new_grid[y][x] = 1
        grid = new_grid

    # Add entrance and exit
    entrance = (random.randint(0, width-1), 0)
    exit = (random.randint(0, width-1), height-1)
    grid[entrance[1]][entrance[0]] = 2  # 2 represents entrance
    grid[exit[1]][exit[0]] = 3  # 3 represents exit

    return grid

def print_dungeon(dungeon):
    for row in dungeon:
        print(''.join(['#' if cell == 1 else 'E' if cell == 2 else 'X' if cell == 3 else '.' for cell in row]))

if __name__ == "__main__":
    dungeon = generate_dungeon(50, 50)
    print_dungeon(dungeon)

import random

class BSPNode:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.left = None
        self.right = None
        self.room = None

def generate_bsp(x, y, width, height, min_room_size):
    node = BSPNode(x, y, width, height)

    if width >= min_room_size * 2 and height >= min_room_size * 2:
        if random.random() < 0.5:
            # Split horizontally
            split = random.randint(y + min_room_size, y + height - min_room_size)
            node.left = generate_bsp(x, y, width, split - y, min_room_size)
            node.right = generate_bsp(x, split, width, y + height - split, min_room_size)
        else:
            # Split vertically
            split = random.randint(x + min_room_size, x + width - min_room_size)
            node.left = generate_bsp(x, y, split - x, height, min_room_size)
            node.right = generate_bsp(split, y, x + width - split, height, min_room_size)
    else:
        node.room = generate_random_room(node.x, node.y, node.width, node.height)

    return node

def generate_random_room(x, y, max_width, max_height):
    min_room_size = 4
    room_width = random.randint(min_room_size, min(max_width, 8))
    room_height = random.randint(min_room_size, min(max_height, 8))
    room_x = x + random.randint(0, max_width - room_width)
    room_y = y + random.randint(0, max_height - room_height)
    return {'x': room_x, 'y': room_y, 'width': room_width, 'height': room_height}

def generate_corridors(node):
    corridors = []
    if node.left and node.right:
        left_room = get_room(node.left)
        right_room = get_room(node.right)
        if left_room and right_room:
            corridors.append(connect_rooms(left_room, right_room))
        corridors.extend(generate_corridors(node.left))
        corridors.extend(generate_corridors(node.right))
    return corridors

def get_room(node):
    if node.room:
        return node.room
    left_room = get_room(node.left) if node.left else None
    right_room = get_room(node.right) if node.right else None
    return left_room or right_room

def connect_rooms(room1, room2):
    x1, y1 = room1['x'] + room1['width'] // 2, room1['y'] + room1['height'] // 2
    x2, y2 = room2['x'] + room2['width'] // 2, room2['y'] + room2['height'] // 2
    if random.random() < 0.5:
        return [
            {'x': x1, 'y': y1, 'x2': x2, 'y2': y1},
            {'x': x2, 'y': y1, 'x2': x2, 'y2': y2}
        ]
    else:
        return [
            {'x': x1, 'y': y1, 'x2': x1, 'y2': y2},
            {'x': x1, 'y': y2, 'x2': x2, 'y2': y2}
        ]

def generate_maze(width, height):
    maze = [[1 for _ in range(width)] for _ in range(height)]  # 1 represents a wall

    def dfs(x, y):
        maze[y][x] = 0  # Mark as visited
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = x + dx * 2, y + dy * 2
            if 0 <= nx < width and 0 <= ny < height and maze[ny][nx] == 1:
                maze[y + dy][x + dx] = 0  # Carve out a passage
                dfs(nx, ny)

    start_x, start_y = random.randint(0, width - 1) // 2 * 2, random.randint(0, height - 1) // 2 * 2
    dfs(start_x, start_y)
    return maze

def generate_dungeon(width, height, dungeon_type='bsp'):
    if dungeon_type == 'bsp':
        root = generate_bsp(0, 0, width, height, 5)
        rooms = []
        corridors = []

        def extract_rooms(node):
            if node.room:
                rooms.append(node.room)
            else:
                if node.left:
                    extract_rooms(node.left)
                if node.right:
                    extract_rooms(node.right)

        extract_rooms(root)
        corridors = generate_corridors(root)

        dungeon = [[1 for _ in range(width)] for _ in range(height)]
        for room in rooms:
            for y in range(room['y'], room['y'] + room['height']):
                for x in range(room['x'], room['x'] + room['width']):
                    dungeon[y][x] = 0

        for corridor in corridors:
            for segment in corridor:
                x1, y1, x2, y2 = segment['x'], segment['y'], segment['x2'], segment['y2']
                if x1 == x2:
                    for y in range(min(y1, y2), max(y1, y2) + 1):
                        dungeon[y][x1] = 0
                else:
                    for x in range(min(x1, x2), max(x1, x2) + 1):
                        dungeon[y1][x] = 0

    elif dungeon_type == 'maze':
        dungeon = generate_maze(width, height)

    return dungeon

if __name__ == "__main__":
    # Test the dungeon generation
    dungeon = generate_dungeon(50, 50, 'bsp')
    for row in dungeon:
        print(''.join(['#' if cell else '.' for cell in row]))

    print("\nMaze Dungeon:")
    maze_dungeon = generate_dungeon(25, 25, 'maze')
    for row in maze_dungeon:
        print(''.join(['#' if cell else '.' for cell in row]))

import random

class BSPNode:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.left = None
        self.right = None
        self.room = None

def generate_bsp(x, y, width, height, min_room_size):
    node = BSPNode(x, y, width, height)

    if width >= min_room_size * 2 and height >= min_room_size * 2:
        if random.random() < 0.5:
            # Split horizontally
            split = random.randint(y + min_room_size, y + height - min_room_size)
            node.left = generate_bsp(x, y, width, split - y, min_room_size)
            node.right = generate_bsp(x, split, width, y + height - split, min_room_size)
        else:
            # Split vertically
            split = random.randint(x + min_room_size, x + width - min_room_size)
            node.left = generate_bsp(x, y, split - x, height, min_room_size)
            node.right = generate_bsp(split, y, x + width - split, height, min_room_size)
    else:
        node.room = generate_random_room(node.x, node.y, node.width, node.height)

    return node

def generate_random_room(x, y, max_width, max_height):
    min_room_size = 4
    room_width = random.randint(min_room_size, min(max_width, 8))
    room_height = random.randint(min_room_size, min(max_height, 8))
    room_x = x + random.randint(0, max_width - room_width)
    room_y = y + random.randint(0, max_height - room_height)
    return {'x': room_x, 'y': room_y, 'width': room_width, 'height': room_height}

def generate_corridors(node):
    corridors = []
    if node.left and node.right:
        left_room = get_room(node.left)
        right_room = get_room(node.right)
        if left_room and right_room:
            corridors.append(connect_rooms(left_room, right_room))
        corridors.extend(generate_corridors(node.left))
        corridors.extend(generate_corridors(node.right))
    return corridors

def get_room(node):
    if node.room:
        return node.room
    left_room = get_room(node.left) if node.left else None
    right_room = get_room(node.right) if node.right else None
    return left_room or right_room

def connect_rooms(room1, room2):
    x1, y1 = room1['x'] + room1['width'] // 2, room1['y'] + room1['height'] // 2
    x2, y2 = room2['x'] + room2['width'] // 2, room2['y'] + room2['height'] // 2
    if random.random() < 0.5:
        return [
            {'x': x1, 'y': y1, 'x2': x2, 'y2': y1},
            {'x': x2, 'y': y1, 'x2': x2, 'y2': y2}
        ]
    else:
        return [
            {'x': x1, 'y': y1, 'x2': x1, 'y2': y2},
            {'x': x1, 'y': y2, 'x2': x2, 'y2': y2}
        ]

def generate_maze(width, height):
    maze = [[1 for _ in range(width)] for _ in range(height)]  # 1 represents a wall

    def dfs(x, y):
        maze[y][x] = 0  # Mark as visited
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = x + dx * 2, y + dy * 2
            if 0 <= nx < width and 0 <= ny < height and maze[ny][nx] == 1:
                maze[y + dy][x + dx] = 0  # Carve out a passage
                dfs(nx, ny)

    start_x, start_y = random.randint(0, width - 1) // 2 * 2, random.randint(0, height - 1) // 2 * 2
    dfs(start_x, start_y)
    return maze

def generate_dungeon(width, height, dungeon_type='bsp'):
    if dungeon_type == 'bsp':
        root = generate_bsp(0, 0, width, height, 5)
        rooms = []
        corridors = []

        def extract_rooms(node):
            if node.room:
                rooms.append(node.room)
            else:
                if node.left:
                    extract_rooms(node.left)
                if node.right:
                    extract_rooms(node.right)

        extract_rooms(root)
        corridors = generate_corridors(root)

        dungeon = [[1 for _ in range(width)] for _ in range(height)]
        for room in rooms:
            for y in range(room['y'], room['y'] + room['height']):
                for x in range(room['x'], room['x'] + room['width']):
                    dungeon[y][x] = 0

        for corridor in corridors:
            for segment in corridor:
                x1, y1, x2, y2 = segment['x'], segment['y'], segment['x2'], segment['y2']
                if x1 == x2:
                    for y in range(min(y1, y2), max(y1, y2) + 1):
                        dungeon[y][x1] = 0
                else:
                    for x in range(min(x1, x2), max(x1, x2) + 1):
                        dungeon[y1][x] = 0

    elif dungeon_type == 'maze':
        dungeon = generate_maze(width, height)

    return dungeon

if __name__ == "__main__":
    # Test the dungeon generation
    dungeon = generate_dungeon(50, 50, 'bsp')
    for row in dungeon:
        print(''.join(['#' if cell else '.' for cell in row]))

    print("\nMaze Dungeon:")
    maze_dungeon = generate_dungeon(25, 25, 'maze')
    for row in maze_dungeon:
        print(''.join(['#' if cell else '.' for cell in row]))

import random

class BSPNode:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.left = None
        self.right = None
        self.room = None

def generate_bsp(x, y, width, height, min_room_size):
    node = BSPNode(x, y, width, height)

    if width >= min_room_size * 2 and height >= min_room_size * 2:
        if random.random() < 0.5:
            # Split horizontally
            split = random.randint(y + min_room_size, y + height - min_room_size)
            node.left = generate_bsp(x, y, width, split - y, min_room_size)
            node.right = generate_bsp(x, split, width, y + height - split, min_room_size)
        else:
            # Split vertically
            split = random.randint(x + min_room_size, x + width - min_room_size)
            node.left = generate_bsp(x, y, split - x, height, min_room_size)
            node.right = generate_bsp(split, y, x + width - split, height, min_room_size)
    else:
        node.room = generate_random_room(node.x, node.y, node.width, node.height)

    return node

def generate_random_room(x, y, max_width, max_height):
    min_room_size = 4
    room_width = random.randint(min_room_size, min(max_width, 8))
    room_height = random.randint(min_room_size, min(max_height, 8))
    room_x = x + random.randint(0, max_width - room_width)
    room_y = y + random.randint(0, max_height - room_height)
    return {'x': room_x, 'y': room_y, 'width': room_width, 'height': room_height}

def generate_corridors(node):
    corridors = []
    if node.left and node.right:
        left_room = get_room(node.left)
        right_room = get_room(node.right)
        if left_room and right_room:
            corridors.append(connect_rooms(left_room, right_room))
        corridors.extend(generate_corridors(node.left))
        corridors.extend(generate_corridors(node.right))
    return corridors

def get_room(node):
    if node.room:
        return node.room
    left_room = get_room(node.left) if node.left else None
    right_room = get_room(node.right) if node.right else None
    return left_room or right_room

def connect_rooms(room1, room2):
    x1, y1 = room1['x'] + room1['width'] // 2, room1['y'] + room1['height'] // 2
    x2, y2 = room2['x'] + room2['width'] // 2, room2['y'] + room2['height'] // 2
    if random.random() < 0.5:
        return [
            {'x': x1, 'y': y1, 'x2': x2, 'y2': y1},
            {'x': x2, 'y': y1, 'x2': x2, 'y2': y2}
        ]
    else:
        return [
            {'x': x1, 'y': y1, 'x2': x1, 'y2': y2},
            {'x': x1, 'y': y2, 'x2': x2, 'y2': y2}
        ]

def generate_maze(width, height):
    maze = [[1 for _ in range(width)] for _ in range(height)]  # 1 represents a wall

    def dfs(x, y):
        maze[y][x] = 0  # Mark as visited
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = x + dx * 2, y + dy * 2
            if 0 <= nx < width and 0 <= ny < height and maze[ny][nx] == 1:
                maze[y + dy][x + dx] = 0  # Carve out a passage
                dfs(nx, ny)

    start_x, start_y = random.randint(0, width - 1) // 2 * 2, random.randint(0, height - 1) // 2 * 2
    dfs(start_x, start_y)
    return maze

def generate_dungeon(width, height, dungeon_type='bsp'):
    if dungeon_type == 'bsp':
        root = generate_bsp(0, 0, width, height, 5)
        rooms = []
        corridors = []

        def extract_rooms(node):
            if node.room:
                rooms.append(node.room)
            else:
                if node.left:
                    extract_rooms(node.left)
                if node.right:
                    extract_rooms(node.right)

        extract_rooms(root)
        corridors = generate_corridors(root)

        dungeon = [[1 for _ in range(width)] for _ in range(height)]
        for room in rooms:
            for y in range(room['y'], room['y'] + room['height']):
                for x in range(room['x'], room['x'] + room['width']):
                    dungeon[y][x] = 0

        for corridor in corridors:
            for segment in corridor:
                x1, y1, x2, y2 = segment['x'], segment['y'], segment['x2'], segment['y2']
                if x1 == x2:
                    for y in range(min(y1, y2), max(y1, y2) + 1):
                        dungeon[y][x1] = 0
                else:
                    for x in range(min(x1, x2), max(x1, x2) + 1):
                        dungeon[y1][x] = 0

    elif dungeon_type == 'maze':
        dungeon = generate_maze(width, height)

    return dungeon

def print_dungeon(dungeon):
    for row in dungeon:
        print(''.join(['#' if cell else '.' for cell in row]))

if __name__ == "__main__":
    print("BSP Dungeon:")
    bsp_dungeon = generate_dungeon(50, 50, 'bsp')
    print_dungeon(bsp_dungeon)

    print("\nMaze Dungeon:")
    maze_dungeon = generate_dungeon(25, 25, 'maze')
    print_dungeon(maze_dungeon)
