# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, room, name, inventory=[]):
        self.room = room
        self.name = name
        self.inventory = inventory

    def check_inventory(self):
        print(f"{self.inventory}")

    def add_item(self, item):
        self.inventory.append(item)
        print(f"You've added {item} to your inventory")

    def remove_item(self, item):

        if len(self.inventory) == 0 or item is None:
            print("You have no items in your inventory")

        else:
            self.inventory.remove(item)
            print(f"You have removed {item} from your inventory")





