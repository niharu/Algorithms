#!/usr/bin/env python
import time
import random

def bubble_sort(slist):
    for i in range(len(slist) - 1):
        isChange = False
        for j in range(len(slist) - 1):
            if slist[j] > slist[j+1]:
                slist[j], slist[j+1] = slist[j+1], slist[j]
                isChange = True

        if not(isChange):
            break

    return slist


if __name__ == '__main__':
    #slist = [i for i in range(10000, 1, -1)]
    slist = [i for i in range(1, 5000)]
    #slist = [random.randint(0, 3000) for i in range(1, 3000)]
    #print(slist)
    start = time.time()
    bubble_sort(slist)
    print(time.time() - start)

