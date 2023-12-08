line_color = color(90,20,9,50)
other_line_color = color(43,49,200,100)
threshold = 1
weight = 15
rotation_angle = PI/13



def setup():
    global cols, rows, field
    size(800, 800)
    background(255)
    noFill()
    noiseDetail(1,0.1)
    rectMode(CENTER)
    stroke(line_color)
    strokeWeight(weight)
    noLoop()

    
def draw():
    s = 800
    i = 1
    while True:
        # s = s * 0.848
        s = s * cos(rotation_angle)
        if s < threshold:
            break
        pushMatrix()
        if i % 2 == 0:
            stroke(line_color)
        else:
            stroke(other_line_color)
        translate(width/2,height/2)
        rotate(rotation_angle*i)
        square(0,0,s)
        popMatrix()
        i = i + 1
    
