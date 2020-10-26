from room import Room
from player import Player
from world import World

import random
from ast import literal_eval


class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)


# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# * World generation code. Do not modify this!
# * An incomplete list of directions. Your task is to fill this with valid traversal directions.
# * Test code. Run the tests by typing `python3 adv.py` in your terminal.
# * REPL code. You can uncomment this and run `python3 adv.py` to walk around the map.
# traversal_path = ['n', 'n']
traversal_path = []

# <--------------------------------------------------------------------------------------------->

reverse = False
stack = Stack()
visited_rooms_in_game = set()
explored = {}
for i in range(len(room_graph)):
    explored[i] = {'n': '?', 's': '?', 'w': '?', 'e': '?'}


def go_back(direction):
    if direction == 'n':
        return 's'
    if direction == 's':
        return 'n'
    if direction == 'e':
        return 'w'
    if direction == 'w':
        return 'e'


print('Starting Room ID: ', player.current_room.id)
print('Starting Entry: ', explored)

visited_rooms_in_game.add(player.current_room.id)

while len(visited_rooms_in_game) < len(room_graph):

    # get current room ID
    start = player.current_room.id
    reverse = False

    # fill in '?' directions with available movements.
    beginning = player.current_room.get_exits()

    for direction in explored[start]:
        if direction not in beginning:
            explored[start][direction] = None

    # perform check on unexplored rooms
    explored_rooms = 0
    for direction in explored[start]:
        if explored[start][direction] != '?':
            explored_rooms += 1
        # else if room is unexplored
        elif not None:
            move = direction
    # if all surrounding rooms are explored
    if explored_rooms == 4:
        reverse = True

    # if reverse = True
    if reverse is True:
        last_move = stack.pop()
        move = go_back(last_move)
        # add movement to traversal_path
        traversal_path.append(move)
        player.travel(move)

    # If not moving in reverse
    else:
        # add next move to stack
        stack.push(move)
        # add next move to traversal_path
        traversal_path.append(move)
        player.travel(move)
        # fill in explored list with visited rooms
        room_2 = player.current_room.id
        explored[start][move] = room_2
        get_reverse = go_back(move)
        explored[room_2][get_reverse] = start

        # add to visited_rooms_in_game
        visited_rooms_in_game.add(room_2)

print('Ending Entry: ', explored)
print('Visited Rooms: ', len(visited_rooms_in_game))
print('Map Length: ', len(room_graph))
print('Ending Room ID: ', player.current_room.id)

# <--------------------------------------------------------------------------------------------->

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
