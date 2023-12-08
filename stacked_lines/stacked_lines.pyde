stroke_transparency = 200
transparency = 100
gradient = False
num_lines = 100
num_points = 40
num_rectangles = 4
min_area = 20000
min_dimension = 150
perturbation = 30
diameter = 400
stroke_weight = 2

neighbor_threshold = 19


import helper

def setup():
    ellipseMode(CENTER)
    rectMode(RADIUS)
    colorMode(RGB)
    size(800, 800)
    noFill()
    background(255)
    noLoop()
    
    if gradient:
        for i in range(height):
            stroke(255 - (i * 255 / height)/2)
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
            print(i)
            i = i+1
    popMatrix()
    
    
    strokeWeight(stroke_weight)
    stroke(0,0,0,stroke_transparency)
    initial_points = []
    pushMatrix()
    #translate(0,100)
    max_value_close_to_top = 50
    # get a list of random y coordinates near the top of the canvas
    for i in range(num_points):
        initial_points.append(random(max_value_close_to_top))
        
    print(initial_points)
        
        
    # for each line, draw line, perturb the points by some small amount
    for i in range(num_lines):
        beginShape()
        for j in range(num_points):
            curveVertex(int(width*(j*1.0/num_points)), initial_points[j])
            if j > 0:
                if initial_points[j] - initial_points[j-1] < neighbor_threshold:
                    initial_points[j] = initial_points[j] + random(perturbation)
                else:
                    #pass
                    initial_points[j] = initial_points[j] - random(perturbation)
        endShape()
    



    
    save("/Users/josephkaiser/stacked_lines.tif")
