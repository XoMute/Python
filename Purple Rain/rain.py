import random
import math
import pygame
from drop import *
from pygame import gfxdraw

screen_width, screen_height = 640, 360

def map(number, min1, max1, min2, max2):
	return ((number - min1)/(max1-min1)) * (max2-min2)+min2

def main():

	pygame.init()
	logo = pygame.image.load("../Images/icon.png")
	pygame.display.set_icon(logo)
	pygame.display.set_caption("Purple Rain")

	screen = pygame.display.set_mode((screen_width, screen_height))

	bgColor = (230, 230, 250)

	drops = [Drop() for i in range(500)]

	zCounter = 0

	for drop in drops:
		if drop.z > 5:
			drop.zMax = 5
			drop.z = randint(0, drop.zMax)
			drop.update(0, drop.zMax)
			zCounter += 1
		if zCounter > 2:
			zCounter = 0


	running = True

	#main loop
	while running:

		#event handler
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		
		#update the screen
		screen.fill(bgColor)
		for drop in drops:
			drop.fall()
			drop.show(screen)

		pygame.display.flip()
		#delay for better visuals
		pygame.time.delay(10)


if __name__ == "__main__":

	main()
