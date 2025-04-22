from TVPoke.BaseClasses.PokeTypes import Water
from TVPoke.BaseClasses.Move import Move

class Gyarados(Water):
    def __init__(self):
        moves = [
            Move("Dragon Dance", "DRAGON", 0),
            Move("Hydro pump", "WATER", 120),
            Move("Waterfall", "WATER", 80),
            Move("Crunch", "DARK", 80)
        ]
        super().__init__("Gyarados", 95, moves, "./TVPoke/Pokemon/imgs/Gyarados.png")
