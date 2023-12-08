gradient = False
num_rectangles = 4
transparency = 100 # out of 255
min_area = 20000
min_dimension = 150
border_weight = 0


import helper

def setup():
    ellipseMode(CENTER)
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
    strokeWeight(0)
    stroke(0)
    pushMatrix()
    translate(-width/2,-height/2)
    i = 0
    while i < num_rectangles:
        fill(random(255),random(255),random(255),transparency)
        x1 = random(width)
        y1 = random(height)
        x2 = random(width*2)
        y2 = random(height*2)
        
        if ( (x2 * y2) > min_area) and (x2 > min_dimension) and (y2 > min_dimension):
            print('x1 is ',x1,' and x2 is', x2)
            rect(x1,y1,x2,y2)
            # rect(random(x1),random(y1),random(x2),random(y2))
            print(i)
            i = i+1
    popMatrix()
    
    save("/Users/josephkaiser/rectangles_fullscreen.tif")
