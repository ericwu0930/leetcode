import numpy as np
s = "abcba"
# 暴力解
# while len(s)-i>max_num:
#     j=len(s)-1
#     while j-i+1>max_num:
#         tmp_i = i
#         tmp_j = j
#         while tmp_i <= tmp_j:
#             if s[tmp_i] == s[tmp_j]:
#                 tmp_i += 1
#                 tmp_j -= 1
#             else:
#                 break
#         if tmp_i>tmp_j and j-i+1>max_num:
#             max_num=j-i+1
#             max_str=s[i:j+1]
#         j-=1
#     i+=1
# print(max_num)
# 动态规划
# table = np.zeros((len(s), len(s)))
# max_num = 0
# max_s = ""
# for i in range(len(s)):
#     for j in range(len(s) - i):
#         if i == 0:
#             table[j][j] = 1
#             if max_num < 1:
#                 max_num = 1
#                 max_s = s[j]
#         elif i == 1:
#             if s[j] == s[j + 1]:
#                 table[j][j + 1] = 1
#                 if max_num < 2:
#                     max_num = 2
#                     max_s = s[j:j + i + 1]
#         elif s[j] == s[j + i] and table[j + 1][j + i - 1]:
#             table[j][j + i] = 1
#             if max_num < i + 1:
#                 max_num = i + 1
#                 max_s = s[j:j + i + 1]
# print(max_s)
# 动态规划优化空间

max_num=1
max_s=s[0]
tmp_list=np.zeros(len(s))
for i in range(len(s)-1,-1,-1):
    for j in range(len(s)-1,i-1,-1):
        if i==j:
            tmp_list[j]=1
        elif i+1==j:
            if s[i]==s[j]:
                tmp_list[j]=1
                if max_num<2:
                    max_num=2
                    max_s=s[i:j+1]
            else:
                tmp_list[j]=0
        elif s[i]==s[j] and tmp_list[j-1]:
            tmp_list[j]=1
            if max_num<j-i+1:
                max_num=j-i+1
                max_s=s[i:j+1]
        else:
            tmp_list[j]=0
print(max_s)
        
# 中间扩张
# max_num = 1
# if not s: max_s = ''
# else: max_s = s[0]


# def expend(left, right, s):
#     while left >= 0 and right < len(s) and s[left] == s[right]:
#         left -= 1
#         right += 1
#     return right - left - 1


# for i in range(1, len(s) - 1):
#     len1 = expend(i - 1, i, s)
#     len2 = expend(i - 1, i + 1, s)
#     if len1 >= len2:
#         if max_num < len1:
#             max_num = len1
#             max_s = s[i - int(len1 / 2):i + int(len1 / 2)]
#     if len2 > len1:
#         if max_num < len2:
#             max_num = len2
#             start = i - int((len2 - 1) / 2)
#             end = i + int((len2 - 1) / 2)
#             max_s = s[start:end + 1]
# len3 = expend(len(s) - 2, len(s) - 1, s)
# if max_num < len3:
#     max_num = len3
#     max_s = s[len(s) - int(len3 / 2):len(s)]
# print(max_s)
