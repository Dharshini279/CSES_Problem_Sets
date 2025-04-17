n=int(input())
arr=list(map(int,input().split()))
arr.sort()
s=1
for c in arr:
    if c>s:
        break
    else:
        s+=c
print(s)
