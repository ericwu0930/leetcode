s = "bananas"
dirc = {}
for i in s:
    if dirc.get(i) == None:
        dirc[i] = 1
    else:
        dirc[i] += 1
has_odd = 0
num = 0
for i in dirc.values():
    if i % 2 == 1: 
        has_odd = 1
        num+=i-1
    else: num += i
if has_odd: num += 1
print(num)