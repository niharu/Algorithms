#!/usr/bin/env python

def selection_sort(slist):
    for i in range(len(slist)):
        min_index = i
        for j in range(i + 1, len(slist)):
            if slist[min_index] > slist[j]:
                min_index = j

        slist[i], slist[min_index] = slist[min_index], slist[i]

    return slist


if __name__ == '__main__':
    print(selection_sort([1,2,3,4,5,6,7,8,9]))
    print(selection_sort([3,1,2,9,6,5,7,8,4]))
    print(selection_sort([99,45,96,43,62,0,60,4,23,19,13,99,28,1,2,3,9,2]))
    
