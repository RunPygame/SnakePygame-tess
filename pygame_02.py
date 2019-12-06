import pygame # 1.

# t = pygame.init()
# print(t) # (6,0) 제대로 돌아감 확인
# 한글 깨지면 한글 인코딩할 것

pygame.init() # 2.

screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption('pygame')
finish = False
# colorBlue = (0, 128, 255)
colorBlue = True
x = 30
y = 30
clock = pygame.time.Clock()

# gameloop란?
# handle events -> update game state -> draw screen -> 다시 처음으로
while not finish:

    for event in pygame.event.get(): # 발생한 이벤트 리스트를 가져온다.
        if event.type == pygame.QUIT: # 끝났으면,
            finish = True

    # 스페이스바를 누르면 다음과 같이 바뀐다.
    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        colorBlue = not colorBlue # 이런식으로 쓰는건 처음봤다..! if 두번 안써도된다.. 대박,..,.
    # elif event.type == pygame.MOUSEBUTTONDOWN and colorBlue == False:
    #     colorBlue = True
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: y -= 3
    if pressed[pygame.K_DOWN]: y += 3
    if pressed[pygame.K_LEFT]: x -= 3
    if pressed[pygame.K_RIGHT]: x += 3
    # 괄호안에 넣도록해서 늘어나지 않도록 조절, 움직일때 기존 것이 지워진다.
    screen.fill((0, 0, 0))

    if colorBlue: color = (0, 128, 255)
    else: color = (255, 255, 255) # white로 change


    pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60)) # (어디에? (R, G, B) 위치y, 위치x, 가로크기, 세로크기)
    pygame.display.flip() # update랑 동일
    # 너무 빠르게 움직이기 때문에 프레임을 지정해줘야 한다. 좀더 자연스러운 움직임 가능
    clock.tick(60)




