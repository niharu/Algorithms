#!/usr/bin/env python

def simple_sort(slist):
    for i in range(len(slist)):
        for j in range(len(slist[i+1::])):
            if slist[i] > slist[i+1::][j]:
                tmp = slist[i]
                slist[i] = slist[i+1+j]
                slist[i+1+j] = tmp
    return slist


if __name__ == '__main__':
    print(simple_sort([1,2,3,4,5,6,7,8,9]))
    print(simple_sort([3,1,2,9,6,5,7,8,4]))
    print(simple_sort([99,45,96,43,62,0,60,4,23,19,13,99,28,1,2,3,9,2]))
