# Charlie DeGennaro
import pygame as pg
import random as r
import math

pg.init()
window_size = (25, 15)
tile_size = 50
tile_scale = 1
screen_size = (int(window_size[0]*tile_size*tile_scale),
               int(window_size[1]*tile_size*tile_scale))
window = pg.display.set_mode(screen_size)
pg.display.set_caption("Wave Function Collapse")

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

tiles = []


class Tile:
    def __init__(self, image, edges, size=50, scale=1):
        self.size_constant = int(size*scale)
        self.image = pg.transform.scale(
            image, (self.size_constant, self.size_constant))
        self.edges = edges
        self.collapsed = False
        self.size = size
        self.scale = scale

    def rotate(self, num):
        new_image = pg.transform.rotate(self.image, -90*num)
        new_edges = self.edges.copy()
        for i in range(len(self.edges)):
            new_edges[i] = self.edges[(
                i - num + len(self.edges)) % len(self.edges)]
        return Tile(new_image, new_edges, self.size, self.scale)


def load_demo_set_full():
    global tiles
    tiles.append(Tile(pg.image.load('images/demo_tiles/blank.png'),
                 [0, 0, 0, 0], tile_size, tile_scale))
    tiles.append(Tile(pg.image.load('images/demo_tiles/up.png'),
                 [1, 1, 0, 1], tile_size, tile_scale))
    tiles.append(tiles[1].rotate(1))
    tiles.append(tiles[1].rotate(2))
    tiles.append(tiles[1].rotate(3))
    tiles.append(Tile(pg.image.load('images/demo_tiles/corner.png'),
                 [1, 1, 0, 0], tile_size, tile_scale))
    tiles.append(tiles[5].rotate(1))
    tiles.append(tiles[5].rotate(2))
    tiles.append(tiles[5].rotate(3))
    tiles.append(Tile(pg.image.load('images/demo_tiles/cross.png'),
                 [1, 1, 1, 1], tile_size, tile_scale))
    tiles.append(Tile(pg.image.load('images/demo_tiles/line.png'),
                 [0, 1, 0, 1], tile_size, tile_scale))
    tiles.append(tiles[10].rotate(1))


def load_demo_set_corners():
    global tiles
    tiles.append(Tile(pg.image.load('images/demo_tiles/blank.png'),
                 [0, 0, 0, 0], tile_size, tile_scale))
    tiles.append(Tile(pg.image.load('images/demo_tiles/corner.png'),
                 [1, 1, 0, 0], tile_size, tile_scale))
    tiles.append(tiles[1].rotate(1))
    tiles.append(tiles[1].rotate(2))
    tiles.append(tiles[1].rotate(3))


def load_demo_set_t():
    global tiles
    tiles.append(Tile(pg.image.load('images/demo_tiles/blank.png'),
                 [0, 0, 0, 0], tile_size, tile_scale))
    tiles.append(Tile(pg.image.load('images/demo_tiles/up.png'),
                 [1, 1, 0, 1], tile_size, tile_scale))
    tiles.append(tiles[1].rotate(1))
    tiles.append(tiles[1].rotate(2))
    tiles.append(tiles[1].rotate(3))


def load_demo_set_t_line():
    global tiles
    load_demo_set_t()
    tiles.append(Tile(pg.image.load('images/demo_tiles/line.png'),
                 [0, 1, 0, 1], tile_size, tile_scale))
    tiles.append(tiles[5].rotate(1))


def load_demo_set_cross():
    global tiles
    tiles.append(Tile(pg.image.load('images/demo_tiles/blank.png'),
                 [0, 0, 0, 0], tile_size, tile_scale))
    tiles.append(Tile(pg.image.load('images/demo_tiles/up.png'),
                 [1, 1, 0, 1], tile_size, tile_scale))
    tiles.append(tiles[1].rotate(1))
    tiles.append(tiles[1].rotate(2))
    tiles.append(tiles[1].rotate(3))
    tiles.append(Tile(pg.image.load('images/demo_tiles/cross.png'),
                 [1, 1, 1, 1], tile_size, tile_scale))


# tiles.append(Tile(pg.image.load('images/demo_tiles/cross.png'), [2, 2, 2, 2], tile_size, tile_scale))
# tiles.append(Tile(pg.image.load('images/demo_tiles/line.png'), [0, 1, 0, 2], tile_size, tile_scale))
# tiles.append(tiles[10].rotate(1))
# tiles.append(tiles[10].rotate(2))
# tiles.append(tiles[10].rotate(3))
# tiles.append(Tile(pg.image.load('images/demo_tiles/line.png'), [0, 1, 0, 1], tile_size, tile_scale))
# tiles.append(tiles[14].rotate(1))
# tiles.append(Tile(pg.image.load('images/demo_tiles/line.png'), [0, 2, 0, 2], tile_size, tile_scale))
# tiles.append(tiles[16].rotate(1))


def reset_grid():
    global grid
    window.fill(windowColor)
    for i in range(len(grid)):
        grid[i] = {
            'grid_pos': (int(i % window_size[0]), int(i/window_size[0])),
            'collapsed': False,
            'options': list(range(len(tiles))),
            'index': None
        }


def return_min_entropy_list():
    min_entropy = 9999999

    for tile in grid:
        if not tile['collapsed']:
            min_entropy = min(len(tile['options']), min_entropy)

    return_list = []

    for i in range(len(grid)):
        if min_entropy == len(grid[i]['options']) and not grid[i]['collapsed']:
            return_list.append(i)
        # else:
            # print('TTT',tile)

    return return_list


def collapse():
    global grid
    min_entropy_list = return_min_entropy_list()
    # print(min_entropy_list)
    gridtile_to_collapse = grid[r.choice(return_min_entropy_list())]
    # gridtile_to_collapse = grid[min_entropy_list[6]]
    if len(min_entropy_list) == 0 or len(gridtile_to_collapse['options']) == 0:
        reset_grid()
        return
    rand_tile = r.choice(gridtile_to_collapse['options'])
    gridtile_to_collapse['index'] = rand_tile
    # print(gridtile_to_collapse)
    gridtile_to_collapse['options'] = [gridtile_to_collapse['index']]
    gridtile_to_collapse['collapsed'] = True
    update_entropy(gridtile_to_collapse)
    blit(gridtile_to_collapse)


def collapsed_count():
    count = 0
    for tile in grid:
        if tile['collapsed']:
            count += 1
    return count


def update_entropy(tile):
    global grid
    grid_index = tile['grid_pos'][0] + tile['grid_pos'][1]*window_size[0]
    up_index = max(grid_index - window_size[0], -1)
    right_index = grid_index + 1
    down_index = grid_index + window_size[0]
    left_index = max(grid_index - 1, -1)

    if down_index >= window_size[0]*window_size[1]:
        down_index = -1
    if right_index >= window_size[0]*window_size[1]:
        right_index = -1

    if right_index % window_size[0] == 0:
        right_index = -1
    if (left_index+1) % window_size[0] == 0:
        left_index = -1

    # print(grid[up_index]['options'])

    if up_index != -1:
        up_options = grid[up_index]['options'].copy()
        for i in range(len(up_options)):
            option = up_options[i]
            # print(tile['index'], up_options[option])
            if tiles[option].edges[DOWN] != tiles[tile['index']].edges[UP]:
                grid[up_index]['options'].remove(option)

    if right_index != -1:
        right_options = grid[right_index]['options'].copy()
        for i in range(len(right_options)):
            option = right_options[i]
            # print(tile['index'], up_options[option])
            if tiles[option].edges[LEFT] != tiles[tile['index']].edges[RIGHT]:
                grid[right_index]['options'].remove(option)

    if down_index != -1:
        down_options = grid[down_index]['options'].copy()
        for i in range(len(down_options)):
            option = down_options[i]
            # print(tile['index'], up_options[option])
            if tiles[option].edges[UP] != tiles[tile['index']].edges[DOWN]:
                grid[down_index]['options'].remove(option)

    if left_index != -1:
        left_options = grid[left_index]['options'].copy()
        for i in range(len(left_options)):
            option = left_options[i]
            # print(tile['index'], up_options[option])
            if tiles[option].edges[RIGHT] != tiles[tile['index']].edges[LEFT]:
                grid[left_index]['options'].remove(option)

    # print(grid[up_index]['options'])


def blit(tile):
    tile_index = tile['index']
    image_size = tiles[tile_index].size_constant
    window.blit(tiles[tile['index']].image, (image_size *
                tile['grid_pos'][0], image_size*tile['grid_pos'][1]))


load_demo_set_full()
grid = [None]*window_size[0]*window_size[1]
run = True
windowColor = [200, 0, 0]
i = 0
j = 0
reset_grid()
while(run):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                collapse()
            if event.key == pg.K_r:
                reset_grid()

    if collapsed_count() < len(grid):
        collapse()

    pg.display.update()

    # pg.time.delay(10)
