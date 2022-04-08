#################################################################################################################################
#                                                       Pixel Gun 2-D                                                           #
#  By: Prithvi Rao                                                                                                              #
#  Teacher: Mr. Millard                                                                                                         #
#  School: American High                                                                                                        #
#  Class: AP Computer Science Principles                                                                                        #
#                                                                                                                               #
#  Description - of game:                                                                                                       #
#       Pixel Gun 2-d is a pixelated third person shooter originated from the ideas of Space invaders. The main                 #
#       character, Rob, is tasked to save the Pixel City from flesh eating zombies. The player can move around the street to    #
#       shoot and eliminate the invaders. He is also given the ability to shoot in all directions to ensure the                 #
#       safety of the citizens of Pixel City. The zombies invade in waves and Rob has to survive long enough to eliminate all   #
#       of them.                                                                                                                #
#                                                                                                                               #
#  Desciption - of classes and functions:                                                                                       #
#                                                                                                                               #
#       Classes:                                                                                                                #
#           --> Bullet                                                                                                          #
#                   The class of Bullet will all the player to shoot the bullet. It will create the image and handles off       #
#                   screen and corner cases. This class will also alow the uset to shoot in any direction with respect to       #
#                   the mouse position.                                                                                         #
#                                                                                                                               #
#           --> Character                                                                                                       #
#                   The class Character is a parent class for both the player and the indvaders. It handles the images for      #
#                   both character classes shooting, moving the bullets, health, collisions, and initial conditions.            #
#                                                                                                                               #
#           --> MainCharacter                                                                                                   #
#                   This class is the Maincharacter (the movable person controlled by the user) and is a child class of         #
#                   the class Character. This class hanldes the bullets and where it goes. It handles bullet corner cases.      #
#                   In addition, it adds a heatlth bar below the character to notify the user the health of their character.    #
#                                                                                                                               #
#           --> Enemy                                                                                                           #
#                   This class is for the invaders that fall from the top of the street and is a child class for the Character  #
#                   class. It handles the images for the invaders and initializes the dictionary for the different sized        #
#                   invaders. It makes them move and handles the collsions.                                                     #
#                                                                                                                               #
#       Functions:                                                                                                              #
#            --> collide                                                                                                        #
#                   This collide function is used to handle the collsions between two object. This includes bullet to           #
#                   character and charcter to character. It is called into the classes.                                         #
#                                                                                                                               #
#            --> main_menu                                                                                                      #
#                   This function is used prior to the actual game function. It acts as a main menu page which allows the       #
#                   user to start his/her game when they are ready to play. This page will prompt you press a mousekey to       #
#                   start the game. It wull also show the use the controls of the game so they know how to play.                #
#                                                                                                                               #
#            --> main                                                                                                           #
#                   This is the main function that is called by the main screen funtion. Its role is to run the actual game.    #
#                   It redraws the screen based on the number of FPS. It also takes the user input and uses it as commands      #
#                   to move the character in game. It is used for kill counts, ammunition, and the HUD items on the screen.     #
#                   Overall this just creats a legible user unterface that the player can use to see what they are doing in     #
#                   game.                                                                                                       #
#                                                                                                                               #
# LINKS:                                                                                                                        #
#                                                                                                                               #
#  # https: // www.pinterest.com/pin/160088961739053448/  # background                                                          #
#                                                                                                                               #
#  # https://opengameart.org/content/animated-top-down-zombie  # link to invaders                                               #
#                                                                                                                               #
#  # https://opengameart.org/content/animated-top-down-survivor-player    #link to main character                               #
#                                                                                                                               #
#  # https://github.com/nealholt/python_programming_curricula/blob/master/CS1/0550_galaga/pygame_galaga2_shoot_any_direction.py #
#     # help for multi directional shooting                                                                                     #
#                                                                                                                               #
#  # https://www.youtube.com/watch?v=3DeW-7vbc50 # more help for multi directional shooting                                     #
#                                                                                                                               #
#  # https://www.youtube.com/watch?v=Q-__8Xw9KTM # over all structure and I got some help for some of the game algorithms       #
#                                                                                                                               #
#################################################################################################################################


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

pygame.display.set_caption(
    " PIXEL GUN 2-D  - Prithvi Rao")


# PARENT CLASSES

# takes the the mouse x and y positions and uses them to load the bullet image on the screen. It moves the bullet with the given
# bullet vel.
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


# This is the parent class for the maincharacter and the zombie. It has all the underlying features of both like cooldowns,
# collsions, and position. It inputs information like x and y position and health and passes it to the child classes.
class Character:

    COOLDOWN = 15
    NUM_CLICKED = 20
    NUM_KILLED = 0

    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.CHACATER_img = None
        self.bullet_img = None
        self.bullets = []
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
                self.bullets.remove(bullet)

    def cooldown(self):
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1

    def shoot(self):
        if self.cool_down_counter == 0:
            x, y = pygame.mouse.get_pos()
            bullet = Bullet(self.x, self.y, x, y, 40, self.bullet_img)
            self.bullets.append(bullet)
            self.cool_down_counter = 1
            self.NUM_CLICKED -= 1

    def get_width(self):
        return self.CHACATER_img.get_width() + 290

    def get_height(self):
        return self.CHACATER_img.get_height()


# CHILD CLASSES

# This is for the main character. It takes in the initial starting position of the person and displays it on the screen.
# He gives the charactr a health and looks for collisions. Also draws the healthbar. It inputs the information from the parent
# class and uses them to identify the maincharacter.
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

# This class takes info from the parent class and adds a dictionary to allow for the mutlple sized zombies to spawn at random.
# It allow spawns them in at diffent locations within a perameter. It takes these paremeters and displays the enemy onto the
# screen


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

# This function takes two objects and checks if they have an overlap. It them returns true or false based off the result.


def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None

# This function is used prior to the actual game function. It takes the mousekey press as a form of input and uses that to excicute
# the actual game function.


def main_menu():
    title_font = pygame.font.SysFont("impact", 75)
    run = True
    main_font = pygame.font.SysFont("comicsans", 25)

    pygame.event.get()
    while run:
        SCREEN.blit(BACKGROUND, (0, 0))
        title_label = title_font.render(
            "Press the mouse to begin", 1, (250, 0, 0))

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
        SCREEN.blit(aim, (30, 600))
        SCREEN.blit(title_label, (WIDTH/2 - title_label.get_width()/2, 100))

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                main()

    pygame.quit()


# This is the main function that is called by the main screen funtion. It allows program to actually run into a window. It takes the
# user inputs and uses them to exicute the code to move the charcter in game.
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


# call the main function so that it actually runs
main_menu()
