from functions.check_for_obstacles import *
from functions.scroll_through_images import scroll_through_images

def key_pressed(pygame, character, obstacles,default_player_images,default_player_images_counters,default_player_images_timer, left='a',right='d',top='w',down='s', map_x = 0, map_y = 0):
    key = pygame.key.get_pressed()

    if character.able_to_move:
        if key[ord(left)] and no_obstacle_on_leftside(character, obstacles):
            scroll_through_images(character, default_player_images,default_player_images_counters,default_player_images_timer, direction="left")
            map_x = 5
        if key[ord(right)] and no_obstacle_on_rightside(character, obstacles):
            scroll_through_images(character, default_player_images, default_player_images_counters,default_player_images_timer, direction="right")
            map_x = -5
        if key[ord(top)] and no_obstacle_on_topside(character, obstacles):
            scroll_through_images(character, default_player_images,default_player_images_counters,default_player_images_timer, direction="top")
            map_y  = 5
        if key[ord(down)] and no_obstacle_on_downside(character, obstacles):
            scroll_through_images(character, default_player_images, default_player_images_counters,default_player_images_timer, direction="down")
            map_y = -5

    return map_x, map_y