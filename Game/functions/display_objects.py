def display_objects(display, objects):
    for each_object in objects:
        if each_object.visible == True:
            display.blit(each_object.img, (each_object.x, each_object.y))