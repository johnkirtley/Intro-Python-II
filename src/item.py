class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f'{self.name}'

    def on_take(self):
        print(f'You picked up a {self.name}')

    def on_drop(self):
        print(f'You dropped your {self.name}')
