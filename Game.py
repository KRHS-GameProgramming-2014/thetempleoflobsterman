import pygame, sys, random

pygame.init()

clock = pygame.time.Clock()

width = 978
height = 645
size = width, height

bgColor = r,g,b = 0, 0, 0

screen = pygame.display.set_mode(size)
bgImage = pygame.image.load("Resources/Objects/Backgrounds/dungeon are lvl 1.PNG")
bgRect = bgImage.get_rect()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
		
		
	bgColor = r,g,b
	screen.fill(bgColor)
	screen.blit(bgImage, bgRect)
	pygame.display.flip()
	clock.tick(60)
