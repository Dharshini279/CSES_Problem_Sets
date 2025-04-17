n=int(input())
arr=list(map(int,input().split()))
ans=1
dp=[0]*(n+1)
for i in range(n):
    dp[arr[i]]=i
for i in range(2,n+1):
    if dp[i]<dp[i-1]:
        ans+=1
print(ans)
