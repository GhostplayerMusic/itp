def setup():
    size(200, 200) # Set the size of canvas
    noStroke() # Disable drawing the stroke

def draw():
    fill(0)
    ellipse(100, 100, 90, 90)
    ellipse(50,50,60,60)
    ellipse(150,50,60,60)
    fill(255)
    arc(100,100, 80, 80, 0, PI, CHORD)
    ellipse(125, 83, 20, 20) # Draw ellipses
    ellipse(75, 83, 20, 20)
    
