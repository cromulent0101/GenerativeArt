# Define variables for the size of the grid cells and the number of columns and rows
gradient = False
num_pts = 12
triangle_radius = 31
circle_spacing = 40
rotation_factor = 0.023
radial_expansion_factor = 0.06


from helper import distance

def setup():
    global cols, rows, field
    ellipseMode(CENTER)
    size(800, 800)
    background(120)
    frameRate(1)
    noLoop()

    if gradient:
        for i in range(height):
            stroke(255 - (i * 255 / height))
            line(0,i,width,i)
            
    
    
def draw():
    noStroke()

    center = [width/2,height/2]
    # radial_gradient(width/2,height/2,1000,color(1,255,1),color(255,1,1),125)
    for radius in range(0,width/2,circle_spacing):
        points = points_on_circle(center[0],center[1],radius,num_pts,radius*rotation_factor)
        for k, v in points.iteritems():
            fill(255,255*(width/2 - radius)/(width/2),255*(len(points)-k)/len(points),130)
            pushMatrix()
            # rotate(radius/1000)
            draw_equilateral_triangle(v[0], v[1], degrees(atan2((v[1]-center[1]),(v[0]-center[0]))), triangle_radius+radius*radial_expansion_factor)
            draw_equilateral_triangle(v[0], v[1], degrees(atan2((v[1]-center[1]),(v[0]-center[0])))+180, (triangle_radius+radius*radial_expansion_factor)/2)
            popMatrix()
    #rotation_factor = rotation_factor + 1


    
def points_on_circle(cx,cy,r,num_pts,offset):
    pts = {}
    for i in range(num_pts):
        angle = i * TWO_PI / num_pts + offset;
        x = cx + cos(angle) * r;
        y = cy + sin(angle) * r;
        pt = (x,y)
        pts[i] = pt
    return pts


def draw_equilateral_triangle(x_center, y_center, theta, radius):
    # Convert theta from degrees to radians
    theta_rad = radians(theta)
    # Calculate the first vertex
    x1 = x_center + radius * cos(theta_rad)
    y1 = y_center + radius * sin(theta_rad)
    
    # Initialize the list of vertices
    vertices = [(x1, y1)]
    
    # Calculate the other two vertices by rotating the first vertex around the center by +/- 120 degrees
    for phi in [120, -120]:
        phi_rad = radians(phi)
        x_new = x_center + (x1 - x_center) * cos(phi_rad) - (y1 - y_center) * sin(phi_rad)
        y_new = y_center + (x1 - x_center) * sin(phi_rad) + (y1 - y_center) * cos(phi_rad)
        vertices.append((x_new, y_new))
    triangle(vertices[0][0],vertices[0][1],vertices[1][0],vertices[1][1],vertices[2][0],vertices[2][1])
    # fill(0)
    # text(str(theta),x_center,y_center)

def radial_gradient_whole_canvas(width,height,start_color,stop_color,num_steps):
    noStroke()
    for i in range(num_steps):
        if i == 0:
            circle_color = start_color
        elif i == (num_steps-1):
            circle_color = stop_color
        else:
            circle_color = lerpColor(start_color,stop_color,(i*1.0/num_steps))
        
        radius = ((num_steps-i)*1.0/num_steps)*distance(0,0,width/2,height/2)
        fill(circle_color)
        circle(width/2,height/2,radius*2)
        

def radial_gradient(x,y,radius,start_color,stop_color,num_steps):
    noStroke()
    for i in range(num_steps):
        if i == 0:
            circle_color = start_color
        elif i == (num_steps-1):
            circle_color = stop_color
        else:
            circle_color = lerpColor(start_color,stop_color,(i*1.0/num_steps))
        
        iteradius = ((num_steps-i)*1.0/num_steps)*radius
        fill(circle_color)
        circle(x,y,iteradius*2)
    
    
    
    
