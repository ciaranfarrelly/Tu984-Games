def setup():
    size(500, 500)
    
def draw():
    colorMode(HSB)
    # Greyscale
    # RGB
    # RGBA
    background(0)
    
    f = 10.0
    g = 20.0
    h = 5
    
    # Addition
    f = f + 1
    f += 1 # f = 12
    
    # Subtraction
    g -= 30
    g = g - 27 # g = -37
    
    # Multiplication
    g = f * h # g = 12 * 5 = 60
    h *= 2 # h = 10
    
    # Division
    g = f / h #  g =12 / 10 = 1.2
    h = h / 2.5 # h = 10 / 2.5 =  4
    
    # Indices
    f = pow(g, 2) # f = (1.2)2 = 1.44
    
    # f = 1.44
    # h = 4
    # g = 1.2
    
    h = h-7 # 4 - 7 = -3
    g += f # 1.2 + 1.44 = 1.64
    f += g # 1.44 + 1.64 = 3.08
    h = f - (g - 5) # = 3.08 + 3.36 = 6.44
    
    # f = 3.08
    # g = 1.64
    # h = 6.44
    
    print( "h: ", h)
    print( "g: ", g)
    print( "f: ", f)
    
    stroke(80, 255, 255)
    line(mouseX, 10, 100, mouseY)
    rect(20, 20, 50, 100)
    noStroke()
    
    circle(100, mouseY, 5)
    fill(90, mouseX / 2, 255)
    
    ellipse(200, 200, 100, 10)
    point(90, 100)
