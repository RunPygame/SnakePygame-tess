# https://python.bakyeono.net/chapter-12-1.html
'''
Start to create a snake game!
# https://playsnake.org

pip install pygame

## colors
RED = 255, 0, 0        # 적색:   적 255, 녹   0, 청   0
GREEN = 0, 255, 0      # 녹색:   적   0, 녹 255, 청   0
BLUE = 0, 0, 255       # 청색:   적   0, 녹   0, 청 255
PURPLE = 127, 0, 127   # 보라색: 적 127, 녹   0, 청 127
BLACK = 0, 0, 0        # 검은색: 적   0, 녹   0, 청   0
GRAY = 127, 127, 127   # 회색:   적 127, 녹 127, 청 127
WHITE = 255, 255, 255  # 하얀색: 적 255, 녹 255, 청 255


'''
import pygame              # ❶ 파이게임 모듈 임포트하기
import time
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500

pygame.init()

# 인자로 화면 객체를 반환해준다.
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

rect = pygame.Rect((0,0), (40, 40))
# graw color
# RED = 255, 0, 0
pygame.draw.rect(screen, (255, 0, 0), rect, 1)
pygame.display.update() # 화면새로고침

time.sleep(15)