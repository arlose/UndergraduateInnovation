from Init import *
from Compare import *

def blobpass(screen):
    length = len(pokers)
    k = 0
    for i in range(1, length):
        if comparepoker(k, i) == LARGER:
            switchpoker(screen, k, i)
        k = i