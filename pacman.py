import pygame,pyautogui,time
from pygame.locals import *
pygame.init()
WIDTH,HEIGHT=pyautogui.size()
maze=pygame.display.set_mode((WIDTH,HEIGHT))
bg=pygame.transform.scale(pygame.image.load("pacbak.webp"),(WIDTH,HEIGHT))
pac=pygame.transform.scale(pygame.image.load("pac.png"),(150,150))
pacx=WIDTH/2 
pacy=HEIGHT/2


while pacy<HEIGHT:
    maze.blit(bg,(0,0))
    maze.blit(pac,(pacx,pacy))
    pygame.display.flip()
    for i in pygame.event.get():
            if i.type==pygame.QUIT:
                pygame.quit()
            if i.type==pygame.KEYDOWN:
                if i.key==pygame.K_LEFT:
                    pacx-=20
                if i.key==pygame.K_RIGHT:
                    pacx+=20
                if i.key==pygame.K_UP:
                    pacy-=20
                if i.key==pygame.K_DOWN:
                    pacy+=20
    pacy+=1      