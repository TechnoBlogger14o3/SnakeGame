import time
import  pygame , sys
from pygame.locals import  *
import random

pygame.init()

pygame.display.set_caption('SnakeXenzia')

dis_width = 600
dis_height = 500

screen = pygame.display.set_mode((dis_width,dis_height))

icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

img = pygame.image.load('head.jpg')
apple = pygame.image.load('apple.png')
clock = pygame.time.Clock()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,155,0)
block = 10
FPS = 15

direction = "right"

small_font = pygame.font.SysFont("comicsansms", 25)
med_font = pygame.font.SysFont("comicsansms", 40)
large_font = pygame.font.SysFont("comicsansms", 75)

def pause():
    paused = True
    display_msg("Paused", black, -100, "large")

    display_msg("Press C to Continue or Q to Quit", black, 25, "small")
    pygame.display.update()
    clock.tick(5)
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_c:
                    paused = False
        #screen.fill(white)


def winner():
    paused = True

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_c:
                    paused = False
                    gameLoop()

        #screen.fill(white)
        display_msg("Congrats , You are A  Winner ", green, -100, "small")

        display_msg("Press C to Continue or Q to Quit", black, 25, "small")
        pygame.display.update()
        clock.tick(5)

def score(score):
    text = small_font.render("Score : "+str(score),True, black)
    screen.blit(text, [0,0])


def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_c:
                    intro = False
                    gameLoop()
        screen.fill(white)
        display_msg("Welcome To SNAKEXENZIA", green , -100,"medium")
        display_msg("Eat Apples and Score 30 to be a Winner", black, 20, "small")
        display_msg("All The Best", black, 60, "small")
        display_msg("Press C to play , P to Pause and Q to Quit",black, 100,"small")

        pygame.display.update()
        clock.tick(5)


def snake(block,snakelist):

    if direction == "right":
        head = pygame.transform.rotate(img,270)
    if direction == "left":
        head = pygame.transform.rotate(img, 90)
    if direction == "up":
        head = img
    if direction == "down":
        head = pygame.transform.rotate(img, 180)


    screen.blit(head,(snakelist[-1][0],snakelist[-1][1]))
    for XnY in snakelist[:-1]:
        pygame.draw.rect(screen, black, [XnY[0], XnY[1], block, block])

        
def text_objects(text,color,size):
    if size == "small":
        textSurface = small_font.render(text,True,color)
    elif size == "medium":
        textSurface = med_font.render(text,True,color)
    elif size == "large":
        textSurface = large_font.render(text,True,color)
    return textSurface,textSurface.get_rect()


def display_msg(msg,color,y_displace=0,size="small"):
    textSurf,textRect = text_objects(msg,color,size)
    #screen_text = font.render(msg, True, color)
    #screen.blit(screen_text, [dis_width/2,dis_height/2])
    textRect.center = (dis_width/2) , (dis_height/2) + y_displace
    screen.blit(textSurf,textRect)


def gameLoop():
    global direction
    direction = "right"
    gameExit = False
    gameOver = False
    x = dis_width / 2
    y = dis_height / 2
    lead_x = 10
    lead_y = 0
    snakeList = []
    snakelen = 1

    randAppleX = round(random.randrange(0,dis_width - block)/10.0)*10.0
    randAppleY = round(random.randrange(0,dis_height - block)/10.0)*10.0

    while not gameExit:
        if gameOver == True:
            display_msg("Game Over", red, -50, "large")
            display_msg("Press C to Play again or Q to Quit", black, 50, "small")
            pygame.display.update()

        while gameOver == True:
            #screen.fill(white)


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = False
                    gameExit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameOver = False
                        gameExit = True
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOver = False
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x = -block
                    lead_y = 0
                    direction = "left"
                elif event.key == pygame.K_RIGHT:
                    lead_x = block
                    lead_y = 0
                    direction = "right"
                elif event.key == pygame.K_UP:
                    lead_y = -block
                    lead_x = 0
                    direction = "up"
                elif event.key == pygame.K_DOWN:
                    lead_y = block
                    lead_x = 0
                    direction = "down"
                elif event.key == pygame.K_p:
                    pause()
        if x >= dis_width or x < 0 or y < 0 or y >= dis_height:
            gameOver = True


        y += lead_y
        x += lead_x


        screen.fill(white)
        #pygame.draw.rect(screen, red, [randAppleX, randAppleY, block, block])
        screen.blit(apple,(randAppleX,randAppleY))
        snakeHead = []
        snakeHead.append(x)
        snakeHead.append(y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakelen:
            del snakeList[0]

        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True

        snake(block,snakeList)

        score(snakelen-1)

        if(snakelen-1 == 30):
            winner()

        pygame.display.update()

        if x == randAppleX and y == randAppleY:
            randAppleX = round(random.randrange(0,dis_width - block)/10.0)*10.0
            randAppleY = round(random.randrange(0,dis_height - block)/10.0)*10.0
            snakelen += 1

        clock.tick(FPS + snakelen/2)



    pygame.quit()
    quit()
game_intro()
gameLoop()

