import pygame, sys, random
from Wall import Wall
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
		 ]
		 
		 
		 

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
		
	bgColor = r,g,b
	screen.fill(bgColor)
	screen.blit(bgImage, bgRect)
	for wall in walls:
		screen.blit(wall.image, wall.rect)
	pygame.display.flip()
	clock.tick(60)
bgColor = r,g,b

		
