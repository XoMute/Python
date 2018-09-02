import pygame
from random import *
from particle import *
from firework import *

screen_width, screen_height = 400, 300

gravity = pygame.math.Vector2(0, 0.2)

def main():

	pygame.init()
	logo = pygame.image.load("../Images/icon.png")
	pygame.display.set_icon(logo)
	pygame.display.set_caption("Sample Text")

	screen = pygame.display.set_mode((screen_width, screen_height))

	fireworks = []
	
	running = True

	#main loop
	while running:

		#event handler
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
		if uniform(0, 1) < 0.05:
			fireworks.append(Firework())


		#draw
		screen.fill((51,51,51))
		for firework in fireworks:
			firework.update()
			firework.show(screen)
		
		#update the screen
		
		pygame.display.flip()
		#some delay for better visuals
		pygame.time.delay(20)


if __name__ == "__main__":

	main()
