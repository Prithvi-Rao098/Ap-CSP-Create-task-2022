import pygame
import os
import random
import math
pygame.font.init()


pygame.init()

# initilizing the SCREENdow screen
WIDTH, HEIGHT = 800, 1000
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join("background.jpg")), (WIDTH, HEIGHT))
MAINCHARACTER = pygame.transform.scale(pygame.image.load(os.path.join("MAINCHARACTER.png")), (55, 50))
BULLET = pygame.transform.scale(pygame.image.load(os.path.join("bullet.png")), (30, 42))
INVADER1 = pygame.transform.scale(pygame.image.load(os.path.join("invader.png")), (55, 50))
INVADER2 = pygame.transform.scale(pygame.image.load(os.path.join("invader.png")), (75, 60))
INVADER3 = pygame.transform.scale(pygame.image.load(os.path.join("invader.png")), (85, 70))

MC_imge = pygame.transform.rotate(MAINCHARACTER, 90)
Bullet_image = pygame.transform.rotate(BULLET,-90)
Invader1_image = pygame.transform.rotate(BULLET,90)
Invader2_image = pygame.transform.rotate(BULLET,90)
Invader3_image = pygame.transform.rotate(BULLET,90)


# ADD NAME
pygame.display.set_caption( " !!!@@@@ ----  ENTER NAME LATER  ----@@@@!!!  - Prithvi Rao")

#PARENT CLASSES
class Bullet:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.bullet_img = Bullet_image
        self.mask = pygame.mask.from_surface(self.bullet_img)
    
    def move(self, vel):
        self.y += vel

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def off_screen(self, height):
        return not(self.y <= height and self.y >= 0)

    def collision(self, obj):
        return collide(self, obj)




class Character:            # parent class for the defenders and invaders

    COOLDOWN = 50

    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.MC_img = MC_imge             #pass later in the inheritence 
<<<<<<< HEAD
        self.mask = pygame.mask.from_surface(self.MC_img)
=======
        self.INVADER_img = None
>>>>>>> parent of a3c1989 (get enemies to collide)
        self.bullet_img = Bullet_image        
        self.bullets = []                         #LIST FOR bulletS
        self.cool_down_counter = 0

    def draw(self, window):
        window.blit(self.MC_img, (self.x, self.y))
        for bullet in self.bullets:
            bullet.draw(window)

    def move_bullets(self, vel):
        self.cooldown()
        for bullet in self.bullets:
            bullet.move(vel)
            if bullet.off_screen(HEIGHT):
                self.bullets.remove(bullet)


    def cooldown(self):
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1

    def shoot(self):
        if self.cool_down_counter == 0:
            bullet = Bullet(self.x, self.y, self.bullet_img)
            self.bullets.append(bullet)
            self.cool_down_counter = 1

    def get_width(self):
        return self.MC_img.get_width()

    def get_height(self):
        return self.MC_img.get_height()

# child classes

class MainCharacter(Character):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.MC_img = MAINCHARACTER
        self.bullet_img = BULLET
        self.mask = pygame.mask.from_surface(self.MC_img)
        self.max_health = health

    def move_bullets(self, vel):
        self.cooldown()
        for bullet in self.bullets:
            bullet.move(vel)
            if bullet.off_screen(HEIGHT):
                self.bullets.remove(bullet)


    def draw(self, window):
        super().draw(window)
        self.healthbar(window)

    def healthbar(self, window):
        pygame.draw.rect(window, (255,0,0), (self.x, self.y + self.MC_img.get_height() + 10, self.MC_img.get_width(), 10))
        pygame.draw.rect(window, (0,255,0), (self.x, self.y + self.MC_img.get_height() + 10, self.MC_img.get_width() * (self.health/self.max_health), 10))


class Enemy(Character):

    ENEMY_MAP = {
                "small" : (Invader1_image),
                "medium" : (Invader2_image),
                "large" : (Invader3_image)
    }

    def __init__(self, x, y, type, health=2):
        super().__init__(x,y,health)
        self.INVADER_img= self.ENEMY_MAP[type]
        self.mask = pygame.mask.from_surface(self.INVADER_img)

    def move(self, vel):
        self.y+= vel






def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None



# initializing the characters and the images
run = True
FPS = 240
bullet_vel = 15
level = 0
lives = 1
player = Character(375, 900)
enemies = []
bullets = []
player_vel = 1
enemy_vel = 1
main_font = pygame.font.SysFont("comicsans", 50)
lost_font = pygame.font.SysFont("comicsans", 70)
wave_length = 5
num_loss = 0
lost = False
clock = pygame.time.Clock() 


def redraw_win():
    SCREEN.blit(BACKGROUND, (0,0))

    lives_show = main_font.render(f"lives: {lives}", 1, (0,0,255))
    level_show = main_font.render(f"level: {level}", 1, (255,0,0))

    SCREEN.blit(lives_show, (10, 600))
    SCREEN.blit(level_show, (10, 800))

    for enemy in enemies:
        enemy.draw(SCREEN)

    player.draw(SCREEN)
    if lost:
        lost_label=lost_font.render("YOU LOST !", 1 , (255,0,0))
        SCREEN.blit(lost_label, (WIDTH/2 - lost_label.get_width()/2, 350))

    
    pygame.display.update()





while run:
    clock.tick(FPS)
    redraw_win()

    if len(enemies) == 0:
        level += 1
        wave_length += 5
    

    if lives <= 0 or player.health <= 0:
        lost = True
        num_loss += 1
    if lost:
        if num_loss > FPS * 3:
            run = False
        else:
            continue 

    if len(enemies) == 0:
        level += 1
        wave_length += 5
        
        for i in range(wave_length):
<<<<<<< HEAD
            enemy = Enemy(random.randrange(290, WIDTH-350), random.randrange(-1500, -100), random.choice(["small", "medium", "large"]))
=======
            enemy = Enemy(random.randrange(50, WIDTH-100), random.randrange(-1500, -100), random.choice(["small", "medium", "large"]))
>>>>>>> parent of a3c1989 (get enemies to collide)
            enemies.append(enemy)

        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player.y - player_vel > 0:                                                             #up
        player.y -= player_vel

    if keys[pygame.K_a] and player.x -player_vel > 0 :                                                             #left
        player.x -= player_vel

    if keys[pygame.K_d] and player.x +player_vel + player.get_width() < WIDTH:                                     #right
        player.x += player_vel

    if keys[pygame.K_s] and player.y + player_vel + player.get_height() < HEIGHT:                                  #down
        player.y += player_vel

    if event.type == pygame.MOUSEBUTTONDOWN:
        player.shoot()
    for enemy in enemies[:]:
        enemy.move(enemy_vel)
    if collide(enemy, player):
        player.health -= 10
        enemies.remove(enemy)
    elif enemy.y + enemy.get_height() > HEIGHT:
        lives -= 1
        enemies.remove(enemy)

    player.move_bullets(-bullet_vel)