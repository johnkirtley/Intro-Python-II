# Implement a class to hold room information. This should have name and
# description attributes.

# Rooms to include are Outside, Foyer, Overlook, Narrow, Treasure


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def outside(self, n_to='foyer'):
        self.n_to = n_to

    def foyer(self, n_to='overlook', s_to='outside', e_to='narrow'):
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to

    def overlook(self, s_to='foyer'):
        self.s_to = s_to

    def narrow(self, n_to='treasure', w_to='foyer'):
        self.n_to = n_to
        self.w_to = w_to

    def treasure(self, s_to='narrow'):
        self.s_to = s_to
