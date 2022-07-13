from functions.movement import Movement
from functions.appearance import Appearance
from functions.coordinates import Coordinates

class Obstacles(Coordinates,Appearance):
    def __init__(self):
        self.block_movement = False
        # coordinates
        Coordinates.__init__(self)
        #image
        Appearance.__init__(self)

        self.color = "No-Color"

    def set_block_movement(self):
        self.block_movement = True

    def set_color(self,color):
        self.color = color

