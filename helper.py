def distance(x1,y1,x2,y2):
    return sqrt( pow((y2 - y1),2) + pow((x2 - x1),2) )

def generate_pts_min_dist_apart(width, height, min_dist, num_pts):
    points = {}
    for i in range(num_pts):
        if i > 0:
            found_valid_point = False
            while not found_valid_point:
                x = int(random(width))
                y = int(random(height))
                found_valid_point = True
                for j in range(1,i+1):
                    if distance(x,y,points[i-j][0],points[i-j][1]) < min_dist:  # at least one point is too close
                        found_valid_point = False
                        break
                if found_valid_point:
                    points[i] = (x,y)
                    break
        else:
            x = int(random(width))
            y = int(random(height))
            points[i] = (x,y)

    return points

def draw_asterisk(x,y,num_lines,asterisk_size):
    for i in range(num_lines):
        pushMatrix()
        translate(x,y)
        rotate(i*PI/num_lines)
        line(-asterisk_size,asterisk_size,asterisk_size,-asterisk_size)
        popMatrix()

def linear_gradient():
    for i in range(height):
        stroke(255 - (i * 255 / height))
        line(0,i,width,i)

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

def draw_line(x,y,theta,l):
    # Convert theta from degrees to radians
    theta_rad = radians(theta)
    
    # Calculate the endpoint of the line
    end_x = x + l * cos(theta_rad)
    end_y = y + l * sin(theta_rad)
    
    # Draw the line
    line(x, y, end_x, end_y)
    
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