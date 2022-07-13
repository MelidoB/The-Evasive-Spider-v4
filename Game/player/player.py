from functions.movement import Movement
from functions.appearance import Appearance
from functions.coordinates import Coordinates

class Player(Coordinates,Movement,Appearance):
    def __init__(self):
        #Things that can be change by others

        #coordinates
        Coordinates.__init__(self)

        #velocity
        Movement.__init__(self)

        #image
        Appearance.__init__(self)

        #power currently use by player
        self.power = None
        self.color = []


    def set_power(self,power):
        self.power = power
    def set_color(self,color):
        self.color.append(color)