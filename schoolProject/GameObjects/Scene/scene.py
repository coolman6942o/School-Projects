
class Cave:
    def __init__(self, cave_name):
        self.name = cave_name
        self.description = None
        self.linked_caves = {}
        self.character = None

    def set_description(self, cave_description):
        self.description = cave_description

    def get_description(self):
        return self.description

    def describe(self):
        print(self.description)

    def link_cave(self, cave_to_link, direction):
        self.linked_caves[direction] = cave_to_link

    def get_details(self):
        print(self.name)
        print(self.description)
        for direction in self.linked_caves:
            cave = self.linked_caves[direction]
            print(f"The {cave.name} is {direction}")

    def move(self, direction):
        if direction in self.linked_caves:
            return self.linked_caves[direction]
        else:
            print("You can't go that way")
            return self

    def set_character(self, character):
        self.character = character

    def get_character(self):
        return self.character