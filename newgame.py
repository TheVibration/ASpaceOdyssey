import sys, pygame
import time
import random

pygame.init()

icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

# set width and height variables
screen_width = 800
screen_height = 600


# color RGB
black = (0,0,0)
white = (255,255,255)
blue = (0,0, 255)

# open window on screen
screen = pygame.display.set_mode([screen_width, screen_height])

# set window caption
pygame.display.set_caption("Space Odyssey")

# clock
clock = pygame.time.Clock()

# load images
alienship = pygame.image.load("alienship.png")
bg = pygame.image.load("bg.jpg")
ship_width = 63

# keep score
def objects_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: " + str(count), True, blue)
    screen.blit(text,(0,0))


# moving objects
def objects(objectx, objecty, objectw, objecth, color):
    pygame.draw.rect(screen, color, [objectx, objecty, objectw, objecth])

# blit alienship onto display surface
def background(x,y):
    screen.blit(bg,(x,y))

# blit alienship onto display surface
def ship(x,y):
    screen.blit(alienship,(x,y))

# pos of background
a = 0
b = 0

def text_objects(msg, font):
    text_surface = font.render(msg, True, white)
    return text_surface, text_surface.get_rect()


def message_display(msg):
    font = pygame.font.Font("freesansbold.ttf", 90)
    TextSurf, TextRect = text_objects(msg,font)
    TextRect.center = ((screen_width/2), (screen_height/2))
    screen.blit(TextSurf, TextRect)

    pygame.display.flip()

    time.sleep(4)

    game()

def crash():
    message_display("Crashed")

def game():
    
    # pos of spaceship
    x = (screen_width * 0.45)
    y = (screen_height * 0.75)
    
    # pos of car default
    x1 = 0
    x2 = 0
    #y1 = 0
    #y2 = 0

    object_startx = random.randrange(0, screen_width)
    object_starty = -600
    object_speed = 7
    object_width = 100
    object_height = 100

    dodged = 0

    exit_game = False

    # crash is set to False, therefore the while
    # loop will continue to repeat untl crash is True
    while not exit_game:

    #for event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1 = -20
                if event.key == pygame.K_RIGHT:
                    x2 = 20
#                elif event.key == pygame.K_DOWN:
#                    y1 = -5
#                elif event.key == pygame.K_UP:
#                    y2 = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    x1 = 0
                if event.key == pygame.K_LEFT:
                    x2 = 0
#                elif event.key == pygame.K_DOWN:
#                   y1 = 0
#                elif event.key == pygame.K_UP:
#                    y2 = 0
        
            x += x1 + x2

        background(a,b)

        objects(object_startx, object_starty, object_width, object_height, black)
        object_starty += object_speed
        ship(x,y)
        objects_dodged(dodged)
        
        if x > screen_width-ship_width or x < 0:
            crash()

        if object_starty > screen_height:
            object_starty = 0 - object_height
            object_startx = random.randrange(0, screen_width)
            dodged = dodged + 1

            if dodged % 5 == 0:
                object_speed += 1

        if y < object_starty+object_height:

            if x > object_startx and x < object_startx + object_width or x+ship_width > object_startx and x + ship_width < object_startx +object_width:
                crash()


        pygame.display.flip()
        clock.tick(60)

game()
pygame.quit()


