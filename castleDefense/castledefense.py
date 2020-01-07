import pygame, os
# import player
import math
from pygame.locals import *


grass = pygame.image.load("resources/images/grass.png")
player = pygame.image.load("resources/images/dude.png")
castle = pygame.image.load("resources/images/castle.png")
arrow = pygame.image.load("resources/images/bullet.png")
# print(grass)
# class Player:
#     global screen
#     def __init__(self):
#         self.hp = 100
#         self.playerImg = pygame.image.load("resources/images/dude.png")
#         self.playerpos = [100, 100]
#
#
#     def mouseMove(self, playerpos, playerImg, screen):
#         position = pygame.mouse.get_pos()
#         angle = math.atan2(position[1] - (playerpos[1] + 32), position[0] - (playerpos[0] + 26))
#         playerrot = pygame.transform.rotate(playerImg, 360 - angle * 57.29)
#         playerpos1 = (playerpos[0] - playerrot.get_rect().width / 2, playerpos[1] - playerrot.get_rect().height / 2)
#         screen.blit(playerrot, playerpos1)
#



colorBlue = (0, 128, 255)

def main():
    print('loading...')
    pygame.init()

    width, height = 640, 480
    screen = pygame.display.set_mode((width, height))

    pygame.mixer.init()
    playerpos = [100, 100]



    arrows = []
    num_arrows = 100

    running = 1
    while running:
        screen.fill(0)

        for x in range(int(width / grass.get_width() + 1)):
            for y in range(int(height / grass.get_height() + 1)):
                screen.blit(grass, (x * 100, y * 100))

        pygame.draw.rect(screen, colorBlue, pygame.Rect(30, 30, 60, 420))

        # player = Player()
        # player.mouseMove()

        position = pygame.mouse.get_pos()
        angle = math.atan2(position[1] - (playerpos[1] + 32), position[0] - (playerpos[0] + 26))
        playerrot = pygame.transform.rotate(player, 360 - angle * 57.29)
        playerpos1 = (playerpos[0] - playerrot.get_rect().width / 2, playerpos[1] - playerrot.get_rect().height / 2)
        screen.blit(playerrot, playerpos1)



        # print(arrows)
        # for bullet in list(arrows):
        #     print(arrows)
        #     velx = math.cos(bullet[0]) * 10
        #     vely = math.sin(bullet[0]) * 10
        #     bullet[1] += velx
        #     bullet[2] += vely
        #     if bullet[1] < -64 or bullet[1] > 640 or bullet[2] < -64 or bullet[2] > 480:
        #         arrows.remove(bullet)
        #         if num_arrows <= 0:
        #             running = 0
        # for projectile in arrows:
        #     print(arrows)
        #     arrow1 = pygame.transform.rotate(arrow, 360 - projectile[0] * 57.29)
        #     screen.blit(arrow1, (projectile[1], projectile[2]))
        #
        #
        #
        # arrowstext = font.render("Remaining arrows: " + str(num_arrows), True, (0, 0, 0))
        # arrowsTextRect = arrowstext.get_rect()
        # arrowsTextRect.topright = [635, 20]
        # screen.blit(arrowstext, arrowsTextRect)


        pygame.display.flip() # 반드시 필요하다



        for event in pygame.event.get(): # 게임 종료
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)





main()