import pygame
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from circleshape import CircleShape
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

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = updatable
	Shot.containers = (shots, updatable, drawable)

	player = Player(x, y)
	asteroid_field = AsteroidField()

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

		pygame.Surface.fill(screen, (0, 0, 0))
		updatable.update(dt)
		for sprite in drawable:
			sprite.draw(screen)
		for asteroid in asteroids:
			if asteroid.collision_detection(player):
				print("Game over!")
				sys.exit()
			
			for shot in shots:
				if asteroid.collision_detection(shot):
					asteroid.split()
					shot.kill()

		pygame.display.flip()
		clock.tick(60)
		dt = clock.tick(60) / 1000
	
if __name__ == "__main__":
	main()
