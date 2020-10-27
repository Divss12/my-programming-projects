import pygame
import sys

pygame.init()

background = pygame.Surface((100,100))
pygame.draw.rect(background,(255,255,255),(0,0,10,10),width=1)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
