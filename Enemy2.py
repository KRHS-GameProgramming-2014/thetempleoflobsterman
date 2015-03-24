import pygame

class Enemy():
    def __init__(self, pos, speed=[1,3]):
        self.upImages =    [pygame.image.load("Resources/Objects/Enemy/skeleu.PNG")]

        self.leftImages =  [pygame.image.load("Resources/Objects/Enemy/skelel3.PNG")]

        self.rightImages = [pygame.image.load("Resources/Objects/Enemy/skeler3.PNG")]

        self.downImages =  [pygame.image.load("Resources/Objects/Enemy/skeled.PNG")]

        self.facing = "up"
        self.changed = False
        self.images = self.upImages
        self.frame = 0
        self.facing = "down"
        self.changed = False
        self.images = self.downImages
        self.frame = 0
        self.facing = "right"
        self.changed = False
        self.images = self.rightImages
        self.frame = 0
        self.facing = "left"
        self.changed = False
        self.images = self.leftImages
        self.frame = 0
        self.maxFrame = len(self.images) - 1
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect(center = pos)
        self.waitCount = 0
        self.maxWait = 60*.25
        self.maxSpeed = speed[0]
        self.speedx = speed[0]
        self.speedy = speed[1]
        self.speed = [self.speedx, self.speedy]
         
    def update(self, width, height):
        self.didBounceX = False
        self.didBounceY = False
        self.move()
        self.collideEdge(width, height)
        self.animate()
        self.changed = False
    
    def move(self):
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)
        
    def collideEdge(self, width, height):
        if not self.didBounceX:
            #print "trying to hit Wall"
            if self.rect.left < 0 or self.rect.right > width:
                self.didBounceX = True
                self.speedx = 6
                #print "hit xWall"
        if not self.didBounceY:
            if self.rect.top < 0 or self.rect.bottom > height:
                self.didBounceY = True
                self.speedy = 6
                #print "hit yWall"
    
    def animate(self):       
        if self.changed:    
            if self.facing == "up":
                self.images = self.upImages
            elif self.facing == "down":
                self.Images = self.downImages
            elif self.facing == "right":
                self.Images = self.rightImages
            elif self.facing == "left":
                self.images = self.leftImages
            
            self.image = self.images[self.frame]
            
    def collideWall(self, other):
        if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
            if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                if not self.didBounceX:
                    self.speedx = -self.speedx
                    self.didBouncex = True
                if not self.didBounceY:
                    self.speedy = -self.speedy
                    self.didBounceY = True
                    #print "hit Ball"
                    
    def distance(self, pt):
        x1 = self.rect.center[0]
        y1 = self.rect.center[1]
        x2 = pt[0]
        y2 = pt[1]
        return math.sqrt(((x2-x1)**2) + ((y2-y1)**2))

         
