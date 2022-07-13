from player.player import Player
from objects.obstacles import Obstacles
from functions.close_application import close_game_function
from functions.key_press import key_pressed
from functions.object_facilitator import object_facilitator
from functions.display_objects import display_objects
from functions.object_takes_object import object_takes_object
from objects.mushrooms import Mushrooms
from objects.portal import Portal

import pygame
from pygame import mixer
import time

def world_3():
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
    player.set_coordinates(300, 300)

    ######################################################
    walls = []
    walls_coord = [[1, 0, 0,'right','yellow'],
                    [5, 0, 0,'right', 'yellow'],
                    [5, 0, 400,'right', 'yellow'],
                    [3, 400, 100,'right', 'yellow'],
                    [3, 400, 300,'right', 'yellow'],
                    [4, 0, 0,'down', 'yellow'],
                    [1, 600, 200,'right', 'yellow'],
                    [1, 1000, 1000,'right', 'yellow']]
    # need the function to create walls with coordinates (A to B)
    img = 'obstacles/wall.png'

    for wall in walls_coord:
        object_facilitator(len(walls), walls, Obstacles, img, wall[0], wall[1], wall[2],wall[3],wall[4])  # start

    #######################################################################

    red_mushrooms = []
    yellow_mushrooms = []

    mushrooms_coords = [
        ['mushrooms/red/1.png', red_mushrooms, 1, 100, 150,'red'],
        ['mushrooms/yellow/1.png', yellow_mushrooms, 1, 300, 150, 'yellow'],
    ]
    ###red

    for element in mushrooms_coords:
        img = element[0]
        object_facilitator(len(element[1]), element[1], Mushrooms, img, element[2], element[3], element[4], 'right',element[5],block_movement=False)


    for mushroom in red_mushrooms + yellow_mushrooms:
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

    ########################### Portals ###########################################

    #Portal A to B
    portals = []
    portals_coords = [['portals/1.png',1,100,300],
                      ['portals/2.png', 1, 500, 500],
                      ]

    for element in portals_coords:
        img = element[0]
        amount_to_create = element[1]
        coord_x, coord_y =  element[2], element[3]

        object_facilitator(len(portals), portals, Portal, img, amount_to_create, coord_x, coord_y, 'right',block_movement=False)


    portal_coords = [[0, 0],
                     [0, 0]
                     ]
    for portal,portal_coords in zip(portals,portal_coords):
        portal.set_move_coords(portal_coords[0], portal_coords[1])

    ######################### Familiars ###############################
    friends = []

    img = 'familiars/1.png'

    object_facilitator(len(friends), friends, Obstacles, img, 1, 300, 500,block_movement=False)  # start

    ##############Visualizor #######################
    visualizers = []
    img = 'visualizers/2.png'
    object_facilitator(len(visualizers), visualizers, Obstacles, img, 1, 300, 500, block_movement=False)

    #######################################################################
    victory_flags = []
    img = 'victory/flag.png'
    object_facilitator(len(victory_flags), victory_flags, Obstacles, img, 1, 500, 150, block_movement=False)  # end

    pygame.init()
    mixer.init()

    #score
    pygame.font.init()
    my_font = pygame.font.SysFont('Comic Sans MS', 30)

    fonts_values = [
        ['0','Helped Comrades:']
    ]

    fonts = []

    for element in fonts_values:

        score_value = f'{element[0]}'
        score = my_font.render(f'{element[1]} {score_value}', False, (255, 255, 255))
        score_bg = my_font.render(f'{element[1]} {score_value}', False, (255, 255, 255), (255, 255, 255))
        score_bg.set_alpha(100)

        fonts.append([score_value,score,score_bg])

    mixer.music.load('music/mushrooms/2.mp3')

    DISPLAY_WIDTH, DISPLAY_HEIGHT = 700, 700
    gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
    clock = pygame.time.Clock()


    # I want the map to move base on the placer position
    map_x = 0
    map_y = 0
    # if I move the player

    while True:
        close_game_function()
        pygame.mixer.init()


        for element in fonts_values:
            score = my_font.render(f'{element[1]} {score_value}', False, (255, 255, 255))
            score_bg = my_font.render(f'{element[1]} {score_value}', False, (255, 255, 255), (255, 255, 255))
            score_bg.set_alpha(100)


        gameDisplay.fill((0, 0, 0))


        #Updating portal coords
        portal_coords = [[-350 ,-200],
                         [300,400]
                         ]

        #Setting portal Coords
        for portal, portal_coord in zip(portals, portal_coords):
            portal.set_move_coords(walls[0].x + portal_coord[0], walls[0].y + portal_coord[1])

        visualizers[0].set_coordinates(portals[1].x_move, portals[1].y_move)
        # displaying walls, flags
        display_objects(gameDisplay, walls+red_mushrooms+yellow_mushrooms+ friends + portals + victory_flags+visualizers)


        gameDisplay.blit(player.img, (player.x, player.y))
        gameDisplay.blit(score, (380, 0))  # score
        gameDisplay.blit(score_bg, (380, 0))  # score


        map_x, map_y = key_pressed(pygame,player,walls+red_mushrooms+yellow_mushrooms+ friends + portals + victory_flags,default_player_images,default_player_images_counters,default_player_images_timer)
        #player gets mushroom
        player_obtain_mushroom_or_mushrooms = object_takes_object(player, red_mushrooms+yellow_mushrooms)
        player_pass_through_portal = object_takes_object(player, portals)
        helped_friend = object_takes_object(player, friends)
        player_obtain_flag_or_flags = object_takes_object(player, victory_flags)

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

        #Portal




        if player_pass_through_portal != None:
            player.able_to_move = False
            map_x += player_pass_through_portal.x_move
            map_y += player_pass_through_portal.y_move


            player.able_to_move = True
            time.sleep(0.5)

        end = time.time()

        print(walls[0].x, walls[0].y, end="\t")
        print(portals[0].x_move, portals[0].y_move)


        try:
            time_in_between = end - start
            print(time_in_between)
            if (time_in_between) > 6:
                player.color = []
                default_player_images = default_player_images_copy
                mixer.music.stop()

        except:
            pass



        if not helped_friend == None and helped_friend.visible == True:
            score_value = int(score_value) + 1
            helped_friend.visible = False


        #player gets flag
        if player_obtain_flag_or_flags != None:
            break


        #Actualizar las coordenadas
        for element in walls+red_mushrooms+yellow_mushrooms+ friends +  visualizers + portals + victory_flags:
            element.set_coordinates(element.x+map_x,element.y+map_y)

        clock.tick(30)
        pygame.display.update()

