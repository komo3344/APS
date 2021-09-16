"""리트코드 39번"""
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        # csum: 합을 갱신, index: 자기자신을 포함하는 순서, path: 지금까지의 탐색 경로
        def dfs(csum, index, path):
            # 목표값을 초과한 경우로 탐색을 종료
            if csum < 0:
                return
            # csum의 초기값은 target이기 때문에 csum의 0은 target과 일치하는 정답
            if csum == 0:
                result.append(path)
                return

            # 자신 부터 하위 원소 까지의 나열 재귀 호출
            for i in range(index, len(candidates)):
                dfs(csum - candidates[i], i, path + [candidates[i]])

        dfs(target, 0, [])
        return result
