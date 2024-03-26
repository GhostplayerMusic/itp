def setup():
    size(800, 800) # Set the size of canvas
    noStroke() # Disable drawing the stroke
    
def drawObject(x,y,s):
    push()
    translate(x,y)
    scale(s)
    fill(0)
    ellipse(100, 100, 90, 90)
    ellipse(50,50,60,60)
    ellipse(150,50,60,60)
    fill(255)
    arc(100,100, 80, 80, 0, PI, CHORD)
    ellipse(125, 83, 20, 20) # Draw ellipses
    ellipse(75, 83, 20, 20)
    pop()
    
div = 6 #Grid Division

t= 800/div
s = t/159.
def draw():
    for i in range(div):
        x=i*800/div
        for j in range(div):
            y=j*800/div
            drawObject(x-20*s,y,s)
        
    
