import pygame
from particle import *
from math import *

screen_width, screen_height = 600, 600

screenDiagonal = sqrt(screen_width**2 + screen_height**2)
screenDiagonalsqr = screen_width**2 + screen_height**2

particleCount = 1000

hashedHSV = []

def map(number, min1, max1, min2, max2):
	return ((number - min1)/(max1-min1)) * (max2-min2)+min2

def constrain(val, min_val, max_val):
	return min(max_val, max(min_val, val))

def hashHSV():
	global hashedHSV

	for i in range(360):
		h = i
		tempC = 1
		tempX = tempC * (1 - abs((h/60)%2 - 1))
		m = 0

		if h < 60:
			tempR, tempG, tempB = tempC, tempX, 0
		elif h < 120:
			tempR, tempG, tempB = tempX, tempC, 0
		elif h < 180:
			tempR, tempG, tempB = 0, tempC, tempX
		elif h < 240:
			tempR, tempG, tempB = 0, tempX, tempC
		elif h < 300:
			tempR, tempG, tempB = tempX, 0, tempC
		elif h < 360:
			tempR, tempG, tempB = tempC, 0, tempX

		red = (tempR + m) * 255
		green = (tempG + m) * 255
		blue = (tempB + m) * 255
		hashedHSV.append((red, green, blue))



def main():

	pygame.init()
	#logo = pygame.image.load("../Images/icon.png")
	#pygame.display.set_icon(logo)
	pygame.display.set_caption("Sample Text")

	screen = pygame.display.set_mode((screen_width, screen_height))

	clock = pygame.time.Clock()

	particles = [Particle(randint(0, screen_width), randint(0, screen_height)) for i in range(particleCount)]
	
	attractor = pygame.math.Vector2()

	toAttract = False

	LBPressed = False

	screen.fill((51, 51, 51))

	running = True

	# main loop
	while running:

		# event handler
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.MOUSEBUTTONDOWN:
				if pygame.mouse.get_pressed()[0]:
					attractor = pygame.math.Vector2(pygame.mouse.get_pos())
					LBPressed = True
				else:
					LBPressed = False

			if event.type == pygame.MOUSEBUTTONUP:
				LBPressed = False
				
			if event.type == pygame.MOUSEMOTION:
				if pygame.mouse.get_pressed()[0]:
					attractor = pygame.math.Vector2(pygame.mouse.get_pos())
					LBPressed = True
				else:
					LBPressed = False


		if LBPressed:
			toAttract = True
		else:
			toAttract = False
		# draw
		screen.fill((0,0,0))

		for particle in particles:
			if toAttract:
				particle.attracted(attractor)
			particle.update()
			particle.show(screen)
		
		clock.tick(60)
		# update the screen
		pygame.display.flip()


if __name__ == "__main__":

	main()
