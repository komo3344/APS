# 리트코드 77번 문제
import itertools
from typing import List


class Solution:
    def combine1(self, n: int, k: int) -> List[List[int]]:
        l = [i for i in range(1, n + 1)]
        return list(itertools.combinations(l, k))

    def combine2(self, n: int, k: int) -> List[List[int]]:
        results = []

        def dfs(elements, start, k):
            if k == 0:
                results.append(elements[:])
                return

            # 자신 이전의 모든 값을 고정하여 재귀 호
            for i in range(start, n+1):
                elements.append(i)
                dfs(elements, i+1, k-1)
                elements.pop()

        dfs([], 1, k)
        return results


"""
n -> 세로
k -> 세로 범위 설
1    1    1
2    2    2
3    3    3
4    4    4
5    5    5
"""