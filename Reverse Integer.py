x=12345
# print(2**32-1)
# min_flag=0
# res_list=[]
# res=0
# if x<0:
#     min_flag=1
#     x=-x
# tmp_a=str(x)
# for i in tmp_a:
#     res_list.append(int(i))
# for i in range(len(res_list)-1,-1,-1):
#     res+=10**i*res_list[i]
# if min_flag:res=-res
# print(res)
min_flag=0
res=0
if x<0:
    x=-x
    min_flag=1
while x!=0:
    pop=x%10
    x=int(x/10)
    res=10*res+pop
    if min_flag==1:
        if res<-2**31:
            res=0
            break
    else:
        if res>2**31-1:
            res=0
            break
if min_flag==1:
    res=-res
print(res)




