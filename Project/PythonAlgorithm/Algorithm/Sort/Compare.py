
import pygame
from Init import Tmp
from Config import *


def switch4bit(x):
    y = x>>4
    x = (x&0xF) << 4
    y = x|y
    return y

def comparepoker(x, y, flag = False):
    # flag True H > S > D > C
    if flag:
        if Tmp[x][1] > Tmp[y][1]:
            return LARGER
        elif Tmp[x][1] < Tmp[y][1]:
            return SMALLE
        else:
            return EQUAL
    # flag False A > K > Q > J > T > 9 > 8 > 7 > 6 > 5 > 4 > 3 > 2
    else:
        if switch4bit(Tmp[x][1]) > switch4bit(Tmp[y][1]):
            return LARGER
        elif switch4bit(Tmp[x][1]) < switch4bit(Tmp[y][1]):
            return SMALLER
        else:
            return EQUAL

def switchpoker(screen, x, y):
    screen.fill(blue)
    length = len(Tmp)

    for i in range(length):
        screen.blit(Tmp[i][0], (10+i*Xoffset,20))

    clock = pygame.time.Clock()
    for i in range(length):
        if i!=x and i!=y:
            screen.blit(Tmp[i][0], (10+i*Xoffset,20+Yoffset))
        else:
            screen.blit(Tmp[i][0], (10+i*Xoffset,20+Yoffset-10))
    pygame.time.wait(WAITTIME)
    pygame.display.update()
    tmp = Tmp[x]
    Tmp[x] = Tmp[y]
    Tmp[y] = tmp
    for i in range(length):
        if i!=x and i!=y:
            screen.blit(Tmp[i][0], (10+i*Xoffset,20+Yoffset))
        else:
            screen.blit(Tmp[i][0], (10+i*Xoffset,20+Yoffset-10))
    pygame.time.wait(WAITTIME)

    for i in range(length):
        screen.blit(Tmp[i][0], (10+i*Xoffset,20))

    pygame.display.update()
