
from GameObjects.Scene.scene import Cave
from GameObjects.Charector.charector import Enemy

cavern = Cave("Cavern")
cavern.set_description("A damp and dirty cave")

dungeon = Cave("Dungeon")
dungeon.set_description("A large cave with a rack")

grotto = Cave("Grotto")
grotto.set_description("A small cave with ancient graffiti")

cavern.link_cave(dungeon, "south")
dungeon.link_cave(cavern, "north")
dungeon.link_cave(grotto, "west")
grotto.link_cave(dungeon, "east")

harry = Enemy("Harry", "A Knight")
harry.set_conversation("Hangry…Hanggrry")
harry.set_weakness("vegemite")

dungeon.set_character(harry)

current_cave = cavern
dead = False

while not dead:
    print("\n")
    current_cave.get_details()
    inhabitant = current_cave.get_character()
    if inhabitant is not None:
        inhabitant.describe()
    command = input("> ")
    if command in ["north", "south", "east", "west"]:
        
        if current_cave.get_details() == "Dungeon":
            print("Cant move")
        else: 
            current_cave = current_cave.move(command)
    elif command == "talk":
        if inhabitant is not None:
            inhabitant.talk()
    elif command == "fight":
        if inhabitant is not None and isinstance(inhabitant, Enemy):
            print("What will you fight with?")
            fight_with = input()
            if inhabitant.fight(fight_with):
                print("Bravo, you won the fight!")
                current_cave.set_character(None)
            else:
                print("You lost the fight.")
                print("That's the end of the game")
                dead = True
        else:
            print("There is no one here to fight with")
    else:
        print("Invalid command")