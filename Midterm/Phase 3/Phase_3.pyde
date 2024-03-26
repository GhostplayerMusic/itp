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

def draw():    
    drawObject(0,0,1)
    drawObject(0,200,1)
        
    
