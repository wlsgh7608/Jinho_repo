from bisect import bisect_left, bisect_right

L = [1,1,2,2,3,3,4,4,5,5]


def lower_bound(s,e,k):
    while s<e:
        m = (s+e)//2
        if L[m] < k:
            s = m+1
        else:
            e = m
    return e


    
def upper_bound(s,e,k):
    while s< e:
        m = (s+e)//2
        if L[m] <= k:
            s = m+1
        else:
            e = m
    return e

print(L)

s,e = 0,len(L)


print("4")
print("lower bound")
print("내꺼",lower_bound(s,e,4))
print("정답",bisect_left(L,4))
print("upper bound")
print("내꺼",upper_bound(s,e,4))

print("정답",bisect_right(L,4))
print("______________________________________")
print("5")
print("lower bound")
print("내꺼",lower_bound(s,e,5))
print("정답",bisect_left(L,5))
print("upper bound")
print("내꺼",upper_bound(s,e,5))
print("정답",bisect_right(L,5))