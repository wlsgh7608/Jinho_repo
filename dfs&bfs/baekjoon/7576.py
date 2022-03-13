"""
토마토
https://www.acmicpc.net/problem/7576
15:56 ~ 16:25
"""
import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int,input().split())
G = []
for _ in range(N):
    G.append(list(map(int,input().split())))
Q = deque()
for i in range(N):
    for j in range(M):
        if G[i][j] == 1:
            Q.append((i,j))
mx_list = [-1,1,0,0]
my_list = [0,0,1,-1]
while Q:
    x,y = Q.popleft()
    
    for mx,my in zip(mx_list,my_list):
        nx = x + mx
        ny = y + my
        if 0<=nx <N and 0<=ny<M and G[nx][ny]== 0  :
            Q.append((nx,ny))
            G[nx][ny] = G[x][y]+1
            
max_days = 0
is_zero = False

for i in range(N):
    for j in range(M):
        if  G[i][j] == 0:
            is_zero = True
        max_days = max(max_days,G[i][j])
if is_zero:
    print(-1)
else:
    print(max_days-1)





