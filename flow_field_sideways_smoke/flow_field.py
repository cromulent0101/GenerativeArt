# Define variables for the size of the grid cells and the number of columns and rows
cell_size = 20
cols, rows = 0, 0
# Define an array to hold the angle of each vector in the flow field
field = []

def setup():
    global cols, rows, field
    size(800, 800)
    background(255)
    
    cols = int(width / cell_size)
    rows = int(height / cell_size)
    
    # Initialize the field with random angles
    for i in range(rows):
        new_row = []
        for j in range(cols):
            new_row.append(random(TWO_PI))
        field.append(new_row)

def draw():
    global field
    
    # Draw the flow field
    for y in range(rows):
        for x in range(cols):
            # Get the angle for this cell
            angle = field[y][x]
            
            # Calculate the x and y coordinates for the center of this cell
            x_pos = x * cell_size + cell_size // 2
            y_pos = y * cell_size + cell_size // 2
            
            # Calculate the endpoint for the vector
            x_end = x_pos + cos(angle) * cell_size * 0.4
            y_end = y_pos + sin(angle) * cell_size * 0.4
            
            # Draw the vector
            stroke(0)
            strokeWeight(1)
            fill(0)
            line(x_pos, y_pos, x_end, y_end)
            ellipse(x_end, y_end, 4, 4)
