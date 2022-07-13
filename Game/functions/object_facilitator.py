
def object_facilitator(n,lista, CLASS,img, c,x,y,direction='right', color="None",block_movement = True):


    x_i = 0
    y_i = 0
    for i in range(n, n+c):
        lista.append(CLASS())
        lista[i].set_coordinates(x + x_i, y + y_i)
        lista[i].set_img(img)
        lista[i].set_color(color)

        if block_movement == True:
            lista[i].set_block_movement()

        if 'left' in direction:
            x_i -= 100
        if 'right' in direction:
            x_i += 100
        if 'up' in direction:
            y_i -= 100
        if 'down' in direction:
            y_i += 100
