# 정렬이란?

데이터를 특정한 기준에 따라서 순서대로 나열하는 것
정렬을 통하여 이진탐색(Binary Search) 가능
정렬 알고리즘 종류 : 선택 정렬, 삽입 정렬, 퀵 정렬, 계수 정렬


## 선택정렬
가장 작은 데이터를 선택해 맨 앞의 데이터와 바꾸고, 그 다음 작은 데이터를 선택해 앞에서 두번 째 데이터와 바꾸는 과정

선택정렬 코드
``` python
arr = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
    min_idx = i
    if arr[min_idx] > arr[i]:
        min_idx= i
    arr[i], arr[min_idx] = arr[min_idx], arr[i]

print(arr)
```

시간복잡도 - O(n^2)

## 삽입 정렬
데이터를 하나씩 확인하여, 각 데이터를 적절한 위치에 삽입하는 정렬
필요할 때만 위치를 바꾸므로 '데이터가 거의 정렬된 형태'일 때 효율적

``` python
arr = [7,5,9,0,3,1,6,2,4,8]

for i in range(1,len(array)):
    for j in range(i,0,-1):
        if arr[j] < arr[j-1]:
            arr[j],arr[j-1] = arr[j-1],arr[j]
        else:
            break
print(arr)
```
시간복잡도 - O(n^2)
최선의 경우 - O(n)

## 퀵 정렬
기준 데이터(pivot)를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 정렬 알고리즘