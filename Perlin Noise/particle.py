import pygame
from main import *

class Particle:

	def __init__(self):
		self.pos = pygame.math.Vector2(randint(1, screen_width), randint(1, screen_height - 1))
		self.vel = pygame.math.Vector2(0)
		self.acc = pygame.math.Vector2(0)

	def update(self):
		self.vel += self.acc
		self.pos += self.vel
		self.acc *= 0
		self.edges()

	def applyForce(self, force):
		self.acc += force

	def show(self, screen):
		pygame.draw.circle(screen, (0, 0, 0), (int(self.pos.x), int(self.pos.y)), 2)
		#pygame.gfxdraw.pixel(screen, int(self.pos.x), int(self.pos.y), (0, 0, 0))

	def edges(self):
		if self.pos.x > screen_width:
			self.pos.x = 0
		if self.pos.x < 0:
			self.pos.x = screen_width
		if self.pos.y > screen_height:
			self.pos.y = 0
		if self.pos.y < 0:
			self.pos.y = screen_height

	def follow(self, vectors):
		x = floor(self.pos.x / scl)
		y = floor(self.pos.y / scl)
		print("Corrected x = ", x, "Corrected y = ", y)
		print("x =", self.pos.x, "y = ", self.pos.y)
		index = x + y * cols
		print(cols, index)
		force = vectors[index]
		self.applyForce(force)