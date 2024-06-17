
from GameObjects.Scene.scene import Cave
from GameObjects.Charector.charector import Enemy
from GameObjects.Item.item import Item

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

vegemite = Item("vegemite")
vegemite.set_description("A Monster's worst nightmare")
grotto.set_item(vegemite)

torch = Item("torch")
torch.set_description("A light for the end of the tunnel")
dungeon.set_item(torch)

bag = []
current_cave = cavern
dead = False
while not dead:
    print("\n")
    current_cave.get_details()
    inhabitant = current_cave.get_character()
    if inhabitant is not None:
        inhabitant.describe()
    item = current_cave.get_item()
    if item is not None:
        item.describe()
    command = input(">")
    if command in ["north", "south", "east", "west"]:
        current_cave = current_cave.move(command)
    elif command == "talk":
        if inhabitant is not None:
            inhabitant.talk()
    elif command == "fight":
        if inhabitant is not None and isinstance(inhabitant, Enemy):
            print("What will you fight with?")
            fight_with = input()
            if fight_with in bag:
                if inhabitant.fight(fight_with):
                    print("Bravo, hero you won the fight!")
                    current_cave.set_character(None)
                    if Enemy.enemies_to_defeat == 0:
                        print("Congratulations, you have survived another adventure!")
                        dead = True
                else:
                    print("Scurry home, you lost the fight.")
                    print("That's the end of the game")
                    dead = True
            else:
                print("You don't have a " + fight_with)
        else:
            print("There is no one here to fight with")
    elif command == "pat":
        if inhabitant is not None:
            if isinstance(inhabitant, Enemy):
                print("I wouldn't do that if I were you...")
            else:
                inhabitant.pat()
        else:
            print("There is no one here to pat :(")
    elif command == "take":
        if item is not None:
            print("You put the " + item.get_name() + " in your bag")
            bag.append(item.get_name())
            current_cave.set_item(None)