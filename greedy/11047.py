n,k = map(int,input().split())
coin_list = []



for _ in range(n):
    coin = int(input())
    coin_list.append(coin)


idx = n-1
cnt = 0
while k:
    # Ai은 Ai-1의 배수임
    coin_cnt = k // coin_list[idx]
    k %= coin_list[idx]
    cnt += coin_cnt

    idx-=1
    

print(cnt)