class Villager:
    def __init__(self, name: str, species: str, catchphrase: str):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []
        
apollo = Villager("Apollo", "Eagle", "pah")
print(apollo.name)
print(apollo.species) 
print(apollo.catchphrase)
print(apollo.furniture)