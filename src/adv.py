from room import Room
from player import Player
from item import Item

# Declare all the rooms


# set items

item_1 = Item('Axe', 'A majestic axe crafted by the Daedra')
item_2 = Item('Compass', 'Use this item for guidance')
item_3 = Item('Sword', 'Use this sword to defeat the evil boss')
item_4 = Item('Key', 'This is the boss Key, which opens the door to battle the boss')


room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [item_1, item_2]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [item_4]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [item_3]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


#
# Main
#

# Make a new player object that is currently in the 'outside' room.


# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
for item in room['foyer'].items:
    print(item.name)


def play_game():
    current_room = room['outside']
    player_name = input('Enter your name to play:')
    player = Player(current_room, player_name)
    command = ""

    while command != 'q':

        command = input(f"{player.name}!! Your current location is {current_room.name}."
                        f" {current_room.description}.To navigate, insert the commands: n,e,s,w. To quit: insert q.")
        if command == 'n':
            if current_room.n_to is None:
                print("you cant go there")

            else:
                current_room = current_room.n_to
                # print(f"Your are in {current_room.name}, {current_room.description}")

        if command == 'w':
            if current_room.w_to is None:
                print("You cant go there")
            else:
                current_room = current_room.w_to

        if command == 's':
            if current_room.s_to is None:
                print("you can't go there")
            else:
                current_room = current_room.s_to
        if command == 'e':
            if current_room.e_to is None:
                print("You cant go there")
            else:
                current_room = current_room.e_to

        if command == 'i':
            player.check_inventory()

    if command == 'q':
        print('Thank you for playing!! :D')


play_game()
