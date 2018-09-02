import pygame
from star import *

screen_width, screen_height = 800, 800

speed = 4

def map(number, min1, max1, min2, max2):
	return ((number - min1)/(max1-min1)) * (max2-min2)+min2

def main():

	pygame.init()
	logo = pygame.image.load("../Images/icon.png")
	pygame.display.set_icon(logo)
	pygame.display.set_caption("Sample Text")

	screen = pygame.display.set_mode((screen_width, screen_height))

	stars = [Star() for i in range(800)]


	running = True

	#main loop
	while running:

		#event handler
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		mouseX = pygame.mouse.get_pos()[0]

		speed = map(mouseX, 0, screen_width, 0, 50)

		#draw
		screen.fill((0,0,0))

		for star in stars:
			star.update(speed)
			star.show(screen)


		#update the screen
		
		pygame.display.flip()
		pygame.time.delay(20)


if __name__ == "__main__":

	main()
