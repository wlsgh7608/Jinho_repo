"""
https://www.acmicpc.net/problem/12015
가장 긴 증가하는 부분 수열 2 / 골드 2 / 40분
"""
import sys
input =  sys.stdin.readline
n = int(input())
n_list = list(map(int,input().split()))

max_lists = []
def idx_check(arr,target):
    lo ,hi = 0, len(arr)-1
    while lo <=hi:
        m = (lo+hi)//2
        if arr[m] >= target:
            hi = m-1
        else:
            lo = m+1
    return lo

for number in n_list:
    idx = idx_check(max_lists,number)
    if idx == len(max_lists):
        max_lists.append(number)
    else:
        max_lists[idx] = number

print(len(max_lists))

""""
input 
1
10 5
"""