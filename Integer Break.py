n=6
f=[0*n for i in range(n+1)]
# f[2]=1
# f[3]=2
# f[4]=4
# f[5]=6
for i in range(2,n+1):
    for j in range(1,i):
        if i-j==2 or i-j==3 or i-j==1:
            f[i]=max(f[i],j*(i-j))
        else:
            f[i]=max(f[i],j*f[i-j])
print(f[n])
