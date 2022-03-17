"""
https://www.acmicpc.net/problem/2751

"""
import sys
input = sys.stdin.readline
n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))

numbers.sort()
for i in numbers:
    print(i)