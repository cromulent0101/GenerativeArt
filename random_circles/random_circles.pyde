# Define variables for the size of the grid cells and the number of columns and rows
# Define an array to hold the angle of each vector in the flow field
from helper import distance, generate_random_pts_min_dist_apart

field = []
num_circles = 9
biggest_circle_r = 240
smallest_circle_r = 40
minimum_distance = biggest_circle_r
circle_weight = 15
line_weight_factor = 0.1
lookback = 2

def setup():
    global cols, rows, field
    size(800, 800)
    background(120)
    ellipseMode(CENTER)
    noLoop()
    
def draw():
    points = generate_random_pts_min_dist_apart(width,height, minimum_distance, num_circles)
    for i in range(num_circles):
        if i > 0:
            x = points[i][0]
            y = points[i][1]
            dist_line = (distance(x,y,points[i-1][0],points[i-1][1]))
            strokeWeight(int(dist_line*line_weight_factor))
            stroke(0)
            line(x,y,points[i-1][0],points[i-1][1])
            strokeWeight(5)
            stroke(random(255),random(255),random(255))
            line(x,y,points[i-1][0],points[i-1][1])
            
    for i in range(num_circles):
        strokeWeight(circle_weight)
        stroke(0)
        circle(points[i][0],points[i][1],smallest_circle_r + int(random(biggest_circle_r - smallest_circle_r)))


    
