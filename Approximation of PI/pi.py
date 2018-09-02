import random
import math
import pygame
from pygame import gfxdraw

def main():

	pygame.init()
	logo = pygame.image.load("../Images/icon.png")
	pygame.display.set_icon(logo)
	pygame.display.set_caption("Approximation of PI")

	screen = pygame.display.set_mode((402,402))

	screen.fill((0,0,0))

	r = 200

	total = 0
	circle = 0

	recordPI = 0

	running = True

	#main loop
	while running:

		#event handler
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		for i in range(10000):

			x, y = random.uniform(0, r*2), random.uniform(0, r*2)
			total += 1
			distance = (x - 200)**2 + (y - 200)**2
			if distance < r**2:
				circle += 1
				pygame.gfxdraw.pixel(screen, int(x), int(y), (255,217,49))
			else:
				pygame.gfxdraw.pixel(screen, int(x), int(y), (0,81,184))

		pi = 4 * (circle/total)
		recordDiff = math.fabs(math.pi - recordPI)
		diff = math.fabs(math.pi - pi)
		if diff < recordDiff:
			recordDiff = diff
			recordPI = pi
			print(recordPI)

	
	#draw
		pygame.draw.circle(screen, (255,255,255), (200, 200), r, 4)
		pygame.draw.rect(screen, (255,255,255), [0,0,r*2,r*2], 4)
		#update the screen
		pygame.display.flip()


if __name__ == "__main__":

	main()
