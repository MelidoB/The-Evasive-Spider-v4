def no_obstacle_on_leftside(character, obstacles):
    for obstacle in obstacles:
            if obstacle.block_movement: #blocks the player movement
                condition_1 = character.x < obstacle.x - 70
                condition_2 = character.y > obstacle.y - 82
                condition_3 = character.x < obstacle.x + obstacle.img.get_width()
                condition_4 = character.y < obstacle.y + obstacle.img.get_height() - 20

                if not condition_1 and condition_2 and condition_3 and condition_4:
                    if obstacle.color in character.color:
                        continue
                    return False

    return True

def no_obstacle_on_rightside(character, obstacles):
    for obstacle in obstacles:
        if obstacle.block_movement:
            condition_1 = character.x > obstacle.x - 100
            condition_2 = character.y > obstacle.y - 82
            condition_3 = character.x > obstacle.x + obstacle.img.get_width() - 20
            condition_4 = character.y < obstacle.y + obstacle.img.get_height() - 20

            if condition_1 and condition_2 and not condition_3 and condition_4:
                if obstacle.color in character.color:
                    continue
                return False
    return True


def no_obstacle_on_topside(character, obstacles):
    for obstacle in obstacles:
        if obstacle.block_movement:
            condition_1 = character.x < obstacle.x - 86
            condition_2 = character.y > obstacle.y
            condition_3 = character.x < obstacle.x + obstacle.img.get_width() - 10
            condition_4 = character.y < obstacle.y + obstacle.img.get_height()

            if not condition_1 and condition_2 and condition_3 and condition_4:
                if obstacle.color in character.color:
                    continue
                return False
    return True

def no_obstacle_on_downside(character, obstacles):
    for obstacle in obstacles:
        if obstacle.block_movement:
            condition_1 = character.x > obstacle.x - 90
            condition_2 = character.y > obstacle.y - 105
            condition_3 = character.x < obstacle.x + obstacle.img.get_width() -10
            condition_4 = character.y > obstacle.y + obstacle.img.get_height() - 20

            if condition_1 and condition_2 and condition_3 and not condition_4:
                if obstacle.color in character.color:
                    continue
                return False
    return True