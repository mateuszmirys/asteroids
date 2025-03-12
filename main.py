import pygame
from player import Player
from constants import *

def main():
	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	dt = 0

	x = SCREEN_WIDTH / 2
	y = SCREEN_HEIGHT / 2
	player = Player(x, y)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

		pygame.Surface.fill(screen, (0, 0, 0))
		player.update(dt)
		player.draw(screen)
		pygame.display.flip()
		clock.tick(60)
		dt = clock.tick(60) / 1000
	
if __name__ == "__main__":
	main()
