import pygame, sys, random
from Wall import Wall
from Player import Player
pygame.init()

clock = pygame.time.Clock()

width = 978
height = 645
size = width, height

bgColor = r,g,b = 0, 0, 0

screen = pygame.display.set_mode(size)
bgImage = pygame.image.load("Resources/Objects/Backgrounds/dungeon are lvl 1.PNG")
bgRect = bgImage.get_rect()

walls = [Wall([0,0],[338,68]),
         Wall([48,133],[145,164]),
         Wall([0,68],[48,230]),
         Wall([0,230],[15, 260]),
         Wall([0,260],[48,611]),
         Wall([242,326],[302,386]),
         Wall([45,355],[205,386]), 
         Wall([0,615],[978,648]),
         Wall([947,0],[957,543]),
         Wall([273,132],[366,163]),
         Wall([337,163],[364,290]),
         Wall([782,228],[910,257]), 
         Wall([434,36],[465,98]),
         Wall([337,0],[972,32]),
         Wall([462,70],[497,230]),
         ]
         
player = Player([25,245])        
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
    
    for wall in walls:
        player.collideWall(wall)
    
    bgColor = r,g,b
    screen.fill(bgColor)
    screen.blit(bgImage, bgRect)
    for wall in walls:
        screen.blit(wall.image, wall.rect)
    screen.blit(player.image, player.rect)
    pygame.display.flip()
    clock.tick(60)
bgColor = r,g,b

        
