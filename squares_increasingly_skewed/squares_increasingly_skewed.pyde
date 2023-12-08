# Define variables for the size of the grid cells and the number of columns and rows
cell_size = 70
gradient = False
num_pts = 10
triangle_radius = 60
square_radius = 400

def setup():
    global cols, rows, field
    ellipseMode(CENTER)
    size(800, 800)
    background(255)
    noFill()
    noLoop()

    if gradient:
        for i in range(height):
            stroke(255 - (i * 255 / height))
            line(0,i,width,i)
            
    
    
def draw():
    cols = int(width / cell_size)
    rows = int(height / cell_size)
    
    center = [width/4,height/4]
    
    # Initialize the field with random angles
    offset_x = 1
    offset_y = 1
    randomness_scale = 1
    for i in range(offset_x,rows-offset_x):
        for j in range(offset_y,cols-offset_y):
            center_x = width * i / cols
            center_y = height * j / rows
            draw_square(center_x,center_y,45+random(j)*randomness_scale*(random(1)-0.5)*j,cell_size, color(0,0,0,2*(random(j)*randomness_scale*(random(1))*j)),color(255))
    



def draw_square(x_center, y_center, theta, side, stroke_color, fill_color):
    # Convert theta from degrees to radians
    theta_rad = radians(theta)
    # Calculate the first vertex
    x1 = x_center + side/sqrt(2) * cos(theta_rad)
    y1 = y_center + side/sqrt(2) * sin(theta_rad)
    
    # Initialize the list of vertices
    vertices = [(x1, y1)]
    
    # Calculate the other two vertices by rotating the first vertex around the center by +/- 120 degrees
    for phi in [90, 180, -90]:
        phi_rad = radians(phi)
        x_new = x_center + (x1 - x_center) * cos(phi_rad) - (y1 - y_center) * sin(phi_rad)
        y_new = y_center + (x1 - x_center) * sin(phi_rad) + (y1 - y_center) * cos(phi_rad)
        vertices.append((x_new, y_new))
    stroke(stroke_color)
    fill(fill_color)
    quad(vertices[0][0],vertices[0][1],vertices[1][0],vertices[1][1],vertices[2][0],vertices[2][1],vertices[3][0],vertices[3][1])
    # fill(0)
    # text(str(theta),x_center,y_center)



    
    
    
    
