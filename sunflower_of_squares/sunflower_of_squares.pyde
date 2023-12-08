# Define variables for the size of the grid cells and the number of columns and rows
cell_size = 20
cols, rows = 0, 0
# Define an array to hold the angle of each vector in the flow field
field = []
line_color = color(129,129,129,40)
threshold = 10
rotation_angle = PI/16
s = 200



def setup():
    global cols, rows, field
    size(800, 800)
    background(255)
    noFill()
    noiseDetail(1,0.1)
    rectMode(CENTER)
    stroke(line_color)
    strokeWeight(10)
    noLoop()

    
def draw():
    s = 500
    i = 1
    while s > threshold:
        pushMatrix()
        translate(width/2,height/2)
        rotate(rotation_angle*i)
        square(0,0,s)
        popMatrix()
        s = s * cos(rotation_angle)
        i = i + 1
    
