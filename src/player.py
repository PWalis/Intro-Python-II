# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, location):
        self.location = location
        self.items = []
    
    def update_location(self, newloc):
        self.location = newloc
    
    def add_item(self, item):
        self.items.append(item)

    def drop_item(self, item):
        self.items.remove(item)
    
    def show_inventory(self):
        print(self.items)