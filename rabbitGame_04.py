# http://raywenderlich.com/
# https://www.raywenderlich.com/2795-beginning-game-programming-for-teens-with-python
'''Rabbit Game'''

# 1 - Import library
import pygame
from pygame.locals import *
import math
import random


# 2 - Initialize the game
pygame.init()
width, height = 640, 480

screen=pygame.display.set_mode((width, height))
# 속도
FPS = 60
fpsClock = pygame.time.Clock()


# bunny move 키 입력 체크
# 위치를 실시간으로 업데이트 해야한다
keys = [False, False, False, False]
# 플레이어 위치(bunny) 가장 처음 위치
playerpos = [100,100]


acc = [0,0] # 토끼가 쏘는 화살, 변수 초기화 적을 맞춘 횟수와 발사횟수
arrows = [] # 화살 각도
badtimer = 100 # 적
badtimer1 = 0
badguys = [[640,100]] # 리스트
healthvalue = 194 # 적들의 피 -> 0되면 게임오버
pygame.mixer.init()




# 3 - Load images
player = pygame.image.load("resources/images/dude.png")

# 배경
grass = pygame.image.load("resources/images/grass.png")
castle = pygame.image.load("resources/images/castle.png")

# 화살 이미지
arrow = pygame.image.load("resources/images/bullet.png")

# 적 이미지
badguyimg1 = pygame.image.load("resources/images/badguy.png")
badguyimg=badguyimg1

healthbar = pygame.image.load("resources/images/healthbar.png")
health = pygame.image.load("resources/images/health.png")
gameover = pygame.image.load("resources/images/gameover.png")
youwin = pygame.image.load("resources/images/youwin.png")

# 3.1 - Load audio
hit = pygame.mixer.Sound("resources/audio/explode.wav")
enemy = pygame.mixer.Sound("resources/audio/enemy.wav")
shoot = pygame.mixer.Sound("resources/audio/shoot.wav")
hit.set_volume(0.05)
enemy.set_volume(0.05)
shoot.set_volume(0.05)
pygame.mixer.music.load('resources/audio/moonlight.wav')
pygame.mixer.music.play(-1, 0.0)
pygame.mixer.music.set_volume(0.25)



# 4 - keep looping through
running = 1
exitcode = 0
while running: # 게임 메인 루프
    badtimer-=1 # 매번 프레임마다 1씩 감소시킨다.
    # 5 - clear the screen before drawing it again
    screen.fill(0)
    # 6 - draw the screen elements
    # 배경그리기 풀
    # 잔디는 pixel이 있는데, 픽셀 때문에 나누기를 한 것
    # 정수로 만들어 6으로 만들게 된다.
    # range(0, 7) ->  0 1 2 3 4 5 6    640/100+1
    for x in range(int(width/grass.get_width()+1)):
        # range(0, 5) -> 0 1 2 3 4     480/100+1
        for y in range(int(height/grass.get_height()+1)):
            screen.blit(grass,(x*100,y*100))
    # 배경그리기 캐슬
    screen.blit(castle,(0,30))
    screen.blit(castle,(0,135))
    screen.blit(castle,(0,240))
    screen.blit(castle,(0,345))

    # 플레이어를 그리기
    screen.blit(player, playerpos)

    # 6.1 - Set player position and rotation
    # 버니 회전
    position = pygame.mouse.get_pos()
    angle = math.atan2(position[1]-(playerpos[1]+32),position[0]-(playerpos[0]+26))
    playerrot = pygame.transform.rotate(player, 360-angle*57.29)
    playerpos1 = (playerpos[0]-playerrot.get_rect().width/2, playerpos[1]-playerrot.get_rect().height/2)
    screen.blit(playerrot, playerpos1)


    # 6.2 - Draw arrows
    # 화살그리기
    for bullet in arrows:
        index=0
        velx=math.cos(bullet[0])*10
        vely=math.sin(bullet[0])*10
        bullet[1]+=velx
        bullet[2]+=vely
        # 화면 밖으로 화살이 나가면 화살을 꺼내준다.
        if bullet[1]<-64 or bullet[1]>640 or bullet[2]<-64 or bullet[2]>480:
            arrows.pop(index) # 이렇게 인덱스 값에 해당하는 화살을 제거
        index+=1

        for projectile in arrows:
            arrow1 = pygame.transform.rotate(arrow, 360-projectile[0]*57.29)
            screen.blit(arrow1, (projectile[1], projectile[2]))

        # 6.3 - Draw badgers
        # 적 생성
        if badtimer == 0: # 0이면 적이 생성된다.
            # 생성 좌표값 추가 50-430사이의 임의값을 가진다.
            badguys.append([640, random.randint(50, 430)])
            # 타이머 값을 변화시킨다. 최저값 지정
            badtimer = 100 - (badtimer1 * 2)
            if badtimer1 >= 35:
                badtimer1 = 35
            else:
                badtimer1 += 5

        index = 0
        for badguy in badguys:
            if badguy[0] < -64:
                badguys.pop(index)
            badguy[0] -= 7

            # 6.3.1 - Attack castle
            # 성 공격
            badrect = pygame.Rect(badguyimg.get_rect())
            badrect.top = badguy[1]
            badrect.left = badguy[0]
            if badrect.left < 64:
                hit.play() ##
                healthvalue -= random.randint(5, 20)
                badguys.pop(index)

            # 6.3.2 - Check for collisions
            # 적이 없어지는 관계
            # 충돌체크
            # 적을 해치우는 방법은 rect를 이용해서 상하좌우 정보를 가져와서 진행
            index1 = 0
            for bullet in arrows:
                bullrect = pygame.Rect(arrow.get_rect())
                bullrect.left = bullet[1]
                bullrect.top = bullet[2]
                if badrect.colliderect(bullrect):
                    enemy.play()
                    acc[0] += 1
                    badguys.pop(index)
                    arrows.pop(index1)
                index1 += 1

            # 6.3.3 - Next bad guy
            index += 1
        for badguy in badguys:
            screen.blit(badguyimg, badguy)

    # 6.4 - Draw clock
    font = pygame.font.Font(None, 24)
    survivedtext = font.render(str((90000-pygame.time.get_ticks())/60000)+":"+str((90000-pygame.time.get_ticks())/1000%60).zfill(2), True, (0,0,0))
    textRect = survivedtext.get_rect()
    textRect.topright=[635,5]
    screen.blit(survivedtext, textRect)

    # 6.5 - Draw health bar
    screen.blit(healthbar, (5,5))
    for health1 in range(healthvalue):
        screen.blit(health, (health1+8,8))


    # 7 - update the screen
    pygame.display.flip()
    # 속도
    fpsClock.tick(FPS)

    # 8 - loop through the events
    for event in pygame.event.get():
        # check if the event is the X button
        if event.type == pygame.QUIT:
            # if it is quit the game
            pygame.quit()
            exit(0)

        # 키를 누를때 -> True로 바꾼다
        if event.type == pygame.KEYDOWN:
            if event.key == K_w:
                keys[0] = True
            elif event.key == K_a:
                keys[1] = True
            elif event.key == K_s:
                keys[2] = True
            elif event.key == K_d:
                keys[3] = True

        # 키를 뗄때 -> False로 바꾼다
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                keys[0] = False
            elif event.key == pygame.K_a:
                keys[1] = False
            elif event.key == pygame.K_s:
                keys[2] = False
            elif event.key == pygame.K_d:
                keys[3] = False
        # 마우스를 클릭하면,
        if event.type == pygame.MOUSEBUTTONDOWN:
            shoot.play()
            position = pygame.mouse.get_pos()
            # 화살발사횟수 증가
            acc[1] += 1
            arrows.append([math.atan2(position[1] - (playerpos1[1] + 32), position[0] - (playerpos1[0] + 26)),
                           playerpos1[0] + 32, playerpos1[1] + 32])

    # 9 - Move player 플레이어를 움직이게 하는 것
    # 키가 만약 True라면,
    if keys[0]:
        playerpos[1] -= 5
    elif keys[2]:
        playerpos[1] += 5
    if keys[1]:
        playerpos[0] -= 5
    elif keys[3]:
        playerpos[0] += 5


# 10 - Win/Lose check
if pygame.time.get_ticks() >= 90000:
    running = 0
    exitcode = 1
if healthvalue <= 0:
    running = 0
    exitcode = 0
if acc[1] != 0:
    accuracy = acc[0] * 1.0 / acc[1] * 100
else:
    accuracy = 0

# 11 - Win/lose display
if exitcode == 0:
    pygame.font.init()
    font = pygame.font.Font(None, 24)
    text = font.render("Accuracy: " + str(accuracy) + "%", True, (255, 0, 0))
    textRect = text.get_rect()
    textRect.centerx = screen.get_rect().centerx
    textRect.centery = screen.get_rect().centery + 24
    screen.blit(gameover, (0, 0))
    screen.blit(text, textRect)
else:
    pygame.font.init()
    font = pygame.font.Font(None, 24)
    text = font.render("Accuracy: " + str(accuracy) + "%", True, (0, 255, 0))
    textRect = text.get_rect()
    textRect.centerx = screen.get_rect().centerx
    textRect.centery = screen.get_rect().centery + 24
    screen.blit(youwin, (0, 0))
    screen.blit(text, textRect)
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
    pygame.display.flip()



