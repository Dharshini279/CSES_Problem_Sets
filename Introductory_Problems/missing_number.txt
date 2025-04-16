n=int(input())
arr=list(map(int,input().split()))
s=sum(arr)
print((n*(n+1)//2)-s)
