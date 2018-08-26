height=[1,8,6,2,5,4,8,3,7]
left=0
right=len(height)-1
maxarea=(right-left)*min(height[left],height[right])
while left+1<right:
    if height[left]<=height[right]:
        left+=1
    else:right-=1
    newarea=(right-left)*height[left] if height[left]<=height[right] else (right-left)*height[right]
    if maxarea<newarea:maxarea=newarea
print(maxarea)
