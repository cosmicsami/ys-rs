import pygame,pyautogui,time
from pygame.locals import *
pygame.font.init()
pygame.mixer.init()
WIDTH,HEIGHT=pyautogui.size()
space=pygame.display.set_mode((WIDTH,HEIGHT))
bg=pygame.transform.scale(pygame.image.load("space 2.png"),(WIDTH,HEIGHT))
sw,sh=WIDTH//40,HEIGHT//25
ys=pygame.transform.rotate(pygame.transform.scale(pygame.image.load("1.png"),(sw,sh)),90)
rs=pygame.transform.rotate(pygame.transform.scale(pygame.image.load("2.png"),(sw,sh)),-90)


while 1:
    space.blit(bg,(0,0))
    space.blit(ys,(50,HEIGHT/2))
    space.blit(rs,(WIDTH-50,HEIGHT/2))




