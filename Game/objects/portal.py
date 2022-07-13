from objects.obstacles import Obstacles

class Portal(Obstacles):
    def __init__(self):
        Obstacles.__init__(self)
        self.x_move = None
        self.y_move = None

    def set_move_coords(self,x,y):
        self.x_move = x
        self.y_move = y
    def get_move_coords(self):
        return self.x_move,self.y_move
