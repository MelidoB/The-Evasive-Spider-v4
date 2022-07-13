from player.player import Player
from objects.obstacles import Obstacles
from functions.close_application import close_game_function
from functions.key_press import key_pressed
from functions.object_facilitator import object_facilitator
from functions.display_objects import display_objects
from functions.object_takes_object import object_takes_object
import pygame

def world_1():
    player = Player()

    default_player_images = {
        'down': ['player_default/down/1.png', 'player_default/down/2.png', 'player_default/down/3.png'],
        'left': ['player_default/left/1.png', 'player_default/left/2.png', 'player_default/left/3.png'],
        'right': ['player_default/right/1.png', 'player_default/right/2.png', 'player_default/right/3.png'],
        'top': ['player_default/top/1.png', 'player_default/top/2.png', 'player_default/top/3.png'],

    }
    default_player_images_counters = {'down': 0, 'left': 0, 'right': 0, 'top': 0}
    default_player_images_timer = {'down': 11, 'left': 11, 'right': 11, 'top': 11}

    player.set_img(default_player_images['right'][0])
    player.set_coordinates(150, 150)
    player.set_velocity(5)



    walls = []

    # need the function to create walls with coordinates (A to B)
    img = 'obstacles/wall.png'
    object_facilitator(len(walls), walls, Obstacles, img, 1, 0, 0)  # start

    object_facilitator(len(walls), walls, Obstacles, img, 5, 0, 0, right=True)
    object_facilitator(len(walls), walls, Obstacles, img, 5, 0, 400, right=True)
    object_facilitator(len(walls), walls, Obstacles, img, 3, 400, 100, right=True)
    object_facilitator(len(walls), walls, Obstacles, img, 3, 400, 300, right=True)
    object_facilitator(len(walls), walls, Obstacles, img, 4, 0, 0, down=True)
    object_facilitator(len(walls), walls, Obstacles, img, 1, 600, 200)

    object_facilitator(len(walls), walls, Obstacles, img, 1, 600, 400)  # end

    victory_flags = []
    img = 'victory/flag.png'
    object_facilitator(len(victory_flags), victory_flags, Obstacles, img, 1, 500, 150, block_movement=False)  # end

    pygame.init()
    DISPLAY_WIDTH, DISPLAY_HEIGHT = 700, 700
    gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
    clock = pygame.time.Clock()

    while True:
        close_game_function()

        gameDisplay.fill((0, 0, 0))
        gameDisplay.blit(player.img, (player.x, player.y))
        # displaying walls, flags
        display_objects(gameDisplay, walls)
        display_objects(gameDisplay, victory_flags)

        key_pressed(pygame, player, walls + victory_flags,walls[0],walls[-1], DISPLAY_WIDTH, DISPLAY_HEIGHT, default_player_images,
                    default_player_images_counters, default_player_images_timer)

        # player gets flag
        player_obtain_flag_or_flags = object_takes_object(player, victory_flags)
        if player_obtain_flag_or_flags != None:
            break

        clock.tick(60)
        pygame.display.update()