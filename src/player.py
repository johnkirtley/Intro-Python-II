class Player:
    def __init__(self, name, current_room, current_items=[]):
        self.name = name
        self.current_room = current_room
        self.current_items = current_items

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

    def add_item(self, item):
        return self.current_items.append(item)

    def remove_item(self, item):
        return self.current_items.remove(item)

    def print_current_items(self):
        if len(self.current_items) > 0:
            for i in self.current_items:
                print(i)
        else:
            print('Inventory Empty')
