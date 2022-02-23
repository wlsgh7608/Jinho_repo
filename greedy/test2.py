

n = int(input())

board = []

for _ in range(n):
    s,e = map(int,input().split())
    board.append((s,e))

board.sort(key = lambda x : x[0])
print(board)