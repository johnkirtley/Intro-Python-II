class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

# takes a specified direction and returns an index position
# this index position is used for the available_rooms attr on the Room class

    def move(self, move):
        if move == 'n':
            return 0
        elif move == 's':
            return 1
        elif move == 'e':
            return 2
        elif move == 'w':
            return 3
