import pygame, math

class Wall():
	def __init__(self, tl, br):
		self.image = pygame.image.load("Resources/Objects/Wall/Wall.png")
		width = br[0] - tl[0]
		height = br[1] - tl[1]
		self.image = pygame.transform.scale(self.image, [width, height])	
		self.rect = self.image.get_rect(topleft = tl)
