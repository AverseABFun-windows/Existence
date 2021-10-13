import pygame
from pygame import *
from pygame.locals import * 
pygame.init()
screen = pygame.display.set_mode((500, 450))
pygame.display.set_caption('Existence')
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((55,55,255))
def ground(color):
    draw.rect(background,color,Rect(0,background.get_height()-200,background.get_width(),background.get_height()/50))
def clouds(cloudpos):
    draw.circle(background,(255,255,255),(cloudpos[0]+5,cloudpos[1]),20)
    draw.circle(background,(255,255,255),(cloudpos[0]+20,cloudpos[1]-5),20)
    draw.circle(background,(255,255,255),(cloudpos[0]+40,cloudpos[1]-10),20)
    draw.circle(background,(255,255,255),(cloudpos[0]+60,cloudpos[1]-5),20)
    draw.circle(background,(255,255,255),(cloudpos[0]+75,cloudpos[1]),20)
    draw.rect(background,(255,255,255),Rect(cloudpos[0],cloudpos[1],80,20))
while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
        ground((0,255,0))
        screen.blit(background, (0, 0))
        pygame.display.flip()
        clouds((190,30))
        clouds((250,90))
        clouds((30,40))
