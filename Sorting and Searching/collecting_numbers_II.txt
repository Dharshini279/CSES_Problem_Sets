n,m=map(int,input().split())
arr=list(map(int,input().split()))
ans=1
dp=[0]*(n+1)
for j in range(n):
    dp[arr[j]]=j
for j in range(2,n+1):
    if dp[j]<dp[j-1]:
        ans+=1
for _ in range(m):
    v1,v2=map(int,input().split())
    v1-=1
    v2-=1
    x,y=arr[v1],arr[v2]
    vis=set()
    for v in [x,y]:
        for d in [v-1,v]:
            if 1<=d<n:
                vis.add(d)
    for i in vis:
        if dp[i]>dp[i+1]:
            ans-=1
    arr[v1],arr[v2]=arr[v2],arr[v1]
    dp[x],dp[y]=v2,v1
    for i in vis:
        if dp[i]>dp[i+1]:
            ans+=1
    print(ans)
            
