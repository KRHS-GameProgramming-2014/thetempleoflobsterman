import pygame, sys, random
from Wall import Wall
from Player import Player
from Enemy2 import Enemy
pygame.init()

clock = pygame.time.Clock()

width = 978
height = 645
size = width, height

bgColor = r,g,b = 0, 0, 0

screen = pygame.display.set_mode(size)
bgImage = pygame.image.load("dungeon are lvl 1.PNG")
bgRect = bgImage.get_rect()

walls =[Wall([0,0],[338,68]),
        Wall([48,133],[145,164]),
        Wall([0,68],[48,230]),
        Wall([0,230],[15, 260]),
        Wall([0,260],[48,611]),
        Wall([242,326],[302,386]),
        Wall([45,355],[205,386]), 
        Wall([0,615],[978,648]),
        Wall([946,0],[977,549]),
        Wall([273,132],[366,163]),
        Wall([337,133],[368,292]),
        Wall([785,228],[913,260]), 
        Wall([434,36],[465,98]),
        Wall([0,0],[977,36]),
        Wall([462,70],[497,230]),
        Wall([177,388],[206,514]),
        Wall ([496,198],[592,229]),
        Wall([560,230],[590,290]),
        Wall([881,196],[913,260]),
        Wall([817,421],[980,452]),
        Wall([305,0],[336,164]),
        Wall([338,452],[367,611]),
        Wall([369,455],[590,482]),
        Wall([945,581],[977,644]),
        Wall([624,0],[655,166]),
        Wall([624,132],[848,165]),
        Wall([786,100],[848,164]),
        Wall([754,68],[816,100]),
        Wall([753,0],[785,100]),
        Wall([753,293],[980,324]),
        Wall([753,261],[785,324]),
        Wall([658,454],[783,484]),
        Wall([753,420],[783,650]),
        Wall([785,69],[816,164])] 
         
player = Player([25,245])        
        #100 #100
enemy  = Enemy([330,325])
        #100 #100

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                player.go("up")
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                player.go("right")
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                player.go("down")
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                player.go("left")
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                player.go("stop up")
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                player.go("stop right")
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                player.go("stop down")
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                player.go("stop left")
    player.update(width, height)
    
    enemy.update(width, height)
    
    for wall in walls:
        player.collideWall(wall)
        enemy.collideWall(wall)
    
    bgColor = r,g,b
    screen.fill(bgColor)
    screen.blit(bgImage, bgRect)
    for wall in walls:
        screen.blit(wall.image, wall.rect)
    screen.blit(player.image, player.rect)
    screen.blit(enemy.image, enemy.rect)
    pygame.display.flip()
    clock.tick(60)
bgColor = r,g,b

        
