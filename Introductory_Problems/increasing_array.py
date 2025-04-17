n=int(input())
arr=list(map(int,input().split()))
m=0
for i in range(1,n):
    if arr[i-1]>arr[i]:
        m+=arr[i-1]-arr[i]
        arr[i]=arr[i-1]
print(m)
