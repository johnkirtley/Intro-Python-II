class Room:
    def __init__(self, name, description, available_rooms, items=[]):
        self.name = name
        self.description = description
        self.items = items

        # array of rooms available to current_room

        self.available_rooms = available_rooms

    def print_items(self):
        for i in self.items:
            item_index = self.items.index(i) + 1
            print(f'{item_index}: {i}')

    def remove_item(self, item):
        return self.items.remove(item)

    def add_item(self, item):
        return self.items.append(item)
