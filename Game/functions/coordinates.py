class Coordinates:
    def __init__(self):
        # coordinates #movement
        self.x, self.y = None, None

    def set_coordinates(self, x, y):
        '''Modifies x,y coordinates without restrictions'''
        self.x, self.y = x, y

    def get_coordinates(self):
        return self.x, self.y