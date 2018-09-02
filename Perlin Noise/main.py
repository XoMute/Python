import pygame
from particle import *
from pygame import gfxdraw
from noise import *
from random import *
from math import *

screen_width, screen_height = 200, 200

def direction(vector):
    """Return the direction component of a vector (in radians), given
    cartesian coordinates.
    """
    if vector.x > 0:
        if vector.y >= 0:
            return atan(vector.y / vector.x)
        else:
            return atan(vector.y / vector.x) + pi * 2
    elif vector.x == 0:
        if vector.y > 0:
            return pi / 2
        elif vector.y == 0:
            return 0
        else:
            return pi * 1.5
    else:
        return atan(vector.y / vector.x) + pi

def map(number, min1, max1, min2, max2):
	return ((number - min1)/(max1-min1)) * (max2-min2)+min2

def polarToDecart(len, start, angle):
	eX = len * cos(angle) + start[0];
	eY = len * sin(angle) + start[1];

	return [int(eX), int(eY)]

scl = 10
cols = int(screen_width / scl)
rows = int(screen_height / scl)

def main():

	pygame.init()
	logo = pygame.image.load("../Images/icon.png")
	pygame.display.set_icon(logo)
	pygame.display.set_caption("Perlin Noise Flow Field")

	clock = pygame.time.Clock()

	screen = pygame.display.set_mode((screen_width, screen_height))

	alphaSurf = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)

	inc = 0.1

	zoff = 0.1

	

	particles = [Particle() for i in range(0, 100)]

	
	#create array of (1, 0) vectors with rotation of 0
	flowfield = [pygame.math.Vector2(1, 0) for i in range(0, rows*cols)]

	#print(direction(pygame.math.Vector2(0, 10)))

	running = True

	#main loop
	while running:

		#event handler
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_d:
					inc += 0.01
				if event.key == pygame.K_a:
					inc -= 0.01
				if event.key == pygame.K_r:
					inc = 0.1

		#draw
		screen.fill((255,255,255))
		alphaSurf.fill((255,255,255,50))

		yoff = 0
		for y in range(rows):
			xoff = 0
			for x in range(cols):

				index = x + y * cols

				start = [x * scl, y * scl]
				#print("NOISE = ", pnoise3(xoff, yoff, zoff))
				#angle = map(pnoise3(xoff, yoff, zoff), -1, 1, 0, pi* 2) #* pi * 2
				angle = pnoise3(xoff, yoff, zoff) * pi * 2
				end = polarToDecart(scl, start, angle)
				print("angle =", degrees(angle))

				
				flowfield[index].rotate(degrees(angle))
				print(flowfield[index])
				pygame.draw.line(alphaSurf, (0, 0, 0, 50), start, end)
				xoff += inc

			yoff += inc

		#zoff += 0.003

		screen.blit(alphaSurf, (0, 0))

		for particle in particles:
			particle.update()
			particle.show(screen)


		clock.tick()
		#print(clock.get_fps())

		#update the screen
		
		pygame.display.flip()
		#some delay for better visuals
		#pygame.time.delay(20)


if __name__ == "__main__":

	main()
