import pygame
import time
import math
import random
from random import *
from pygame.locals import *
from datetime import datetime
from datetime import timedelta

FPS = 30
fpsClock = pygame.time.Clock()


def draw_block(screen, color, position, rect):
    block = pygame.Rect((position[1], position[0]), (rect[1], rect[0]))
    pygame.draw.rect(screen, color, block)

def draw_img(screen, img, pos1, pos2):
    screen.blit(img, [pos2, pos1])

def draw_background(screen):
    background = pygame.Rect((0, 0), (width, height))
    pygame.draw.rect(screen, white, background)


def collision(y1, x1, size1, y2, x2, size2):
    if y1 < y2 < y1 + size1 and x1 < x2 < x1 + size1:
        return True
    if y1 < y2 < y1 + size1 and x1 < x2 + size2 < x1 + size1:
        return True
    if y1 < y2 + size2 < y1 + size1 and x1 < x2 < x1 + size1:
        return True
    if y1 < y2 + size2 < y1 + size1 and x1 < x2 + size2 < x1 + size1:
        return True
    if y2 < y1 < y2 + size2 and x2 < x1 < x2 + size2:
        return True
    if y2 < y1 < y2 + size2 and x2 < x1 + size1 < x2 + size2:
        return True
    if y2 < y1 + size1 < y2 + size2 and x2 < x1 < x2 + size2:
        return True
    if y2 < y1 + size1 < y2 + size2 and x2 < x1 + size1 < x2 + size2:
        return True


# pygame init --------------------------------------------------------
# screen, 사용하는 색 저장
pygame.init()
width, height = 1200, 800
screen = pygame.display.set_mode((width, height))

red = 255, 0, 0
green = 0, 255, 0
blue = 0, 0, 255
black = 0, 0, 0
white = 255, 255, 255
gray = 127, 127, 127

# img,

# print(playerImg)

# init end -----------------------------------------------------------

# class --------------------------------------------------------------

class Player:
    playerImg = pygame.image.load("resources/images/dude.png")
    # playerpos = [400, 250]
    color = green
    size = 20
    rspd = 0
    cspd = 0
    palyer_spd = 10

    def __init__(self):
        # 마우스가 올라간 위치에서 시작한다.
        # 바니 제대로 움직이게하고, 총 쏘게 할 것
        # self.position = pygame.mouse.get_pos()
        self.position = [400, 250]

        # self.position = list(self.position)
        # # print('--', self.position, self.playerpos)
        # self.angle = math.atan2(self.position[1] - (self.playerpos[1] + 32), self.position[0] - (self.playerpos[0] + 26))
        # self.playerrot = pygame.transform.rotate(self.playerImg, 360 - self.angle * 57.29)
        # self.playerpos1 = (self.playerpos[0] - self.playerrot.get_rect().width / 2, self.playerpos[1] - self.playerrot.get_rect().height / 2)


    def draw(self, screen):
        draw_img(screen, self.playerImg, self.position[0], self.position[1])
        draw_block(screen, self.color, self.position, (self.size, self.size))


class Castle:
    color = black
    def __init__(self):
        self.hp = 100

    def draw(self, screen):
        draw_block(screen, self.color, (100, 0), (700, 200))


class Enermies:
    color = red

    def __init__(self):
        self.spd = 1
        self.size = 30
        self.delay = 50
        self.stats = []  # stats = [hp, y, x, delay]

    def draw(self, screen):
        for hp, y, x, delay in self.stats:
            draw_block(screen, self.color, (y, x), (self.size, self.size))


class Shots:
    color = gray

    def __init__(self):
        self.spd = 2
        self.size = 10
        self.dmg = 10
        self.stats = []  # damage, pal, y, x

    def draw(self, screen):
        for damage, pal, y, x in self.stats:
            draw_block(screen, self.color, (y, x), (self.size, self.size))


class Shield:
    color = blue

    def __init__(self):
        self.size = 31
        self.visible = 0
        self.position = [0, 0]

    def draw(self, screen):
        if self.visible == 1:
            draw_block(screen, self.color, (self.position[0], self.position[1]), (self.size, 5))


class StatBar:
    color = gray

    def __init__(self):
        self.hpbar = 50
        self.damaged = 0

    def draw(self, screen):
        draw_block(screen, self.color, (0, 0), (100, 1200))
        draw_block(screen, green, (40, 50), (20, self.hpbar * 4))
        draw_block(screen, red, (40, 50 + self.hpbar * 4), (20, self.damaged * 4))


class GameBoard:
    width = 1200
    height = 800

    def __init__(self):
        self.player = Player()
        self.castle = Castle()
        self.enms = Enermies()
        self.shots = Shots()
        self.sb = StatBar()
        self.sd = Shield()

    def draw(self, screen):
        self.player.draw(screen)
        self.castle.draw(screen)
        self.enms.draw(screen)
        self.shots.draw(screen)
        self.sb.draw(screen)
        self.sd.draw(screen)


# class end -----------------------------------------------------------

bd = GameBoard()
cur_enermies = 0
while True:
    # 적 생성
    if random() < 0.002:
        if cur_enermies < 5:
            bd.enms.stats.append([10, random() * bd.height - bd.enms.size, bd.width - 5, 0])
            cur_enermies += 1
    print(bd.sd.visible)
    print(bd.sd.position)
    if bd.sd.visible:
        draw_block(screen, blue, bd.sd.position, (30, 5))
    # 방패 위치 갱신
    bd.sd.position = [bd.player.position[0] - 5, bd.player.position[1] + 25]
    # event 처리 ----------------------------------------------------
    events = pygame.event.get()
    for event in events:
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT or event.key == ord('a'):
                bd.player.cspd = -bd.player.palyer_spd
            if event.key == K_RIGHT or event.key == ord('d'):
                bd.player.cspd = bd.player.palyer_spd
            if event.key == K_UP or event.key == ord('w'):
                bd.player.rspd = -bd.player.palyer_spd
            if event.key == K_DOWN or event.key == ord('s'):
                bd.player.rspd = bd.player.palyer_spd
            if event.key == event.key == ord('e'):
                bd.sd.visible = 1
        if event.type == pygame.KEYUP:
            if event.key == K_LEFT or event.key == ord('a') or event.key == K_RIGHT or event.key == ord('d'):
                bd.player.cspd = 0
            if event.key == K_UP or event.key == ord('w') or event.key == K_DOWN or event.key == ord('s'):
                bd.player.rspd = 0
            if event.key == event.key == ord('e'):
                bd.sd.visible = 0
        if event.type == MOUSEMOTION:
            position = pygame.mouse.get_pos()  # get_pos = x,y 순서대로 나온다
        if event.type == MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()
            bd.shots.stats.append([bd.shots.dmg, math.atan2(position[1] + bd.player.size // 2 - bd.player.position[0],
                                                            position[0] + bd.player.size // 2 - bd.player.position[1]),
                                   bd.player.position[0], bd.player.position[1]])

    # event 처리 end ------------------------------------------------
    # print(bd.player.rspd, bd.player.cspd)
    # player 이동
    if bd.player.rspd > 0:
        if bd.player.position[0] + bd.player.size < bd.height:
            bd.player.position[0] += bd.player.rspd
    elif bd.player.rspd < 0:
        if bd.player.position[0] > 0:
            bd.player.position[0] += bd.player.rspd
    if bd.player.cspd > 0:
        if bd.player.position[1] + bd.player.size < bd.width:
            bd.player.position[1] += bd.player.cspd
    elif bd.player.cspd < 0:
        if bd.player.position[1] > 200:
            bd.player.position[1] += bd.player.cspd

    # enermy 이동
    for i in range(len(bd.enms.stats)):
        hp, y, x, delay = bd.enms.stats.pop(0)
        if hp < 1 or y < 100 or y > 800:
            cur_enermies -= 1
            continue
        else:
            if x > 200:
                bd.enms.stats.append([hp, y, x - bd.enms.spd, delay])
            else:
                if delay == bd.enms.delay:
                    if bd.sb.hpbar > 0:
                        bd.sb.hpbar -= 1
                        bd.sb.damaged += 1
                    else:
                        print('game over')
                    delay = 0
                bd.enms.stats.append([hp, y, x, delay + 1])

    # shots 이동 및 명중여부
    for i in range(len(bd.shots.stats)):
        # print(bd.shots.stats)
        dmg, pal, y1, x1 = bd.shots.stats.pop(0)
        size1 = bd.shots.size
        hit = 0
        for enm in bd.enms.stats:
            hp, y2, x2, delay = enm
            size2 = bd.enms.size
            if hit == 0:
                if collision(y1, x1, size1, y2, x2, size2):
                    enm[0] -= dmg
                    hit = 1
        if hit == 0:
            if 0 <= y1 + math.cos(pal) * bd.shots.spd < bd.height and 200 <= x1 + math.sin(
                    pal) * bd.shots.spd < bd.width:
                bd.shots.stats.append(
                    [dmg, pal, y1 + math.sin(pal) * bd.shots.spd, x1 + math.cos(pal) * bd.shots.spd])  # 삼각함수 들어가야됨

    # if bd.shots.stats:
    #     print(bd.shots.stats)
    #     print(math.degrees(bd.shots.stats[0][1]))

    draw_background(screen)
    bd.draw(screen)
    pygame.display.update()
