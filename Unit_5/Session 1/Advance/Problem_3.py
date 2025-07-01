class Villager:
    VALID_FURNITURE = {
        "acoustic guitar",
        "ironwood kitchenette",
        "rattan armchair",
        "kotatsu",
        "cacao tree",
    }

    def __init__(self, name: str, species: str, personality: str, catchphrase: str):
        self.name = name
        self.species = species
        self.personality = personality  
        self.catchphrase = catchphrase
        self.furniture = []

    def add_item(self, item_name: str) -> None:
        if item_name in Villager.VALID_FURNITURE:
            self.furniture.append(item_name)


def of_personality_type(townies, personality_type):
    return [
        villager.name
        for villager in townies
        if villager.personality == personality_type
    ]


isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
bob      = Villager("Bob",      "Cat",  "Lazy",   "pthhhpth")
stitches = Villager("Stitches", "Cub",  "Lazy",   "stuffin'")

print(of_personality_type([isabelle, bob, stitches], "Lazy")) 
print(of_personality_type([isabelle, bob, stitches], "Cranky")) 
