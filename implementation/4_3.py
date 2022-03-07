# 게임 개발
"""
- [ ] 완전탐색(브루트 포스) 
- [✔] 시뮬레이션 
- [✔] 알고리즘을 어떻게 구현하였는가?
  - 현재 상황에서 4방향을 모두 체크한다.
  - 만약 4방향 모두 갈 수 없을 시 현재 방향에서 뒤로 간다. (이 떄 바다이거나 맵의 끝인지 판별)
시간복잡도 : O(1)

"""
n,m = map(int,input().split())

x,y,d = map(int,input().split())
dic = {0:(-1,0),1:(0,1),2:(1,0),3:(0,-1)}
maps = []
for _ in range(n):
    maps.append(list(map(int,input().split())))  # 맵 추가
print(maps)
visited = [[False for _ in range(m)] for _ in range(n)] # n*m 방문리스트
visited[x][y] = True
cnt = 0
while True:
    ini_d = d # 현재 방향
    for i in range(d-1,d-5,-1): # 4방향으로 체크
        cur_d = i%4
        nx,ny = x + dic[cur_d][0], y + dic[cur_d][1]
        if nx and ny and nx < n and ny < m and (not maps[nx][ny]) and (not visited[nx][ny]): # 갈 수 있을 시
            x,y = nx,ny
            visited[x][y] = True
            d = cur_d
            cnt+=1
            break
    else: # 4방향을 모두 돌았을 때
        back = (ini_d-2)%4
        nx,ny = x+dic[back][0], y+ dic[back][1]
        if nx<n and ny<n and maps[nx][ny] : # 바다거나 끝일 경우
            break
        else: # 뒤로 back
            x,y = nx,ny
            cnt+=1
        
print(cnt)
"""
input
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1

output
3
"""