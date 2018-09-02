import pygame
import main
import particle
from random import *

class Firework:

	def __init__(self):
		self.firework = particle.Particle(randint(0, main.screen_width), main.screen_height, True)
		self.exploded = False
		self.particles = []

	def explode(self):
		self.particles = [particle.Particle(
			int(self.firework.pos.x), int(self.firework.pos.y), False
		) for x in range(0, 100)]

	def update(self):
		if not self.exploded:
			self.firework.applyForce(main.gravity)
			self.firework.update()

			if self.firework.vel.y >= -0.5:
				self.exploded = True
				self.explode()
		else:
			for x in self.particles:
				x.applyForce(main.gravity)
				x.update()


	def show(self, screen):
		if not self.exploded:
			self.firework.show(screen)
		else:
			for x in self.particles:
				x.show(screen)




