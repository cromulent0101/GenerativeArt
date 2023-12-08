# Define variables for the size of the grid cells and the number of columns and rows
cell_size = 100
shape_color=color(0,0,0,128)

gradient = True



def setup():
    global cols, rows, field
    ellipseMode(CENTER)
    size(1000, 1000)
    background(255)
    noLoop()
        
    cols = int(width / cell_size) # 1000 / 10 = 100
    rows = int(height / cell_size)
    
    if gradient:
        for i in range(height):
            stroke(255 - (i * 255 / height))
            line(0,i,width,i)
    

    
def draw():
    for i in range(rows):
        for j in range(cols):
            #print('i is ',i)
            #print('j is ',j)
            pushMatrix()
            translate(random(15),random(15))
            draw_random_shape_in_square(i*width/cols,j*height/rows,s=cell_size,shape_color=shape_color,circle_radius=cell_size)
            popMatrix()

    
def draw_random_shape_in_square(start_x,start_y,s=10,shape_color=color(0,0,0),circle_radius=5): # x, y upper left point of square
    shape_type = int(random(3)) # 0 circle, 1 rect, 2 triangle
    print('shape is',shape_type)
    print('start_x',start_x)
    noStroke()
    fill(shape_color)

    if shape_type == 0: # circle
        circle(start_x + s/2, start_y + s/2, circle_radius)
    elif shape_type == 1: # rect
        shape_orientation = random(4) # 0 NW, 1 NE, 2 SE, 3 SW
        pass
    else:
        shape_orientation = int(random(4))
        if shape_orientation == 0:
            triangle(start_x,start_y, start_x+s, start_y, start_x,start_y+s)
        elif shape_orientation == 1:
            triangle(start_x,start_y, start_x+s, start_y, start_x+s,start_y+s)
        elif shape_orientation == 2:
            triangle(start_x+s,start_y, start_x+s, start_y+s, start_x,start_y+s)
        else:
            triangle(start_x,start_y, start_x, start_y+s, start_x+s,start_y+s)

    
    
    
    
    
    
    
    
