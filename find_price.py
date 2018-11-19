#!/usr/bin/env python
import sys
import argparse
import utility

def find_price(arr, target):
    '''
    prints 2 items whose prices sum up to target
    :param arr: an array containing tuples(item,value)
    :param target: integer
    :return:
    '''
    if len(arr) < 2:
        print("Not possible")
        return
    left = 0
    right = len(arr)-1
    closest_l, closest_r = None, None
    while(left<right):
        sum = arr[left][1] + arr[right][1]
        if sum == target:
            print(str(arr[left][0]) + " " + str(arr[left][1]) + ", " + str(arr[right][0]) + " " + str(arr[right][1]))
            return
        if sum < target:
            if closest_l:
                if sum > closest_l[1]+closest_r[1]:
                    closest_l, closest_r = arr[left], arr[right]
            else:
                closest_l, closest_r = arr[left],arr[right]
            left+=1
        else:
            right-=1
    if closest_l:
        print(str(closest_l[0]) + " " + str(closest_l[1]) + ", " + str(closest_r[0]) + " " + str(closest_r[1]))
        return
    print("Not possible")


def main(argv):
    '''
    :param Processes arguments from command line:
    :return:
    '''
    parser = argparse.ArgumentParser(description="Find items to buy with a gift card")
    parser.add_argument('filename', type=str, help='name of file containing items and prices')
    parser.add_argument('target', type=int, help='amount available in gift card')
    args = parser.parse_args()
    find_price(utility.read_file(args.filename),args.target)

if __name__ == "__main__":
    main(sys.argv[:])



