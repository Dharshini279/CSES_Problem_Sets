n=int(input())
arr=list(map(int,input().split()))
l=0
m=0
vis=set()
for r in range(n):
    while arr[r] in vis:
        vis.remove(arr[l])
        l+=1
    vis.add(arr[r])
    m=max(m,r-l+1)
print(m)
