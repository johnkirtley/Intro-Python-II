from room import Room
from player import Player
from item import Item

# Declare all the rooms
# available_rooms arranged n, s, e, w

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", ['foyer', None, None, None], [
                         Item('torch', 'you can now see in the dark')]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", ['overlook', 'outside', 'narrow', None], [Item('matches', 'allows you to light torch')]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [None, 'foyer', None, None], [Item('map', 'helps you find treasure room')]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", ['treasure', None, None, 'foyer']),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [None, 'narrow', None, None], [Item('treasure chest', 'you have found the treasure!')])
}

# Sets player name and initial room location

player_name = input('What is your name? ')
player1 = Player(player_name, room['outside'])

# Stores inputted direction in variable


def inputParser():

    direction = input(
        '\nWhere would you like to go next? (n for North, e for East, s for South, w for West, or q to Quit)')

    return direction


while True:

    print(f"\n{player1.name}'s current location is {player1.current_room.name}")

    print(f"{player1.current_room.description}\n")

    print(f'Items you currently have: ')
    player1.print_current_items()

    # Allows you to drop item in current room
    if len(player1.current_items) > 0:

        drop_item_action = input(
            'Would you like to drop an item in this room? (drop [item_name] or n for No) ').split()

        if drop_item_action[0].lower() == 'drop':
            for i in player1.current_items:
                if i.name == drop_item_action[1]:
                    player1.remove_item(i)
                    print(
                        f'{player1.name} dropped {i.name} in {player1.current_room.name}')
                    player1.current_room.add_item(i)

    # Allows you to pickup item in current room
    if len(player1.current_room.items) > 0:
        print('\nItems in this room:')
        player1.current_room.print_items()

        get_item = input(
            'Would you like to select an item? (get [item_name]) or n for No ').split()

        if get_item[0].lower() == 'get':

            for i in player1.current_room.items:
                if i.name == get_item[1]:
                    player1.add_item(i)
                    print(f'Added {i.name} to inventory')
                    player1.current_room.remove_item(i)

                if i.name == 'treasure chest':
                    print('You found the treasure!!!')
                    break

    else:
        print('\nNo items in this room')

    # Prompts for direction input after item selection/drops
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
            print('\n*****Cannot proceed in that direction. Try again.*****')
