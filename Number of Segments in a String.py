s="           "
num=0
blank_flag=0
seg_flag=0
for i in s:
    if i!=" ":
        seg_flag=1
    elif i==" " and seg_flag==1:
        blank_flag=1
    if seg_flag and blank_flag:
        num+=1
        seg_flag=0
        blank_flag=0
if blank_flag==0 and seg_flag==1:
    print(num+1)
else:
    print(num)