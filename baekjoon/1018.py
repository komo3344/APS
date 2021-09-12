import sys

N, M = map(int, sys.stdin.readline().split())

board = []
for _ in range(N):
    board.append(sys.stdin.readline().strip())

check1 = 0
check2 = 0
ans = []
minimum = 64
for i in range(N-7):
    ans.append([])
    for j in range(M-7):
        for k in range(8):  # 8*8 체스판에서 칠해야 하는 칸 수 계산
            for l in range(8):
                if (k + l) % 2 == 0:
                    if board[i + k][j + l] == 'B':
                        check1 += 1
                    else:
                        check2 += 1
                else:
                    if board[i + k][j + l] == 'W':
                        check1 += 1
                    else:
                        check2 += 1
        ans[i].append(min(check1, check2))
        check1, check2 = 0, 0


for i in range(len(ans)):
    if min(ans[i]) < minimum:
        minimum = min(ans[i])
print(minimum)