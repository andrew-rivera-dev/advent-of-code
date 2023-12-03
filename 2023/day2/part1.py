import fileinput

game_config = {
    'red': 12,
    'green': 13,
    'blue': 14
}

class Game:
    def __init__(self, id=None, reveals=[]):
        self.id = id
        self.reveals = reveals

class Reveal:
    def __init__(self, cube_sets=[]):
        self.cube_sets = cube_sets

class CubeSet:
    def __init__(self, quantity=0, color=None):
        self.quantity = quantity
        self.color = color

def get_game_id(game_id_long):
    return int(game_id_long.split(' ')[1])

def parse_reveals(reveals):
    reveal_objs = []
    parse_reveals = reveals.split(';')
    for reveal in parse_reveals:
        parse_cube_sets = reveal.split(',')
        cube_sets = []
        for cube_set in parse_cube_sets:
            _, quantity, color = cube_set.split(' ')
            cube_sets.append(CubeSet(int(quantity), color.strip()))
        reveal_objs.append(Reveal(cube_sets))

    return reveal_objs

def is_game_possible(game):
    for reveal in game.reveals:
        for cube_set in reveal.cube_sets:
            if cube_set.quantity > game_config[cube_set.color]:
                return False
    return True

games = []

for line in fileinput.input(files ='2023/day2/input.txt'):
    game_id_long, reveals = line.split(':')
    games.append(Game(get_game_id(game_id_long), parse_reveals(reveals)))
    
possible_game_ids = []

for game in games:
    if is_game_possible(game):
        possible_game_ids.append(game.id)

print(sum(possible_game_ids))

