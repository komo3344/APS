from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(index, path):
            result.append(path)
            # print(result)
            for i in range(index, len(nums)):
                dfs(i + 1, path + [nums[i]])

        dfs(0, [])
        return result


input = [1, 2, 3]
output = [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
solution = Solution()
answer = solution.subsets(input)
print(answer)
if output == answer:
    print('정답')
