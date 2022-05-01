def longestPalindrome(self, s: str) -> str:
    # 팰린드롬 판별 및 투포인터 확장
    def expand(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    # 해당 사항이 없을 때 빠르게 리턴
    if len(s) < 2 or s == s[::-1]:
        return s

    result = ''
    for i in range(0, len(s) - 1):
        # 짝수, 홀수일 경우 고려하여 2개의 윈도우 이동
        result = max(result,
                     expand(i, i+1),    # 짝수 윈도우
                     expand(i, i+2),    # 홀수 윈도우
                     key=len)

    return result
