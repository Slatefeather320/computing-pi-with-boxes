import pygame

class box:
    def __init__(self, x, y, vx, vy, color, xsize, ysize, mass):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.color = color
        self.xsize = xsize
        self.ysize = ysize
        self.mass = mass

b1 = box(100,100,0.1,0,(255,0,0),100,100, 10000)
b2 = box(800,100,0,0,(0,0,255),100,100, 1)

# make window
window = pygame.display.set_mode((1200,200))
cancolide = True
colcount = 0

#frame cleaning and drawing next frame
def drawframe():
    
    window.fill((0,0,0)) #clears screen
    
    pygame.draw.rect(window,b1.color,(b1.x, b1.y, b1.xsize, b1.ysize))
    pygame.draw.rect(window,b2.color,(b2.x, b2.y, b2.xsize, b2.ysize))
    pygame.display.update() #updates frame


def updatepos():
    b1.x += b1.vx
    b2.x += b2.vx


def calphysics():
    global cancolide, colcount
    if abs(b1.x - b2.x) < 100:
        if cancolide:
            b1.vx = ((b1.vx*(b1.mass - b2.mass)) + (2*b2.mass*b2.vx)) / (b1.mass + b2.mass)
            b2.vx = ((b2.vx*(b2.mass - b1.mass)) + (2*b1.mass*b1.vx)) / (b1.mass + b2.mass)
            cancolide = False
            colcount +=1
            print(colcount) 
    else: 
        cancolide = True
    
    #if b1.x <= 0:
        #b1.vx = abs(b1.vx)
    if b2.x > 1200-b2.xsize:
        b2.vx = abs(b2.vx) * -1
        colcount +=1
        print(colcount)



#active loop 
active = True

while active:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         active = False

   #main game loop
   drawframe()
   updatepos()
   calphysics()


