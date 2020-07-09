class Room:
    def __init__(self, name, description, available_rooms):
        self.name = name
        self.description = description

        # array of rooms available to current_room

        self.available_rooms = available_rooms
