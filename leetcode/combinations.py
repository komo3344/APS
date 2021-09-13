# 리트코드 77번 문제
import itertools
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        l = [i for i in range(1, n + 1)]
        return list(itertools.combinations(l, k))
