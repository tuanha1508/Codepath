class Villager:
    VALID_FURNITURE = {
        "acoustic guitar",
        "ironwood kitchenette",
        "rattan armchair",
        "kotatsu",
        "cacao tree",
    }

    def __init__(self, name: str, species: str, personality: str, catchphrase: str, neighbor=None):
        self.name = name
        self.species = species
        self.personality = personality
        self.catchphrase = catchphrase
        self.furniture = []
        self.neighbor = neighbor

    def add_item(self, item_name: str) -> None:
        if item_name in Villager.VALID_FURNITURE:
            self.furniture.append(item_name)


def of_personality_type(townies, personality_type):
    return [
        villager.name
        for villager in townies
        if villager.personality == personality_type
    ]


def message_received(start_villager, target_villager):
    seen = set()
    current = start_villager

    while current is not None:
        if current is target_villager:
            return True
        if current in seen:
            break
        seen.add(current)
        current = current.neighbor

    return False

isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
tom_nook = Villager("Tom Nook", "Raccoon", "Cranky", "yes, yes")
kk_slider = Villager("K.K. Slider", "Dog", "Lazy", "dig it")
isabelle.neighbor = tom_nook
tom_nook.neighbor = kk_slider

print(message_received(isabelle, kk_slider))
print(message_received(kk_slider, isabelle))
