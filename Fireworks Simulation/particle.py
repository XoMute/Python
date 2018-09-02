import pygame
from main import *

class Particle:

	def __init__(self, x, y, firework):
		self.pos = pygame.math.Vector2(x, y)
		self.firework = firework
		self.lifespan = 255
		if self.firework:
			self.vel = pygame.math.Vector2(0, uniform(-11, -5))
		else:
			a = uniform(uniform(-1, 1) * uniform(1, 6), uniform(-1, 1)* uniform(1, 6))
			b = uniform(uniform(-1, 1) * uniform(1, 6), uniform(-1, 1) * uniform(1, 6))
			self.vel = pygame.math.Vector2(a, b)
		self.acc = pygame.math.Vector2(0, 0)

	def applyForce(self, force):
		self.acc += force

	def update(self):
		if not self.firework:
			self.vel *= 0.9
			self.lifespan -= 4
			if self.lifespan < 0:
				self.lifespan = 0
		self.vel += self.acc
		self.pos += self.vel
		self.acc *= 0
		

		
	def show(self, screen):
		if self.firework:
			color = (255,255,255)
			pygame.draw.circle(screen, color, (int(self.pos.x), int(self.pos.y)), 3)
		else:
			color = (255,255,255,self.lifespan)
			pygame.draw.circle(screen, color, (int(self.pos.x), int(self.pos.y)), 2)
		