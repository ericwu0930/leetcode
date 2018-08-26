candies=[1,2,2,3,1,2,5,4,3,4]
n=len(candies)//2
m=len(set(candies))
print(n) if n<=m else print(m)
#set() 函数创建一个无序不重复元素集
# 可进行关系测试，删除重复数据，还可以计算交集、差集、并集等。
            