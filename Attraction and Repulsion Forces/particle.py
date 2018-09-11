import pygame
from pygame import gfxdraw
from random import *
import main
from math import *


main.hashHSV()

class Particle:

	def __init__(self, x, y):

		self.pos = pygame.math.Vector2(x, y)
		self.prevPos = pygame.math.Vector2()
		self.prevPos.x = self.pos.x
		self.prevPos.y = self.pos.y
		self.vel = pygame.math.Vector2()
		self.acc = pygame.math.Vector2()
		self.dist = 0

	def update(self):
		self.vel += self.acc
		self.pos += self.vel
		self.acc *= 0

	def show(self, screen):
		tempDist = main.constrain(self.dist, 0, main.screenDiagonal * 0.5)
		index = floor(main.map(tempDist, 0, main.screenDiagonal * 0.5, 0, 359))
		color = main.hashedHSV[index]
		pygame.draw.line(screen, color, [int(self.pos.x), int(self.pos.y)], 
											[int(self.prevPos.x), int(self.prevPos.y)])
		#pygame.gfxdraw.pixel(screen, int(self.pos.x), int(self.pos.y), color)
		self.prevPos.x = self.pos.x
		self.prevPos.y = self.pos.y


	def attracted(self, target):
		force = target - self.pos
		dsquared = force.length_squared()
		self.dist = force.length()
		dsquared = main.constrain(dsquared, 5, 50)
		G = 15
		strength = G / dsquared
		if force.length_squared() > 0.01:# cannot scale_to_length zero vector
			force.scale_to_length(strength)
		self.acc += force
	
