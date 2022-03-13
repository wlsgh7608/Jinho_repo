import sys
input = sys.stdin.readline
N,M = map(int,input().split())
G = []
for _ in range(N):
    G.append(list(map(int,input().rstrip())))
    
print(G)
"""
input
4 5 
00110
00011
11111
00000


output
3
"""