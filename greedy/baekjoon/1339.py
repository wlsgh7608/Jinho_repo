"""
https://www.acmicpc.net/problem/1339

"""




n = int(input())
max_len = 0
words = []

c_list = set()
for _ in range(n):
    word = input()
    words.append(word)
    max_len = max(max_len,len(word))

for word in words:
    for c in word:
        c_list.add(c)

for _ in range(n):
    print("")


print(c_list)
# numbers = [(9-i) for i in range(10)]

# max_chr = None
# D = {}
# for i in range(max_len,0,-1):
#     alp_dic = {}
#     for word in words:
#         if len(word)>=i:
#             idx = len(word)-i
#             if idx in alp_dic:
#                 alp_dic[idx]+=1
#             else:
#                 alp_dic[idx] = 1
            

"""
988
 88
 88
 88
 88
 88
 88
 88
 88
 88
"""
