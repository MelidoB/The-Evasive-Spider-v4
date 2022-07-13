from player.player import Player
from objects.obstacles import Obstacles
from functions.close_application import close_game_function
from functions.key_press import key_pressed
from functions.object_facilitator import object_facilitator
from functions.display_objects import display_objects
from functions.object_takes_object import object_takes_object
from objects.mushrooms import Mushrooms
import pygame
from pygame import mixer
import time

def world_2():
    player = Player()

    default_player_images = {
        'down': ['player_default/down/1.png', 'player_default/down/2.png', 'player_default/down/3.png'],
        'left': ['player_default/left/1.png', 'player_default/left/2.png', 'player_default/left/3.png'],
        'right': ['player_default/right/1.png', 'player_default/right/2.png', 'player_default/right/3.png'],
        'top': ['player_default/top/1.png', 'player_default/top/2.png', 'player_default/top/3.png'],
    }
    default_player_images_copy = default_player_images.copy()

    default_player_images_counters = {'down': 0, 'left': 0, 'right': 0, 'top': 0}
    default_player_images_timer = {'down': 11, 'left': 11, 'right': 11, 'top': 11}

    player.set_img(default_player_images['right'][0])
    player.set_coordinates(150, 300)
    player.set_velocity(5)

    ######################################################
    walls = []

    # need the function to create walls with coordinates (A to B)
    img = 'obstacles/wall.png'
    object_facilitator(len(walls), walls, Obstacles, img, 1, 0, 0,color="yellow")  # start

    object_facilitator(len(walls), walls, Obstacles, img, 5, 0, 0, right=True,color="yellow")
    object_facilitator(len(walls), walls, Obstacles, img, 5, 0, 400, right=True,color="yellow")
    object_facilitator(len(walls), walls, Obstacles, img, 3, 400, 100, right=True,color="yellow")
    object_facilitator(len(walls), walls, Obstacles, img, 3, 400, 300, right=True,color="yellow")
    object_facilitator(len(walls), walls, Obstacles, img, 4, 0, 0, down=True,color="yellow")
    object_facilitator(len(walls), walls, Obstacles, img, 1, 600, 200,color="yellow")

    object_facilitator(len(walls), walls, Obstacles, img, 1, 600, 400,color="yellow")  # end

    #######################################################################
    red_mushrooms = []

    ###red
    img = 'mushrooms/red/1.png'
    object_facilitator(len(red_mushrooms), red_mushrooms, Mushrooms, img, 1, 100, 150, right=True,block_movement=False)
    for mushroom in red_mushrooms:
        mushroom.color = 'red'
        mushroom.set_transformation_images()
    yellow_mushrooms = []
    ###yellow
    img = 'mushrooms/yellow/1.png'
    object_facilitator(len(yellow_mushrooms), yellow_mushrooms, Mushrooms, img, 1, 300, 150, right=True, block_movement=False)
    for mushroom in yellow_mushrooms:
        mushroom.color = 'yellow'
        mushroom.set_transformation_images()

    ###red+yellow
    transformation_images_combined = {
        'down': ['mushrooms/red_yellow/player/down/1.png', 'mushrooms/red_yellow/player/down/2.png',
                 'mushrooms/red_yellow/player/down/3.png'],
        'left': ['mushrooms/red_yellow/player/left/1.png', 'mushrooms/red_yellow/player/left/2.png',
                 'mushrooms/red_yellow/player/left/3.png'],
        'right': ['mushrooms/red_yellow/player/right/1.png', 'mushrooms/red_yellow/player/right/2.png',
                  'mushrooms/red_yellow/player/right/3.png'],
        'top': ['mushrooms/red_yellow/player/top/1.png', 'mushrooms/red_yellow/player/top/2.png',
                'mushrooms/red_yellow/player/top/3.png'],
    }

    #######################################################################
    victory_flags = []
    img = 'victory/flag.png'
    object_facilitator(len(victory_flags), victory_flags, Obstacles, img, 1, 500, 150, block_movement=False)  # end

    pygame.init()
    mixer.init()
    mixer.music.load('music/mushrooms/2.mp3')

    DISPLAY_WIDTH, DISPLAY_HEIGHT = 700, 700
    gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
    clock = pygame.time.Clock()

    while True:
        close_game_function()
        pygame.mixer.init()

        gameDisplay.fill((0, 0, 0))
        gameDisplay.blit(player.img, (player.x, player.y))
        # displaying walls, flags
        display_objects(gameDisplay, walls+red_mushrooms+yellow_mushrooms+victory_flags)

        key_pressed(pygame, player, walls + victory_flags,walls[0],walls[-1], DISPLAY_WIDTH, DISPLAY_HEIGHT, default_player_images,
                    default_player_images_counters, default_player_images_timer)

        #player gets mushroom
        player_obtain_mushroom_or_mushrooms = object_takes_object(player, red_mushrooms+yellow_mushrooms)
        #El atributo de bloquear al jugador sea falso
        if (player_obtain_mushroom_or_mushrooms != None and player_obtain_mushroom_or_mushrooms.visible == True):
            if len(player.color) > 0:
                default_player_images = transformation_images_combined

            else:
                default_player_images = player_obtain_mushroom_or_mushrooms.transformation_images  # give mushroom image to player
            player.color.append(player_obtain_mushroom_or_mushrooms.color)
            player_obtain_mushroom_or_mushrooms.visible = False #Make mushroom invisible
            mixer.music.play()
            start = time.time()



        end = time.time()
        try:
            if (end-start) > 6:
                player.color = []
                default_player_images = default_player_images_copy
                mixer.music.stop()
        except:
            pass



        #player gets flag
        player_obtain_flag_or_flags = object_takes_object(player, victory_flags)
        if player_obtain_flag_or_flags != None:
            break

        clock.tick(60)
        pygame.display.update()
