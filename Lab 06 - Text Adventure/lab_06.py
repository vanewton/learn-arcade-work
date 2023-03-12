
class Room:
    """The room that we are starting in."""
    def __init__(self, description, north, south, east, west):
        self.description: str = ""
        self.north: str = north
        self.south: str = south
        self.east: str = east
        self.west: str = west



def main():
    my_room = Room ("description",
                    "north",
                    "south",
                    "east",
                    "west")
    print(my_room.description)
    print(my_room.north)
    print(my_room.south)
    print(my_room.east)
    print(my_room.west)

    main()
        room_list = {}
    print(room_list)