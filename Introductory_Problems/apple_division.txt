from itertools import combinations
n=int(input())
arr=list(map(int,input().split()))
dif=float('inf')
t=sum(arr)
for i in range(n):
    m=0
    for j in combinations(arr,i):
        m=abs(sum(j)-t)
        dif=min(abs(sum(j)-m),dif)
print(dif)
