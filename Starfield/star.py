from random import *
from main import *
import pygame
import main

class Star:
	x, y, z = 0, 0, 0
	r = 0
	pz = 0

	def __init__(self):
		self.x = randint(-screen_width / 2, screen_width / 2)
		self.y = randint(-screen_height / 2, screen_height / 2)
		self.z = randint(0, screen_width)
		self.r = map(self.z, 0, screen_width, 16, 0)
		self.pz = self.z

	def update(self, Speed):
		self.z -= Speed
		if self.z < 1:
			self.x = randint(-screen_width / 2, screen_width / 2)
			self.y = randint(-screen_height / 2, screen_height / 2)	
			self.z = screen_width
			self.pz = self.z

	def show(self, screen):
		
		sx = map(self.x/self.z, 0, 1, 0, screen_width) + screen_width / 2	#so center will become (0, 0)
		sy = map(self.y/self.z, 0, 1, 0, screen_height) + screen_height / 2

		self.r = map(self.z, 0, screen_width, 6, 0)

		pygame.draw.circle(
			screen, (255,255,255), 
			(int(sx), int(sy)), 
			int(self.r)
		)

		px = map(self.x/self.pz, 0, 1, 0, screen_width) + screen_width / 2
		py = map(self.y/self.pz, 0, 1, 0, screen_height) + screen_height / 2

		self.pz = self.z

		pygame.draw.line(
			screen, (255,255,255),
			(px, py), (sx, sy)
		)

		




