#!/usr/bin/env python
import sys
import argparse
import utility

def bonus(arr, target):
    '''
    prints 3 items whose prices sum up to target
    todo:
     * modularize find_price and bonus.py
    :param arr: an array containing tuples(item,value)
    :param target: integer
    :return:
    '''
    if len(arr) < 3:
        print("Not possible")
        return
    closest_k, closest_l, closest_r = None, None, None
    for k in range(len(arr)-2):
        left = k+1
        right = len(arr)-1
        while(left<right):
            sum = arr[k][1] + arr[left][1] + arr[right][1]
            if sum == target:
                print(str(arr[k][0]) + " " + str(arr[k][1]) +", "+ str(arr[left][0]) + " " + str(arr[left][1]) + ", " + str(arr[right][0]) + " " + str(arr[right][1]))
                return
            elif sum < target:
                if closest_l:
                    if sum > closest_k[1] + closest_l[1]+closest_r[1]:
                        closest_k, closest_l, closest_r = arr[k], arr[left], arr[right]
                else:
                    closest_k, closest_l, closest_r = arr[k], arr[left], arr[right]
                left+=1
            else:
                right-=1
    if closest_k:
        print(str(closest_k[0]) + " " + str(closest_k[1]) + ", " + str(closest_l[0]) + " " + str(closest_l[1]) + ", " + str(closest_r[0]) + " " + str(closest_r[1]))
        return
    print("Not possible")
    return


def main(argv):
    '''
    :param Processes arguments from command line:
    :return:
    '''
    parser = argparse.ArgumentParser(description="Find items to buy with a gift card")
    parser.add_argument('filename', type=str, help='name of file containing items and prices')
    parser.add_argument('target', type=int, help='amount available in gift card')
    args = parser.parse_args()
    bonus(utility.read_file(args.filename),args.target)

if __name__ == "__main__":
    main(sys.argv[:])


