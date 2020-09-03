# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = items

    def remove_item_from_room(self, item):
        for i in self.items:

            if item == i.name:
                self.items.remove(i)


    def reveal_items(self):
        string = "This room has the item(s):"
        for i in self.items:
            # print(i['name'])
            string += '\n' + i.name

        return print(string)





# room_5 = Room('room', 'a room', [{'name': 'Axe'},{'name': 'Compass'}, {'name': 'Key'}])
#
# room_5.remove_item_from_room('Axe')
# room_5.reveal_items()
