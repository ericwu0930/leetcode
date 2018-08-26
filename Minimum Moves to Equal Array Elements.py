#时间复杂度不止O（n）
nums = [1, 2, 3]
max = 0
sum = 0
for i in nums:
    if i > max: max = i
    sum += i
j=0
while True:
    if (sum + j*(len(nums) - 1)
        ) % len(nums) == 0 and (sum + j*(len(nums) - 1)) // len(nums) >= max:
        break
    j+=1
print(j)