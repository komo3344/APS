import itertools
import sys
from typing import List


class Solution:
    def permute1(self, nums: List[int]) -> List[List[int]]:
        results = []
        prev_elements = []

        def dfs(elements):
            # 리프 노드일 때 결과 추가
            if len(elements) == 0:
                results.append(prev_elements[:])
            # 순열 생성 재귀호출
            for e in elements:
                next_elements = elements[:]
                next_elements.remove(e)

                prev_elements.append(e)
                dfs(next_elements)
                prev_elements.pop()

        dfs(nums)
        return results

    def permute2(self, nums: List[int]) -> List[List[int]]:
        return list(map(list, list(itertools.permutations(nums))))


if __name__ == "__main__":
    user_input = list(map(int, sys.stdin.readline().split()))
    s = Solution()
    print(s.permute1(user_input))
    print(s.permute2(user_input))
