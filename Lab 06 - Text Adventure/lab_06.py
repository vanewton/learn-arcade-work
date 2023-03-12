
class Room:
    """The room that we are starting in."""

    def __init__(self, description, north, south, east, west):
        self.description: str = ""
        self.north: str = north
        self.south: str = south
        self.east: str = east
        self.west: str = west



def main():
    room = Room ("A quaint room lit with a single torch. Tucked in a corner is a small bed adjacent to a wooden bookshelf.",
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