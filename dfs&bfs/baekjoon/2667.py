"""
단지번호 붙이기
https://www.acmicpc.net/problem/2667
15:37 ~ 15:54
"""
import sys
sys.setrecursionlimit(10**6)

def dfs(x,y):
    cnt = 1
    if 0<=x<N and 0<=y<N and G[x][y] == 1:
        G[x][y] = 2
        cnt+=dfs(x-1,y)
        cnt+=dfs(x,y-1)
        cnt+=dfs(x,y+1)
        cnt+=dfs(x+1,y)
        return cnt
    return 0


N = int(input())
G = []
for _ in range(N):
    G.append(list(map(int,input())))

apts = []

for i in range(N):
    for j in range(N):
        if G[i][j]==1:
            apts.append(dfs(i,j))
apts.sort()
print(len(apts))
for apt in apts:
    print(apt)