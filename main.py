import pygame
from pygame import *
from pygame.locals import *
def add(x,y):
    return x+y
pygame.init()
screen = pygame.display.set_mode((500, 450))
pygame.display.set_caption('Existence')
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((55,55,255))
def ground(color):
    draw.rect(background,color,Rect(0,background.get_height()-200,background.get_width(),background.get_height()/50))
def clouds(cloudpos):
    for i in range(3):
        draw.circle(background,(255,255,255),(add(cloudpos[0],i*20),cloudpos[1]),20)
while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
        ground((0,255,0))
        screen.blit(background, (0, 0))
        pygame.display.flip()
        clouds((190,40))
        clouds((250,90))
        clouds((30,30))
        clouds((120,70))