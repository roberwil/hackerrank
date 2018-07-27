#!/bin/python3
from collections import Counter

if __name__ == '__main__':

    temp = input()
    letters = Counter(temp)

    values = list(map(int, letters.values()))
    values.sort()
    values.reverse()

    arr = [item for item in values[:3]]
    arr = list(set(arr))
    arr.sort()
    arr.reverse()

    arr_len = len(arr)
    a_arr, b_arr, c_arr = [], [], []

    for key in letters:
        if arr_len == 1:
            a_arr.append(key)
        elif arr_len == 2:
            if arr[0] == letters[key]:
                a_arr.append(key)
            if arr[1] == letters[key]:
                b_arr.append(key)
        else:
            if arr[0] == letters[key]:
                a_arr.append(key)
            if arr[1] == letters[key]:
                b_arr.append(key)
            if arr[2] == letters[key]:
                c_arr.append(key)
    
    if arr_len == 1:
        a_arr.sort()
        print ('{} {}'.format(a_arr[0], arr[0]))
        print ('{} {}'.format(a_arr[1], arr[0]))
        print ('{} {}'.format(a_arr[2], arr[0]))
    elif arr_len == 2:
        if (len(a_arr) == 2):
            a_arr.sort()
            print ('{} {}'.format(a_arr[0], arr[0]))
            print ('{} {}'.format(a_arr[1], arr[0]))
            print ('{} {}'.format(b_arr[0], arr[1]))
        else:
            b_arr.sort()
            print ('{} {}'.format(a_arr[0], arr[0]))
            print ('{} {}'.format(b_arr[0], arr[1]))
            print ('{} {}'.format(b_arr[1], arr[1]))
    else:
        print ('{} {}'.format(a_arr[0], arr[0]))
        print ('{} {}'.format(b_arr[0], arr[1]))
        print ('{} {}'.format(c_arr[0], arr[2]))
