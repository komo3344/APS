"""
11650번
좌표 정렬하기
"""
# n = int(input())
# result = []
# for i in range(n):
#     p = list(map(int, input().split()))
#     result.append(p)
#
# result = sorted(result, key=lambda x: (x[0], x[1]))
#
# for x in result:
#     print(x[0], x[1])


import sys
n = int(sys.stdin.readline())
result = []
for i in range(n):
    result.append(list(map(int, sys.stdin.readline().split())))
result = sorted(result, key=lambda x: (x[0], x[1]))
for i in result:
    print(i[0], i[1])
