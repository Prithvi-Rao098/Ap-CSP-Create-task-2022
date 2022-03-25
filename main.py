import pygame
import os
pygame.font.init()

# initilizing the SCREENdow screen
WIDTH, HEIGHT = 1000, 900
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
BACKGROUND = (234, 212, 252)


# ADD NAME
pygame.display.set_caption(
    " !!!@@@@ ----  ENTER NAME LATER  ----@@@@!!!  - Prithvi Rao")


# initializing the characters and the images
run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
main_menu()
