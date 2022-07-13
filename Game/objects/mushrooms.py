from objects.obstacles import Obstacles

class Mushrooms(Obstacles):
    def __init__(self):
        Obstacles.__init__(self)
        self.transformation_images = None
        self.music = None

    def set_transformation_images(self):
        self.transformation_images = {
            'down': [f'mushrooms/{self.color}/player/down/1.png', f'mushrooms/{self.color}/player/down/2.png',
                     f'mushrooms/{self.color}/player/down/3.png'],
            'left': [f'mushrooms/{self.color}/player/left/1.png', f'mushrooms/{self.color}/player/left/2.png',
                     f'mushrooms/{self.color}/player/left/3.png'],
            'right': [f'mushrooms/{self.color}/player/right/1.png', f'mushrooms/{self.color}/player/right/2.png',
                      f'mushrooms/{self.color}/player/right/3.png'],
            'top': [f'mushrooms/{self.color}/player/top/1.png', f'mushrooms/{self.color}/player/top/2.png',
                    f'mushrooms/{self.color}/player/top/3.png'],
        }
