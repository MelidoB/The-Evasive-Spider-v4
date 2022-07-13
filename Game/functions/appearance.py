import pygame

class Appearance:
    def __init__(self):
        # image # img related to movement
        self.img = None
        self.visible = True

    def set_img(self,img):
        self.img = pygame.image.load(f'images/{img}')