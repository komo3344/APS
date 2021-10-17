"""리트코드 332번 문제"""
from typing import List
import collections

tickets = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]


def findItinerary(tickets: List[List[str]]) -> List[str]:
    # 그래프 구성
    graph = collections.defaultdict(list)

    # 1)
    # for a, b in tickets:
    #     graph[a].append(b)
    # for a in graph:
    #     graph[a].sort()

    # 2)
    for a, b in sorted(tickets):
        print(a, b)
        graph[a].append(b)
    print("그래프: ", graph)
    route = []

    def dfs(a):
        # 첫 번째 값을 읽어 어휘 순 방문
        while graph[a]:
            dfs(graph[a].pop(0))
        route.append(a)

    dfs('JFK')
    print("결과: ", route)
    # 다시 뒤집어 어휘 순 결과로
    return route[::-1]


"""
ATL JFK
"""

answer = findItinerary(tickets)
print(answer)


def findItinerary2(tickets: List[List[str]]) -> List[str]:
    graph = collections.defaultdict(list)
    for a, b in sorted(tickets, reverse=True):
        graph[a].append(b)
    route = []
    print("그래프: ", graph)

    def dfs(a):
        while graph[a]:
            dfs(graph[a].pop())
        route.append(a)

    dfs('JFK')
    return route[::-1]


answer = findItinerary2(tickets)
print(answer)


def findItinerary3(tickets: List[List[str]]) -> List[str]:
    pass
    # graph = collections.defaultdict(list)
    # for a, b in sorted(tickets, reverse=True):
    #     graph[a].append(b)
    # route = []
    # print("그래프: ", graph)
    #
    # def dfs(a):
    #     while graph[a]:
    #         dfs(graph[a].pop())
    #     route.append(a)
    #
    # dfs('JFK')
    # return route[::-1]