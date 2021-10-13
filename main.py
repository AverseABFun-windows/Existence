import pygame
from pygame import *
from pygame.locals import *
class Event:
    def __init__(self,ctr):
        self.ctr=ctr
    def run(self,data):
        exec(self.ctr,{"dataa":data})
class Events:
    def __init__(self,data):
        self.events=[]
        self.data=str(data)
    def register(self,event:Event):
        self.events.append(event)
    def loop(self):
        for i in self.events:
            i.run(self.data)
mousee=new Events("mouse")
pygame.init()
screen = pygame.display.set_mode((500, 450))
pygame.display.set_caption('Existence')
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((55,55,255))
def ground(color):
    draw.rect(background,color,Rect(0,background.get_height()-195,background.get_width(),background.get_height()/10))
def clouds(cloudpos):
    draw.circle(background,(255,255,255),(cloudpos[0]+5,cloudpos[1]),20)
    draw.circle(background,(255,255,255),(cloudpos[0]+20,cloudpos[1]-5),20)
    draw.circle(background,(255,255,255),(cloudpos[0]+40,cloudpos[1]-10),20)
    draw.circle(background,(255,255,255),(cloudpos[0]+60,cloudpos[1]-5),20)
    draw.circle(background,(255,255,255),(cloudpos[0]+75,cloudpos[1]),20)
    draw.rect(background,(255,255,255),Rect(cloudpos[0],cloudpos[1],80,20))
def button(text,location,color,tcolor,size):
    draw.rect(background,color,Rect(location[0],location[1],size[0],size[1]))
    tfont=pygame.font.SysFont("dejavuserif",20)
    screen.blit(tfont.render(text,True,tcolor),location)
while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
        
        ground((0,255,0))
        tfont=pygame.font.SysFont("dejavuserif",20)
        screen.blit(tfont.render("Existence",True,(255,255,255)),(50,10))
        screen.blit(background, (0, 0))
        pygame.display.flip()
        clouds((380,30))
        clouds((300,90))
        clouds((50,30))