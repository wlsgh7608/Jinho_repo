"""
https://www.acmicpc.net/problem/10816
숫자카드 2 / 실버 4 / 75분
20:42 ~ 21:55
"""
import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
            

N = int(input())
numbers = list(map(int,input().split()))
M = int(input())
targets  = list(map(int,input().split()))
numbers.sort()


result = []
for t in targets:
    s = 0
    e = N-1
    up = bisect_right(numbers,t)
    down = bisect_left(numbers,t)
    print(up-down,end=" ")