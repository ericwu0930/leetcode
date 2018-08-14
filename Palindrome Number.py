x=21120
# tmp_x=str(x)
# flag=1
# pointer=0
# while x!=0 and flag:
#     if x%10==int(tmp_x[pointer]):
#         x=x//10
#         pointer+=1
#     else:
#         flag=0
# if flag==1:
#     print(True)
# else:
#     print(False)

tmp_x=0
while tmp_x<x and x//10:
    tmp=x%10
    x//=10
    tmp_x=tmp_x*10+tmp
if tmp_x==x or tmp_x//10==x:
    print(True)
else:
    print(False)

    