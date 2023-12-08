gradient = False
num_rectangles = 5
border_weight = 1
diameter = 400
threshold = 5


import helper

def setup():
    ellipseMode(CENTER)
    rectMode(RADIUS)
    colorMode(HSB)
    size(800, 800)
    background(255)
    noStroke()
    #frameRate(1)
    noLoop()

    if gradient:
        for i in range(height):
            stroke(255 - (i * 255 / height))
            line(0,i,width,i)
            
    

def draw():
    strokeWeight(border_weight)
    stroke(0)
    fill(0,0,0,0)
    pushMatrix()
    translate(width/2,-height/4)
    rotate(PI/4)
    x = width/2
    y = height/2
    print(threshold)
    dia = 600
    for i in range(0,10):
        #rotate(PI/4)
        fill(255*(i*1.0/10),255,255,120)
        new_diameter = dia / (pow(sqrt(2),i))
        circle(x,y,new_diameter*2)
        fill(255*(i*1.0/10)+12,255,255,120)
        new_diameter = dia / (pow(sqrt(2),i+1))
        # print(sqrt(2))
        print(new_diameter)
        square(x,y,new_diameter)
    
    popMatrix()
    
    #save("/Users/josephkaiser/circumscribe.tif")
