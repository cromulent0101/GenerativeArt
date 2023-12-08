# Define variables for the size of the grid cells and the number of columns and rows
cell_size = 250
color_noise_scale = -10
gradient = False
shape_color=color(255,255,255)



def setup():
    global cols, rows, field
    ellipseMode(CENTER)
    size(1000, 1000)
    background(0)
    noStroke()
    noLoop()
        
    cols = int(width / cell_size) # 1000 / 10 = 100
    rows = int(height / cell_size)
    
    if gradient:
        for i in range(height):
            stroke(255 - (i * 255 / height))
            line(0,i,width,i)
    

    
def draw():
    recursion_chance = 5
    for i in range(rows):
        for j in range(cols):
            #print('i is ',i)
            #print('j is ',j)
            draw_random_shape_in_square(i*width/cols,j*height/rows,cell_size,shape_color,cell_size,recursion_chance)
            stroke(0)
            # line(i*width/cols,j*height/rows,i*width/cols+cell_size,j*height/rows)
            # line(i*width/cols+cell_size,j*height/rows,i*width/cols+cell_size,j*height/rows+cell_size)


    
def draw_random_shape_in_square(start_x,start_y,s,shape_color,circle_dia,recusion_chance): # x, y upper left point of square
    if s > 8:
        
        shape_type = int(random(recusion_chance)) # 0 circle, 1 rect, 2 triangle
        print(shape_type)
        print('shape is',shape_type)
        print('start_x',start_x)
        fill(shape_color)
    
        if shape_type == 0: # circle
            circle(start_x + s/2, start_y + s/2, circle_dia)
        elif shape_type == 1: # rect, or recurse???
            shape_orientation = int(random(4))
            if shape_orientation == 0:
                triangle(start_x,start_y, start_x+s, start_y, start_x,start_y+s)
            elif shape_orientation == 1:
                triangle(start_x,start_y, start_x+s, start_y, start_x+s,start_y+s)
            elif shape_orientation == 2:
                triangle(start_x+s,start_y, start_x+s, start_y+s, start_x,start_y+s)
            else:
                triangle(start_x,start_y, start_x, start_y+s, start_x+s,start_y+s)
        else:
            print('recursion time')
            s = s/2
            draw_random_shape_in_square(start_x,start_y,s,color(red(shape_color)/2+int(noise(start_x,start_y)*color_noise_scale),green(shape_color),blue(shape_color),alpha(shape_color)),circle_dia/2,recusion_chance)
            draw_random_shape_in_square(start_x+s,start_y,s,color(red(shape_color),green(shape_color)/2+int(noise(start_x,start_y)*color_noise_scale),blue(shape_color),alpha(shape_color)),circle_dia/2,recusion_chance)
            draw_random_shape_in_square(start_x,start_y+s,s,color(red(shape_color),green(shape_color),blue(shape_color)/2+int(noise(start_x,start_y)*color_noise_scale),alpha(shape_color)),circle_dia/2,recusion_chance)
            draw_random_shape_in_square(start_x+s,start_y+s,s,shape_color,circle_dia/2,recusion_chance)
        

    
    
    
    
    
    
    
    
