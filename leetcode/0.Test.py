from collections import deque
from typing import List


def inplaceArray(arr: List[int]):
    arr[1] = 2

def sortArray(arr: List[int]):
    arr.sort()

def reverseArray(arr: List[int]):
    return reversed(arr)

def testArray():
    arr = list(range(5))

    inplaceArray(arr)

    print(arr)


def testDict():
    d = dict()

    d.get(1, -1)


if __name__ == '__main__':
   testArray()

    # a = [1,2,3]
    # a.pop()
    # a.append([2, 3])
    # print(a)x
    #
    # print(a+[1,3])
    #
    # print(a.pop(0))
    # print(a)
    #
    # q = deque()
    #
    # dict().val
