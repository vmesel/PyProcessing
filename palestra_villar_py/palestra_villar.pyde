# Conteudo dado na palestra do Villar
# GruPy Hacker - Garoa Hacker Clube
# Data: 16/07/2016 no Garoa Hacker Clube


def setup():
    fill(255,255,255,50)
    size(600,400)
# rect(point, point, width, height)
def draw():
    fill(255,100,100,50)
    rect(mouseX, mouseY, 50, 70)
    noStroke()
    
def mousePressed():
    background(128)
    
def mouseDragged():
    ellipse(mouseX, mouseY, 50, 50)