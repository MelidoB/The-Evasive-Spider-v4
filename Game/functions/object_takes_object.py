def object_takes_object(object_1,objects):

    for object in objects:
        conditions = [
            object_1.x > object.x - 90,
            object_1.y > object.y - 82,
            object_1.x < object.x + object.img.get_width() - 20,
            object_1.y < object.y + object.img.get_height() - 20]

        if all(conditions):
            return object