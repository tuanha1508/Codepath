class Villager:
    VALID_FURNITURE = {
        "acoustic guitar",
        "ironwood kitchenette",
        "rattan armchair",
        "kotatsu",
        "cacao tree",
    }

    def __init__(self, name: str, species: str, catchphrase: str):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []

    def add_item(self, item_name: str) -> None:
        if item_name in Villager.VALID_FURNITURE:
            self.furniture.append(item_name)
            
alice = Villager("Alice", "Koala", "guvnor")
print(alice.furniture)

alice.add_item("acoustic guitar")
print(alice.furniture)

alice.add_item("cacao tree")
print(alice.furniture)

alice.add_item("nintendo switch")
print(alice.furniture)

