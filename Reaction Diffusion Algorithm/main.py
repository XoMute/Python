import pygame
import pygame.gfxdraw
from math import *
from random import *

screen_width, screen_height = 200, 200

def constrain(val, min_val, max_val):
    return min(max_val, max(min_val, val))

def laplaceA(grid, x, y):

	sumA = 0
	sumA += grid[x][y]['a'] * (-1)
	sumA += grid[x - 1][y]['a'] * 0.2
	sumA += grid[x][y - 1]['a'] * 0.2
	sumA += grid[x + 1][y]['a'] * 0.2
	sumA += grid[x][y + 1]['a'] * 0.2
	sumA += grid[x + 1][y + 1]['a'] * 0.05
	sumA += grid[x + 1][y - 1]['a'] * 0.05
	sumA += grid[x - 1][y + 1]['a'] * 0.05
	sumA += grid[x - 1][y - 1]['a'] * 0.05
	return sumA


def laplaceB(grid, x, y):

	sumB = 0
	sumB += grid[x][y]['b'] * (-1)
	sumB += grid[x - 1][y]['b'] * 0.2
	sumB += grid[x][y - 1]['b'] * 0.2
	sumB += grid[x + 1][y]['b'] * 0.2
	sumB += grid[x][y + 1]['b'] * 0.2
	sumB += grid[x + 1][y + 1]['b'] * 0.05
	sumB += grid[x + 1][y - 1]['b'] * 0.05
	sumB += grid[x - 1][y + 1]['b'] * 0.05
	sumB += grid[x - 1][y - 1]['b'] * 0.05
	return sumB


def main():

	pygame.init()
	logo = pygame.image.load("../Images/icon.png")
	pygame.display.set_icon(logo)
	pygame.display.set_caption("Reaction Diffusion Algorithm")

	screen = pygame.display.set_mode((screen_width, screen_height))

	grid = []

	for x in range(screen_width):	#creating a 2D grid with "a" and "b" in each cell
		grid.append([])
		for y in range(screen_height):
			grid[x].append({
				"a" : 1,
				"b" : 0
			})

	nextGrid = grid

	for x in range(100, 110):
		for y in range(100, 110):
			grid[x][y]['b'] = 1

	

	dA = 1.0
	dB = 0.5
	feed = 0.055
	kill = 0.062

	running = True

	#main loop
	while running:

		#event handler
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		screen.fill((0,0,0))

		for x in range(1, screen_width - 1):
			for y in range(1, screen_height - 1):
				a = grid[x][y]['a']
				b = grid[x][y]['b']
				nextGrid[x][y]['a'] = (a 
									+ (dA * laplaceA(grid, x, y))
									- (a * b * b) + (feed * (1 - a))
									)
	
				nextGrid[x][y]['b'] = (b 
									+ (dB * laplaceB(grid, x, y))
									+ (a * b * b) - (kill + feed) * b
									)
				nextGrid[x][y]['a'] = constrain(nextGrid[x][y]['a'], 0, 1)
				nextGrid[x][y]['b'] = constrain(nextGrid[x][y]['b'], 0, 1)
				#draw
				a = nextGrid[x][y]['a']
				b = nextGrid[x][y]['b']
				c = floor((a - b)*255)
				c = constrain(c, 0, 255)

				r = c
				g = c
				b = c

				pixelColor = (r,g,b)
				#print(pixelColor)
				pygame.gfxdraw.pixel(screen, x, y, pixelColor)
				


						
		
		grid = nextGrid
		
		#update the screen

		pygame.display.flip()
		#some delay for better visuals
		#pygame.time.delay(20)


if __name__ == "__main__":

	main()
