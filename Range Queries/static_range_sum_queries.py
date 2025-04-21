from collections import deque
n,m=map(int,input().split())
arr=list(map(int,input().split()))
q1=[tuple(map(int,input().split())) for i in range(m)]
q=deque(q1)
dp=[0]*(n+1)
for i in range(n):
    dp[i+1]=dp[i]+arr[i]
while q:
    f,l=q.popleft()
    print(dp[l]-dp[f-1]) 
    
