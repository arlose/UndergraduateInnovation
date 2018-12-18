# -*- coding:utf-8 -*-
import pygame
import sys
from pygame.locals import *
import random

from Config import *
from Init import *
from Compare import *
from BlobSort import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((Width, Height), pygame.RESIZABLE, 0)
    pygame.display.set_caption("Poker")
    clock = pygame.time.Clock()

    sample = pygame.image.load('../../PokerImages/card_CA.png')
    size = sample.get_rect().size # 455*680
    pokersinit(size)
    random.shuffle(pokers)

    length = len(pokers)
    first = True

    # for Blob Sort
    for i in range(length):
        Tmp.append(pokers[i])

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                random.shuffle(pokers)
                first = True
            keystate = pygame.key.get_pressed()
            sortflag = keystate[K_SPACE]
            if sortflag:
                for i in range(length):
                    blobpass(screen)
        if first:
            screen.fill(blue)
            for i in range(length):
                screen.blit(pokers[i][0], (10+i*Xoffset,20))
            first = False
            pygame.display.update()
        clock.tick(30)
    pygame.quit()
    
if __name__ == '__main__':
    main()
