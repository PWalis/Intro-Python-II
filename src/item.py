# Create an item class with name and discription attributes 
class Item:
    def __init__(self, name='', description=''):
        self.name = name
        self.description = description 
    
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.name
    
    def on_take(self):
        print(f'You have picked up {self.name}')
    
    def on_drop(self):
        print(f'You have dropped {self.name}')

class Item_special(Item):
    def __init__(self, name='', description='', special_property=''):
        super().__init__(name=name, description=description)
        self.sp = special_property

item_list = [Item('Love', 'its love yo')]
for i in item_list:
    if i.name == 'Love':
        print(i)
