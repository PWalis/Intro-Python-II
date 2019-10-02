from room import Room
import player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

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


player_1 = player.Player('outside')

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


on = 1
print('ENTER "q" TO QUIT')
while on == 1:
    paths = room[player_1.location].available_path()
    
    print('Current location: ', player_1.location)
    print(f'Possible directions: {paths} \n')
    k = input('Press key: ')

    if k == 'q':
        break
    if k in paths:
        if k == 'n':
            newloc = room[player_1.location].n_to.room.split(' ',1)[0].lower()
            player_1.update_location(newloc)

        elif k == 'e':
            newloc = room[player_1.location].e_to.room.split(' ',1)[0].lower()
            player_1.update_location(newloc)

        elif k == 's':
            newloc = room[player_1.location].s_to.room.split(' ',1)[0].lower()
            player_1.update_location(newloc)
            
        elif k == 'w':
            newloc = room[player_1.location].w_to.room.split(' ',1)[0].lower()
            player_1.update_location(newloc)
    else:
        print('\n###You can not go that way###\n')
        