import pygame
import sys

def close_game_function():
    """Close the game function when clicking exit"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # if it is quit the game
            pygame.quit()
            sys.exit()