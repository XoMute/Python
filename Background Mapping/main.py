import pygame

screen_width, screen_height = 640, 360

def map(number, min1, max1, min2, max2):
	return ((number - min1)/(max1-min1)) * (max2-min2)+min2

def main():

	pygame.init()
	logo = pygame.image.load("../Images/icon.png")
	pygame.display.set_icon(logo)
	pygame.display.set_caption("Sample Text")

	screen = pygame.display.set_mode((screen_width, screen_height))

	running = True

	#main loop
	while running:

		#event handler
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		mouseX = pygame.mouse.get_pos()[0]
		bgColor = map(mouseX, 0, 640, 0, 255)

		#draw
		screen.fill((bgColor, bgColor, bgColor))

		#update the screen
		pygame.display.flip()


if __name__ == "__main__":

	main()
