line_color = color(0,255,9,255)
other_line_color = color(255,9,9,255)
threshold = 10
rotation_angle = PI/10
weight = 2



def setup():
    global cols, rows, field
    size(800, 800)
    background(255)
    noFill()
    noiseDetail(1,0.1)
    rectMode(CENTER)
    stroke(line_color)
    strokeWeight(1)
    noLoop()

    
def draw():
    s = width
    i = 1
    strokeWeight(weight)
    while True:
        # strokeWeight(weight-i)
        s = s / (cos(rotation_angle) + sin(rotation_angle))
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
        pushMatrix()
        # stroke(other_line_color)
        # translate(width/2,height/2)
        # rotate(rotation_angle*i*(-1))
        # square(0,0,s)
        popMatrix()
        i = i + 1
    
