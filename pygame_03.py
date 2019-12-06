import pygame
pygame.init()

# mp3
pygame.mixer.music.load('christmas.mp3')
pygame.mixer.music.play(-1) # 0: 한번 -1: 무한

# 항상 값을 변수로 지정하는 습관을 들여야한다.
displayWidth = 1000
displayHeight = 800

screen = pygame.display.set_mode((displayWidth, displayHeight))

myimg = pygame.image.load('myimg.jpg')

def myimgMethod(x, y):
    # 그리기 뭐를? 어디에?
    screen.blit(myimg, (x, y))

x = (displayWidth * 0.2)
y = (displayHeight * 0.2)

finished = False
while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
    # 그냥 그려주면 배경색때문에 문제가 있어서 배경색을 지정해줘야 한다.
    screen.fill((255, 255, 200))

    # 함수랑 변수랑 이름을 중복하면 안된다.
    myimgMethod(x, y)
    pygame.display.flip()

pygame.quit()
quit()