################################################################################
# Concentric
#
# Playing around with concentric circles
# 
# Based on the talented Paul Rickards: 
# https://twitter.com/paulrickards/status/1028651749555560448
#
# Aaron Penne 
# 2018-08-21
# https://github.com/aaronpenne
################################################################################

# Define globals here
# rand_seed = 22
frame_rate = 1
x = 777
w = 1000  # width, previously 700
h = 1618  # height, previously 1000
pad = h/2
pad_pct = 0.09


        
        
def setup():
    # Sets size of canvas in pixels (must be first line)
    size(w, h) # (width, height)
    
    # Sets resolution dynamically (affects resolution of saved image)
    pixelDensity(displayDensity())  # 1 for low, 2 for high
    
    # Sets color space to Hue Saturation Brightness with max values of HSB respectively
    # colorMode(HSB, 360, 100, 100, 100)
        
    # Set the number of frames per second to display
    frameRate(frame_rate)
        
    # Set the psuedorandom seed
    # randomSeed(rand_seed)
    
    # Set (x, y) for circles to center
    ellipseMode(CENTER)
    
    
    background(0, 0, 24.7)
    
    # Stops draw() from running in an infinite loop (should be last line)
    noLoop()



def draw():
    vertical_steps = 22 # previously 20
    horizontal_steps = 4
    circle_size = 146 # perviously 100
    # odd rows
    pushMatrix()
    rotate(radians(0))
    translate(-125,70) # previously -75,40
    initial_fill = 255
    for i in range(1,vertical_steps,2):
        for j in range(1,horizontal_steps+1):
            concentric_circles(j*w/horizontal_steps,i*h/vertical_steps,False,ceil(i/2 + 1),circle_size,(vertical_steps-i)*initial_fill/vertical_steps)
        

    # even rows
    shift = w/8
    color_base = 0
    for i in range(0,vertical_steps,2):
        concentric_circles(1*w/4 + shift,i*h/vertical_steps,False,ceil(i/2 + 1),circle_size,color(255-(i*255/vertical_steps),color_base,color_base))
        concentric_circles(2*w/4 + shift,i*h/vertical_steps,False,ceil(i/2 + 1),circle_size,color(color_base,255-(i*255/vertical_steps),color_base))
        concentric_circles(3*w/4 + shift,i*h/vertical_steps,False,ceil(i/2 + 1),circle_size,color(color_base,color_base,255-(i*255/vertical_steps)))
    popMatrix()
    num_lines = 100
    # for i in range(num_lines):
     #   line(1,random(h)-1,w-1,random(h)-1)

    border()
    save("/Users/josephkaiser/circles.tif")
    
def concentric_circles(x=100, y=100, randumb=False, num_circles=4, outer_radius=110, color_fill='#ffffff', color_stroke='#000000', weight=1):
        step = outer_radius / num_circles
        radius = outer_radius
        base_color = random(256)
        base_red = random(256)
        base_green = random(256)
        base_blue = random(256)
        for i in range(0,num_circles+1):
            print(i, radius)
            if radius > 2:
                if randumb:
                    # fill(random(256),random(256),random(256))
                    # fill(base_color/(i+1))
                    fill(base_red/(i+1),base_green/(i+1),base_blue/(i+1))
                else:
                    fill(color_fill)
                ellipse(x, y, radius, radius)
            else:
                pass
            radius -= step
            

        
def border():
    noStroke()
    fill('#ffffff')
    rect(0, 0, width, height*pad_pct)  # Top
    rect(0, 0, width*pad_pct, height)  # Left
    rect(0, height - height*pad_pct, width, height*pad_pct)  # Bottom
    rect(width - width*pad_pct, 0, width*pad_pct, height)  # Right
    
def cool_noise(h,w,noiseVal=0,noiseScale=0.02):

    for y in range(h):
        for x in range(w):
            noiseDetail(3, 0.5)
            noiseVal = noise(
                x * noiseScale, y * noiseScale)
            stroke(noiseVal * 255)
            point(x, y)
            noiseDetail(8, 0.65)
            noiseVal = noise((x + w/2) * noiseScale,
                        y * noiseScale)
            stroke(noiseVal * 255)
            point(x + w/2, y)
