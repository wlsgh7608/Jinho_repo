# https://www.acmicpc.net/problem/1931

n = int(input())



board = []
for _ in range(n):
    s,e = map(int,input().split())
    board.append((s,e))


board.sort(key = lambda x:(x[1],x[0])) # 종료시간, 시작시간 sort
# LIS 
dp = [1 for _ in range(n)]
for i in range(1,n):
    for j in range(i):
        if board[i][0] >= board[j][1] :
            dp[i] = max(dp[i],dp[j]+1)
print(dp)
print(dp[-1])

[5,2,3,6,7,8]