#!/usr/bin/env python

def insert_sort(slist):
    for i in range(1, len(slist)):
        tmp = slist[i]
        if slist[i] < slist[0]:
            del slist[i]
            slist.insert(0, tmp)
        else:
            for j in range(0, i):
                if slist[j] <= slist[i] and slist[i] < slist[j+1]:
                    del slist[i]
                    slist.insert(j+1, tmp)

    return slist


if __name__ == '__main__':
    print(insert_sort([1,2,3,4,5,6,7,8,9]))
    print(insert_sort([3,1,2,9,6,5,7,8,4]))
    print(insert_sort([99,45,96,43,62,0,60,4,23,19,13,99,28,1,2,3,9,2]))

