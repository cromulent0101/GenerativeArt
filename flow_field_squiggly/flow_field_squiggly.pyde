# Define variables for the size of the grid cells and the number of columns and rows
cell_size = 20
cols, rows = 0, 0
# Define an array to hold the angle of each vector in the flow field
field = []
line_color = color(129,129,129,40)
randomness_scale = TWO_PI
num_lines = 1000 # should be a square
num_steps = 10
step_size = 10
draw_vectors = False



def setup():
    global cols, rows, field
    size(800, 800)
    background(255)
    noiseDetail(1,0.1)
    noLoop()
    
    cols = int(width / cell_size)
    rows = int(height / cell_size)
    
    # Initialize the field with random angles
    for i in range(rows):
        new_row = []
        for j in range(cols):
            new_row.append(((noise(i * cell_size, j * cell_size))-0.5) * randomness_scale)
        field.append(new_row)


     
    
def draw():
    global field
    
    # Draw the flow field
    if draw_vectors:
        for y in range(rows):
            for x in range(cols):
                ## Get the angle for this cell
                angle = field[y][x]
                
                ## Calculate the x and y coordinates for the center of this cell
                x_pos = x * cell_size + cell_size // 2
                y_pos = y * cell_size + cell_size // 2
                
                ## Calculate the endpoint for the vector
                x_end = x_pos + cos(angle) * cell_size * 0.4
                y_end = y_pos + sin(angle) * cell_size * 0.4
                
                ## Draw the vector
                stroke(0)
                #strokeWeight(1)
                fill(0)
                line(x_pos, y_pos, x_end, y_end)
                ellipse(x_end, y_end, 4, 4)
            

    
    #pushMatrix()
    for i in range(int(sqrt(num_lines))):
        
        # rotate(radians(0.1))
        for j in range(int(sqrt(num_lines))):
            x = i * width / int(sqrt(num_lines))
            y = j * height / int(sqrt(num_lines))
            beginShape()
            noFill()
            for n in range(num_steps):
                #stroke(color(120,120,120,num_steps-n))
                stroke(line_color)
                curveVertex(x, y)
                column_index = int(x / cell_size)     # 200/20 = 10
                row_index = int(y / cell_size)
        
                # NOTE: normally you want to check the bounds here 
                if column_index < cols and row_index < rows:
                    grid_angle = field[row_index][column_index]
                    print("grid angle is", grid_angle)
                    x_step = step_size * cos(grid_angle)     
                    y_step = step_size * sin(grid_angle)
                
                    x = x + x_step     
                    y = y + y_step
                else:
                    break
            
            endShape()
    # popMatrix()
    
