from room import Room
from player import Player

# Declare all the rooms
# available_rooms arranged n, s, e, w

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", ['foyer', None, None, None]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", ['overlook', 'outside', 'narrow', None]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [None, 'foyer', None, None]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", ['treasure', None, None, 'foyer']),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [None, 'narrow', None, None])
}

# Sets player name and initial room location

player_name = input('What is your name? ')
player1 = Player(player_name, room['outside'])

# Stores inputted direction in variable


def inputParser():

    direction = input(
        'Where would you like to go next? (n for North, e for East, s for South, w for West, or q to Quit)')

    return direction


while True:

    print(f"{player1.name}'s current location is {player1.current_room.name}")

    print(f"{player1.current_room.description}")

    direction = inputParser()

    if direction == 'q':
        break

    # if a valid direction is given
    # change current_room to new room if there is a valid room to move too

    if direction in ['n', 's', 'e', 'w']:
        room_index = player1.move(direction)
        if player1.current_room.available_rooms[room_index] != None:
            player1.current_room = room[player1.current_room.available_rooms[room_index]]
        else:
            print('*****Cannot proceed in that direction. Try again.*****')
