# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, room, description):
        self.room = room
        self.desc = description
        self.n_to = None
        self.w_to = None
        self.e_to = None
        self.s_to = None
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def take_item(self, item):
        self.items.remove(item)

    def available_path(self):
        path_list = []
        if self.n_to != None:
            path_list.append('n')
        if self.w_to != None:
            path_list.append('w')
        if self.e_to != None:
            path_list.append('e')
        if self.s_to != None:
            path_list.append('s')
        return path_list