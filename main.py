########################################
#              Prithvi Rao             #
#                                      #
#         --- enter name ---       #
#                                      #
#   period: 6                          #
#   Description:

import pygame
import main_menu_animation as MA
pygame.font.init()

# initilizing the SCREENdow screen
WIDTH, HEIGHT = 1000,900
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
BACKGROUND = (234, 212, 252)
pygame.display.set_caption("Space Invader - Prithvi Rao")

run = True

while run:
    for event in pygame.event.get():
        title_label = title_font.render("Press the mouse to begin", 1, (250,0,0))
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
main_menu()