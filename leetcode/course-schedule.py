"""
207 - https://leetcode.com/problems/course-schedule/
"""
import collections

from typing import List


class Solution:
    # solution1 DFS로 순환 구조 판별
    def canFinish_1(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        # 그래프 구성
        for x, y in prerequisites:
            graph[x].append(y)
        print(graph)
        traced = set()

        def dfs(i):
            # 순환 구조이면 False
            if i in traced:
                return False

            traced.add(i)
            for y in graph[i]:
                if not dfs(y):
                    return False

            # 탐색 종료 후 순환 노드 삭제
            traced.remove(i)

            return True

        # 순환 구조 판별
        for x in list(graph):
            if not dfs(x):
                return False
        return True

    # solution2 가지치기를 이용한 최적화
    def canFinish_2(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        # 그래프 구성
        for x, y in prerequisites:
            graph[x].append(y)
        print(graph)
        traced = set()
        visited = set()

        def dfs(i):
            # 순환 구조이면 false
            if i in traced:
                return False

            # 이미 방문했던 노드이면 True
            if i in visited:
                return True

            traced.add(i)
            print(f"add - traced: {traced}")
            for y in graph[i]:
                if not dfs(y):
                    return False
            # 탐색 종료 후 순환노드 삭제
            traced.remove(i)
            print(f"remove - traced: {traced}")
            # 탐색 종료 후 방문 노드 추가
            visited.add(i)
            print(f"visited: {visited}")

            return True

        # 순환 구조 판별
        for x in list(graph):
            print("list graph", x, graph)
            if not dfs(x):
                return False

            return True

prerequisites = [[0, 1], [2, 0], [1, 2]]

solution = Solution()
# x = solution.canFinish_1(2, [[1, 0]])
# y = solution.canFinish_2(2, [[1, 0], [0, 1]])

z = solution.canFinish_2(3, prerequisites)

print(z)
