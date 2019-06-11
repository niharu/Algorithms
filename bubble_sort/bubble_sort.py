#!/usr/bin/env python

def bubble_sort(slist):
    for i in range(len(slist) - 1):
        for j in range(len(slist) - 1):
            if slist[j] > slist[j+1]:
                slist[j], slist[j+1] = slist[j+1], slist[j]

    return slist


if __name__ == '__main__':
    print(bubble_sort([1,2,3,4,5,6,7,8,9]))
    print(bubble_sort([3,1,2,9,6,5,7,8,4]))
    print(bubble_sort([99,45,96,43,62,0,60,4,23,19,13,99,28,1,2,3,9,2]))
