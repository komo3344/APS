"""
리트코드 200번 문제
"""
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            # 더 이상 땅이 아닌 경우
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
                return
            # 이미 탐색 한 것은 다른 값으로 바꿈
            grid[i][j] = '#'
            
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
            
        count = 0
        for i in range(len(grid)):          # 행 개수 반복
            for j in range(len(grid[0])):   # 열 개수 반복
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1
        return count

