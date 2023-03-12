
class Room:
    """The room that we are starting in."""

    def __init__(self, description, north, south, east, west):
        self.description: str = ""
        self.north: str = north
        self.south: str = south
        self.east: str = east
        self.west: str = west



def main():
    room = Room ("description",
                    "north",
                    "south",
                    "east",
                    "west")
    print(room.description)
    print(room.north)
    print(room.south)
    print(room.east)
    print(room.west)

main()
    room_list = []
    print(room_list)