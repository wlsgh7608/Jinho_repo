"""
https://www.acmicpc.net/problem/1167
트리의 지름 / 골드 3 /
"""
import sys
input = sys.stdin.readline
n = int(input())
G = [[] for _ in range(n)]

def bfs(vertex):
    from collections import deque
    max_len = 0
    visited = [False for _ in range(len(G))]
    visited[vertex] = True
    Q = deque()
    Q.append((vertex,0))
    while Q:
        v,w = Q.popleft()
        max_len = max(max_len,w)
        for next,n_w in G[v]:
            if not visited[next]:
                visited[next] = True
                Q.append((next,w+n_w))
    return max_len


for _ in range(n):
    a, *next = map(int,input().split())
    next = next[:-1]
    i = 0
    while i <len(next):
        b,w = next[i],next[i+1]
        G[a-1].append((b-1,w))
        i+=2


max_dist = 0
for i in range(len(G)):
    max_dist = max(max_dist,bfs(i))
    
print(max_dist)