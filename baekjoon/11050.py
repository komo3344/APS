import sys
from itertools import combinations
from math import comb


def solution1():
    a, b = list(map(int, sys.stdin.readline().split()))

    def factorial(num):
        result = 1
        for i in range(num, 1, -1):
            result *= i
        return result

    print(factorial(a) // (factorial(a-b) * factorial(b)))


def solution2():
    a, b = list(map(int, sys.stdin.readline().split()))
    L = [i for i in range(a)]
    print(len(list(combinations(L, b))))


# python 3.8 이상
def solution3():
    a, b = list(map(int, sys.stdin.readline().split()))
    print(comb(a, b))


solution2()