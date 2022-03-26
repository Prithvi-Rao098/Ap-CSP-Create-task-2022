import pygame, sys

class Player(pygame.sprite.Sprite):
	def __init__(self, pos_x, pos_y):
		super().__init__()
		self.attack_animation = False
		self.sprites = []
		self.sprites.append(pygame.image.load("assets", "MC", "MC_P1.png"))
		self.sprites.append(pygame.image.load("assets", "MC", "MC_P2.png"))
		self.sprites.append(pygame.image.load("assets", "MC", "MC_P3.png"))
		self.sprites.append(pygame.image.load("assets", "MC", "MC_P4.png"))
		self.sprites.append(pygame.image.load("assets", "MC", "MC_P5.png"))
		self.sprites.append(pygame.image.load("assets", "MC", "MC_P6.png"))
		self.sprites.append(pygame.image.load("assets", "MC", "MC_P7.png"))

		self.current_sprite = 0
		self.image = self.sprites[self.current_sprite]

		self.rect = self.image.get_rect()
		self.rect.topleft = [pos_x,pos_y]

	def attack(self):
		self.attack_animation = True

	def update(self,speed):
		if self.attack_animation == True:
			self.current_sprite += speed
			if int(self.current_sprite) >= len(self.sprites):
				self.current_sprite = 0

		self.image = self.sprites[int(self.current_sprite)]

# General setup
pygame.init()
clock = pygame.time.Clock()

# Game Screen
WIDTH, HEIGHT = 750, 750
WIN = pygame.display.set_mode((WIDTH,HEIGHT))


# Creating the sprites and groups
moving_sprites = pygame.sprite.Group()
player = Player(0,0)
moving_sprites.add(player)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		
		player.attack()

	# Drawing
	WIN.fill((0,0,0))
	moving_sprites.draw(WIN)
	moving_sprites.update(0.25)
	pygame.display.flip()
	clock.tick(60)