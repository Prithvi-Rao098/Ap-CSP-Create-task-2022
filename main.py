####################################################
#                  Pixel Gun 2-D                   #
#  By: Prithvi Rao                                 #
#  Teacher: Mr. Millard                            #
#  School: American High                           #
#  Class: AP Computer Science Principles           #
#
#
#
#
#
#
#


import pygame
import os
import random
import math
pygame.font.init()

pygame.init()

# initilizing the SCREENdow screen
WIDTH, HEIGHT = 800, 900
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
BACKGROUND = pygame.transform.scale(pygame.image.load(
    os.path.join("background.jpg")), (WIDTH, HEIGHT))
MAINCHARACTER = pygame.transform.scale(
    pygame.image.load(os.path.join("MAINCHARACTER.png")), (55, 50))
BULLET = pygame.transform.scale(
    pygame.image.load(os.path.join("bullet.png")), (33, 42))
INVADER1 = pygame.transform.scale(
    pygame.image.load(os.path.join("invader.png")), (39, 39))
INVADER2 = pygame.transform.scale(
    pygame.image.load(os.path.join("invader.png")), (55, 55))
INVADER3 = pygame.transform.scale(
    pygame.image.load(os.path.join("invader.png")), (85, 85))

MC_imge = pygame.transform.rotate(MAINCHARACTER, 90)
Bullet_image = pygame.transform.rotate(BULLET, -90)
Invader1_image = pygame.transform.rotate(INVADER1, -90)
Invader2_image = pygame.transform.rotate(INVADER2, -90)
Invader3_image = pygame.transform.rotate(INVADER3, -90)


# ADD NAME
pygame.display.set_caption(
    " PIXEL GUN 2-D  - Prithvi Rao")

# PARENT CLASSES


class Bullet:
    def __init__(self, x, y, mouse_x, mouse_y, bullet_vel, bullet_img):
        self.x = x
        self.y = y
        self.bullet_vel = 70
        angle = math.atan2(mouse_y - y, mouse_x-x)
        self.dx = math.cos(angle)*bullet_vel - 1.6
        self.dy = math.sin(angle)*bullet_vel - 1.6

        self.bullet_img = Bullet_image
        self.mask = pygame.mask.from_surface(self.bullet_img)

    def move(self, vel):
        self.x = self.x + self.dx
        self.y = self.y + self.dy

    def draw(self, window):
        window.blit(self.bullet_img, (self.x, self.y))

    def off_screen(self, height):
        return not(self.y <= height and self.y >= 0)

    def collision(self, obj):
        return collide(self, obj)


class Character:            # parent class for the defenders and invaders

    COOLDOWN = 15
    NUM_CLICKED = 20
    NUM_KILLED = 0

    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.CHACATER_img = None  # pass later in the inheritence
        self.bullet_img = None
        self.bullets = []  # LIST FOR bulletS
        self.cool_down_counter = 0

    def draw(self, window):
        window.blit(self.CHACATER_img, (self.x, self.y))
        for bullet in self.bullets:
            bullet.draw(window)

    def move_bullets(self, vel, obj):
        self.cooldown()
        for bullet in self.bullets:
            bullet.move(vel)
            if bullet.off_screen(HEIGHT):
                self.bullets.remove(bullet)
            elif bullet.collision(obj):
                obj.health -= 10
                self.NUM_KILLED += 1
                self.bulletswwwwwwwwwwwwww.remove(bullet)

    def cooldown(self):
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1

    def shoot(self):
        if self.cool_down_counter == 0:
            x, y = pygame.mouse.get_pos()
            # def __init__(self, x, y, mouse_x, mouse_y, bullet_vel, bullet_img):
            bullet = Bullet(self.x, self.y, x, y, 40, self.bullet_img)
            self.bullets.append(bullet)
            self.cool_down_counter = 1
            self.NUM_CLICKED -= 1

    def get_width(self):
        return self.CHACATER_img.get_width() + 290

    def get_height(self):
        return self.CHACATER_img.get_height()

# child classes


class MainCharacter(Character):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.CHACATER_img = MC_imge
        self.bullet_img = BULLET
        self.mask = pygame.mask.from_surface(self.CHACATER_img)
        self.max_health = health

    def move_bullets(self, vel, objs):
        self.cooldown()
        for bullet in self.bullets:
            bullet.move(vel)
            if bullet.off_screen(HEIGHT):
                self.bullets.remove(bullet)
            else:
                for obj in objs:
                    if bullet.collision(obj):
                        objs.remove(obj)
                        self.NUM_KILLED += 1
                        if bullet in self.bullets:
                            self.bullets.remove(bullet)

    def draw(self, window):
        super().draw(window)
        self.healthbar(window)

    def healthbar(self, window):
        pygame.draw.rect(window, (255, 0, 0), (self.x, self.y +
                         self.CHACATER_img.get_height() + 10, self.CHACATER_img.get_width(), 10))
        pygame.draw.rect(window, (0, 255, 0), (self.x, self.y + self.CHACATER_img.get_height() +
                         10, self.CHACATER_img.get_width() * (self.health/self.max_health), 10))


class Enemy(Character):

    ENEMY_MAP = {
        "small": (Invader1_image),
        "medium": (Invader2_image),
        "large": (Invader3_image)
    }

    def __init__(self, x, y, type, health=20):
        super().__init__(x, y, health)
        self.CHACATER_img = self.ENEMY_MAP[type]
        self.mask = pygame.mask.from_surface(self.CHACATER_img)

    def move(self, vel):
        self.y += vel


def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None


def main():
    run = True
    FPS = 60
    bullet_vel = 60
    level = 0
    lives = 5
    player = MainCharacter(375, 850)
    enemies = []
    num_clicked = 20
    player_vel = 6    # 1.2
    enemy_vel = 1  # 0.2
    main_font = pygame.font.SysFont("comicsans", 50)
    lost_font = pygame.font.SysFont("comicsans", 70)
    wave_length = 10
    num_loss = 0
    lost = False
    clock = pygame.time.Clock()

    def redraw_win():
        SCREEN.blit(BACKGROUND, (0, 0))

        lives_show = main_font.render(f"lives: {lives}", 1, (0, 0, 255))
        level_show = main_font.render(f"level: {level}", 1, (255, 0, 0))
        bullets_show = main_font.render(
            f"ammo: {player.NUM_CLICKED}/20", 1, (255, 0, 0))
        kills_show = main_font.render(
            f"kills: {player.NUM_KILLED}", 1, (255, 0, 0))

        SCREEN.blit(lives_show, (10, 600))
        SCREEN.blit(level_show, (10, 800))
        SCREEN.blit(bullets_show, (10, 700))
        SCREEN.blit(kills_show, (590, 750))
        for enemy in enemies:
            enemy.draw(SCREEN)

        player.draw(SCREEN)
        if lost:
            lost_label = lost_font.render("YOU LOST !", 1, (255, 0, 0))
            SCREEN.blit(lost_label, (WIDTH/2 - lost_label.get_width()/2, 350))

        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_win()

        if player.NUM_CLICKED == 0:
            starttime = pygame.time.get_ticks()
            reload = False

            if pygame.time.get_ticks() - 2000 >= 2000:
                reload = True
                print("reload is true")

            if reload == True:
                player.NUM_CLICKED = 20

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
            wave_length += 8

            for i in range(wave_length):
                enemy = Enemy(random.randrange(
                    290, WIDTH-350), random.randrange(-1500, -100), random.choice(["small", "medium", "large"]))
                enemies.append(enemy)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and player.y - player_vel > 0:  # up
            player.y -= player_vel

        if keys[pygame.K_a] and player.x - player_vel > 0:  # left
            player.x -= player_vel

        if keys[pygame.K_d] and player.x + player_vel + player.get_width() < WIDTH:  # right
            player.x += player_vel

        if keys[pygame.K_s] and player.y + player_vel + player.get_height() < HEIGHT:  # down
            player.y += player_vel

        if keys[pygame.K_r]:  # down
            player.NUM_CLICKED = 20

        if keys[pygame.K_SPACE]:       # OR if keys[pygame.K_SPACE]:
            player.shoot()

        for enemy in enemies[:]:
            enemy.move(enemy_vel)
            if collide(enemy, player):
                player.health -= 10
                enemies.remove(enemy)
            elif enemy.y + enemy.get_height() > HEIGHT:
                lives -= 1
                enemies.remove(enemy)

        player.move_bullets(-bullet_vel, enemies)


def controls():
    FPS = 60
    run = True
    main_font = pygame.font.SysFont("comicsans", 50)
    clock = pygame.time.Clock()

    def redraw_win():

        SCREEN.blit(BACKGROUND, (0, 0))

        move_up = main_font.render(f"Button to move up : w", 1, (0, 255, 0))
        move_down = main_font.render(
            f"Button to move down : s", 1, (0, 255, 0))
        move_right = main_font.render(f"Button to move up : d", 1, (0, 255, 0))
        move_left = main_font.render(f"Button to move up : a", 1, (0, 255, 0))
        reload = main_font.render(f"Button to reload : r", 1, (0, 255, 0))
        shoot = main_font.render(
            f"Button to move shoot : SPACE", 1, (0, 255, 0))
        aim = main_font.render(
            f"Place the cursor over the enemy and press the spacebar to shoot", 1, (0, 255, 0))

        SCREEN.blit(move_up, (90, 350))
        SCREEN.blit(move_down, (90, 400))
        SCREEN.blit(move_right, (90, 450))
        SCREEN.blit(move_left, (90, 500))
        SCREEN.blit(reload, (90, 550))
        SCREEN.blit(shoot, (900, 600))
        SCREEN.blit(aim, (0, 800))

        pygame.display.update()
    while run:
        clock.tick(FPS)
        redraw_win()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()


def main_menu():
    title_font = pygame.font.SysFont("impact", 60)
    run = True
    pygame.event.get()
    while run:
        SCREEN.blit(BACKGROUND, (0, 0))
        title_label = title_font.render(
            "Press the mouse to begin", 1, (250, 0, 0))
        controls_label = title_font.render(
            "Press left arrow key to see the controls", 1, (0, 250, 0))
        SCREEN.blit(title_label, (WIDTH/2 - title_label.get_width()/2, 350))
        SCREEN.blit(controls_label, (WIDTH/1.3 - title_label.get_width(), 500))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                main()
            if event.type == pygame.K_r:
                controls()

    pygame.quit()


main_menu()
