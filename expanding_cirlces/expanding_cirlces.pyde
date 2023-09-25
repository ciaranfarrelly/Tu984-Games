def setup():
    size(500,500)
    background(0)
    global x1
    global y1
    x1 = width/2
    y1 = width/2
    global x2
    global y2
    x2 = width/2
    y2 = width/2
    global x3
    global y3
    x3 = width/2
    y3 = width/2    
    global x4
    global y4
    x4 = width/2
    y4 = width/2
    global radius
    
    global h
    global s
    global b

y1 = 0
x1 = 0

y2 = 0
x2 = 0

y3 = 0
x3 = 0

y4 = 0
x4 = 0
radius = 0

h = 80
s = 70
b = 50


def draw():
    global x1
    global y1
    
    global x2
    global y2
    
    global x3
    global y3
    
    global x4
    global y4
    
    global radius
    
    global h
    global s
    global b
    
    colorMode(HSB)

    fill(h,s,b)
    h += 2
    s += 3
    b += 1
    noStroke()
    
    if x < 375 :
        radius += 1
    else:
        radius -= 1

    
    circle(x1, y1, radius)
    x1 += 1
    y1 -= 1
    circle(x2, y2, radius)
    x2 += 1
    y2 += 1
    circle(x3, y3, radius)
    x3 -= 1
    y3 += 1
    circle(x4, y4, radius)
    x4 -= 1
    y4 -= 1
