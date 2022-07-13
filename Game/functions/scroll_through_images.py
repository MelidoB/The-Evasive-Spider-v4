def scroll_through_images(character, default_player_images,default_player_images_counters, default_player_images_timer, direction):
    if default_player_images_timer[direction] > 10:
        character.set_img(default_player_images[direction][default_player_images_counters[direction]])
        if default_player_images_counters[direction] < len(default_player_images[direction]) - 1:
            default_player_images_counters[direction] += 1
        else:
            default_player_images_counters[direction] = 0
        default_player_images_timer[direction] = 0
    else:
        default_player_images_timer[direction] += 1