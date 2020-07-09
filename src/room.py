class Room:
    def __init__(self, name, description, available_rooms, items=[]):
        self.name = name
        self.description = description
        self.items = items

        # array of rooms available to current_room

        self.available_rooms = available_rooms

    def print_items(self):
        for i in self.items:
            print(i)
