stroke_transparency = 255
square_transparency = 50
alternating_color = False
gradient = False
num_lines = 5
num_points = 200
num_rectangles = 6
min_area = 20000
min_dimension = 150
perturbation = 60
separation = 40
stroke_weight = 1

neighbor_threshold = 400


import helper

def setup():
    ellipseMode(CENTER)
    rectMode(RADIUS)
    colorMode(RGB)
    size(800, 800)
    noFill()
    background(128)
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
        fill(random(255),random(255),random(255),square_transparency)
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
    
    noFill()
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
        if alternating_color:
            if i % 2 == 0:
                stroke(255)
            else:
                stroke(0)
        beginShape()
        for j in range(num_points):
            initial_points[j] = initial_points[j] + separation
            curveVertex(int(width*(j*1.0/num_points)), initial_points[j])
            if j > 0:
                height_difference = (initial_points[j] - initial_points[j-1])
                if abs(height_difference) < neighbor_threshold and height_difference > 0: # if current point is further down than previous point
                    initial_points[j-1] = initial_points[j-1] + random(perturbation)
                elif abs(height_difference) < neighbor_threshold and height_difference < 0: # current point higher than prev
                    #pass
                    initial_points[j] = initial_points[j] + random(perturbation)
        endShape()
    



    
    save("/Users/josephkaiser/stacked_lines_rect_background.tif")
