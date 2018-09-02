import pygame
from random import *
from rain import *

rainColor = (138, 43, 226)

class Drop:
	x = 0
	y = 0
	z = 0
	zMax = 20
	yspeed = 0
	length = 0
	thickness = 0

	def __init__(self):
		self.x = randint(0, screen_width)
		self.y = randint(-500, -50)
		self.z = randint(0, self.zMax)
		self.update(0, self.zMax)

	def update(self, min1, max1):
		self.yspeed = map(self.z, min1, max1, 4, 10)
		self.length = map(self.z, min1, max1, 10, 20)
		self.thickness = map(self.z, min1, max1, 1, 3)

	def fall(self):
		self.y += self.yspeed
		gravity = map(self.z, 0, 20, 0.01, 0.2)
		self.yspeed += gravity
		if self.y > screen_height:
			self.y = randint(-200, -100)
			self.yspeed = map(self.z, 0, self.zMax, 4, 10)

	def show(self, screen):
		pygame.draw.line(
			screen, rainColor, 
			[self.x, self.y], 
			[self.x, self.y + self.length],
			int(self.thickness)
		)
		
